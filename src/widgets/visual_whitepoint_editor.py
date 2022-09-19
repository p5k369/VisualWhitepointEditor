"""VisualWhitepointEditor widget."""
from copy import copy

from PyQt6.QtCore import QPointF, pyqtSignal, pyqtSlot
from PyQt6.QtGui import QBrush, QColor, QResizeEvent, QIcon
from PyQt6.QtWidgets import QGraphicsItem, QGraphicsView, QWidget, QMessageBox

from src.gen.ui_white_point_editor import Ui_white_point_editor
from src.widgets.color_rect import ColorRect


class VisualWhitePointEditor(QWidget):
    """VisualWhitePointEditor widget."""

    color_changed = pyqtSignal(QColor)

    def __init__(self, parent: QWidget | None = None) -> None:
        """Create a new VisualWhitePointEditor."""
        super().__init__(parent)

        self._ui = Ui_white_point_editor()
        self._ui.setupUi(self)
        self._color: QColor = QColor(255, 255, 255, 1)
        self._view: QGraphicsView = self._ui.graphicsView
        self._view.setBackgroundBrush(self._color)
        self._background_color_value: float = 1

        self._rect = ColorRect(0, 0, 300, 300)
        self._rect.setBrush(QBrush(self._color))
        self._rect.setFlags(
            QGraphicsItem.GraphicsItemFlag.ItemIsSelectable
            | QGraphicsItem.GraphicsItemFlag.ItemIsMovable
        )
        self._view.scene().addItem(self._rect)

        self._ui.color_circle.color_changed.connect(self.on_color_change)
        self._ui.color_red_sb.valueChanged.connect(
            lambda x: setattr(
                self._ui.color_circle,
                "red",
                (x / self._ui.color_red_sb.maximum()),
            )
        )
        self._ui.color_green_sb.valueChanged.connect(
            lambda x: setattr(
                self._ui.color_circle,
                "green",
                (x / self._ui.color_green_sb.maximum()),
            )
        )
        self._ui.color_blue_sb.valueChanged.connect(
            lambda x: setattr(
                self._ui.color_circle,
                "blue",
                (x / self._ui.color_blue_sb.maximum()),
            )
        )
        self._ui.hue_sb.valueChanged.connect(
            lambda x: setattr(
                self._ui.color_circle, "hue", (x / self._ui.hue_sb.maximum())
            )
        )
        self._ui.saturation_sb.valueChanged.connect(
            lambda x: setattr(
                self._ui.color_circle,
                "saturation",
                (x / self._ui.saturation_sb.maximum()),
            )
        )

        self._ui.value_sb.valueChanged.connect(
            lambda x: self.on_foreground_value_change(
                (x / self._ui.value_sb.maximum())
            )
        )
        self._ui.inner_value_slider.valueChanged.connect(
            lambda x: self.on_foreground_value_change(
                x / self._ui.inner_value_slider.maximum()
            )
        )
        self._ui.outer_value_slider.valueChanged.connect(
            lambda x: self.on_background_value_change(
                x / self._ui.inner_value_slider.maximum()
            )
        )
        self._ui.reset_btn.clicked.connect(self.on_reset_whitepoint)

        self._ui.size_slider.valueChanged.connect(self.on_size_changed)
        self._ui.center_btn.setIcon(
            QIcon("src/resources/icons/filter_center_focus_black_48dp.svg")
        )
        self._ui.center_btn.clicked.connect(self.on_center_rect)
        self._ui.reset_size_btn.setIcon(
            QIcon("src/resources/icons/aspect_ratio_black_48dp.svg")
        )
        self._ui.reset_size_btn.clicked.connect(
            lambda x: self._ui.size_slider.setValue(30)
        )
        self._ui.measure_btn.clicked.connect(self.on_measurement)

    def _toggle_ui_signals(self) -> None:
        """Block and unblock signals of ui elements."""
        elements = [
            self._ui.color_red_sb,
            self._ui.color_green_sb,
            self._ui.color_blue_sb,
            self._ui.value_sb,
            self._ui.saturation_sb,
            self._ui.hue_sb,
            self._ui.inner_value_slider,
        ]
        for element in elements:
            if element.signalsBlocked():
                element.blockSignals(False)
            else:
                element.blockSignals(True)

    def resizeEvent(  # pylint: disable=invalid-name
        self, event: QResizeEvent
    ) -> None:
        """Handle resizing."""
        super().resizeEvent(event)
        self.on_center_rect()

    @pyqtSlot(QColor, name="on_color_change")
    def on_color_change(self, color: QColor) -> None:
        """Refresh controls on color change from color circle."""
        self._toggle_ui_signals()
        self._color = color
        self._ui.color_red_sb.setValue(color.red())
        self._ui.color_green_sb.setValue(color.green())
        self._ui.color_blue_sb.setValue(color.blue())
        self._ui.value_sb.setValue(color.value())
        self._ui.saturation_sb.setValue(color.saturation())
        self._ui.hue_sb.setValue(color.hue())
        self._rect.setBrush(QBrush(color))
        background_color: QColor = copy(self._color)
        background_color.setHsvF(
            self._color.hueF(),
            self._color.saturationF(),
            self._background_color_value,
        )
        self._view.setBackgroundBrush(background_color)
        self._toggle_ui_signals()

    @pyqtSlot(name="on_background_value_change")
    def on_background_value_change(self, value: float) -> None:
        """Refresh background according to slider position."""
        self._background_color_value = value
        self.on_color_change(self._color)

    @pyqtSlot(name="on_foreground_value_change")
    def on_foreground_value_change(self, value: float) -> None:
        """Refresh foreground according to slider position."""
        self._toggle_ui_signals()
        self._ui.value_sb.setValue(int(value * self._ui.value_sb.maximum()))
        self._ui.inner_value_slider.setValue(
            int(value * self._ui.inner_value_slider.maximum())
        )
        self._ui.color_circle.value = value
        self._toggle_ui_signals()

    @pyqtSlot(name="on_hue_change")
    def on_hue_change(self, value: float) -> None:
        """Refresh foreground according to hue value."""
        self._ui.color_circle.hue = value

    @pyqtSlot(name="on_reset_whitepoint")
    def on_reset_whitepoint(self) -> None:
        """Reset whitepoint."""
        self._ui.color_red_sb.setValue(255)
        self._ui.color_green_sb.setValue(255)
        self._ui.color_blue_sb.setValue(255)
        self._ui.value_sb.setValue(255)
        self._ui.inner_value_slider.setValue(511)

    @pyqtSlot(int, name="on_size_changed")
    def on_size_changed(self, length: int) -> None:
        """Resize rectangle from its center point."""
        old_width = self._rect.rect().width()
        old_heigth = self._rect.rect().height()
        self._rect.setRect(0, 0, length * 10, length * 10)
        self._rect.setPos(
            QPointF(
                self._rect.x()
                - (self._rect.rect().width() / 2 - old_width / 2),
                self._rect.y()
                - (self._rect.rect().height() / 2 - old_heigth / 2),
            )
        )
        self._view.update()

    @pyqtSlot(name="on_center_rect")
    def on_center_rect(self) -> None:
        """Center the rectangle."""
        self._rect.setPos(
            QPointF(
                (self._view.width() - self._rect.rect().width()) / 2,
                (self._view.height() - self._rect.rect().height()) / 2,
            )
        )
        self._view.update()

    @pyqtSlot(name="on_measurement")
    def on_measurement(self) -> None:
        """Not implemented measuring of color."""
        title = "Not implemented yet"
        text = "For the biggest part this is an interface showcase."
        QMessageBox.information(self, title, text)
