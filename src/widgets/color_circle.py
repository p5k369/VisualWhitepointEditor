"""
ColorCircle Widget.

(c) Patrick Zwerschke, 2022
updated to PyQt6 and refined

(c) Teigigutesiegel, 2021
used code from
https://gist.github.com/sjdv1982/75899d10e6983b878f63083e3c47b39b,
copyright (c) 2017 Sjoerd de Vries
"""

from PyQt6.QtCore import QLineF, QPointF, QRect, Qt, pyqtSignal
from PyQt6.QtGui import (
    QColor,
    QConicalGradient,
    QMouseEvent,
    QPainter,
    QPaintEvent,
    QRadialGradient,
    QResizeEvent,
)
from PyQt6.QtWidgets import QWidget


class ColorCircle(QWidget):
    """ColorCircle Widget."""

    MARGIN = 2

    color_changed = pyqtSignal(QColor)

    def __init__(self, parent: QWidget | None = None) -> None:
        """Initialize ColorCircle Widget."""
        super().__init__(parent)
        self._radius: float = 0
        self._color: QColor = QColor(255, 255, 255, 1)
        self._x: float = 0.5
        self._y: float = 0.5
        self._square: QRect

    def resizeEvent(  # pylint: disable=invalid-name
        self, _: QResizeEvent
    ) -> None:
        """Handle resizing of the color wheel."""
        size = min(self.width(), self.height()) - ColorCircle.MARGIN * 2
        self._radius = size / 2
        self._square = QRect(0, 0, size, size)
        self._square.moveCenter(self.rect().center())

    def paintEvent(  # pylint: disable=invalid-name
        self, _: QPaintEvent
    ) -> None:
        """Paint colorwheel and marker."""
        center = QPointF(self.width() / 2, self.height() / 2)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        painter.setViewport(
            ColorCircle.MARGIN,
            ColorCircle.MARGIN,
            self.width() - 2 * ColorCircle.MARGIN,
            self.height() - 2 * ColorCircle.MARGIN,
        )
        hsv_grad = QConicalGradient(center, 90)
        for deg in range(360):
            col = QColor.fromHsvF(deg / 360, 1, self._color.valueF())
            hsv_grad.setColorAt(deg / 360, col)

        val_grad = QRadialGradient(center, self._radius)
        val_grad.setColorAt(
            0.0, QColor.fromHsvF(0.0, 0.0, self._color.valueF(), 1.0)
        )
        val_grad.setColorAt(1.0, Qt.GlobalColor.transparent)

        painter.setPen(Qt.GlobalColor.transparent)
        painter.setBrush(hsv_grad)
        painter.drawEllipse(self._square)
        painter.setBrush(val_grad)
        painter.drawEllipse(self._square)

        painter.setPen(Qt.GlobalColor.black)
        painter.setBrush(self._color)
        line = QLineF.fromPolar(
            self._radius * self._color.saturationF(),
            360 * self._color.hueF() + 90,
        )
        line.translate(QPointF(self.rect().center()))
        painter.drawEllipse(line.p2(), 8, 8)

    def _recalc(self) -> None:
        """Repaint position of marker according to input color."""
        self.color_changed.emit(self._color)
        self.update()

    def _map_color(self, x_pos: int, y_pos: int) -> QColor:
        """Get color according to position of marker."""
        color = QColor()
        line = QLineF(QPointF(self.rect().center()), QPointF(x_pos, y_pos))
        saturation = min(1.0, line.length() / self._radius)
        hue = (line.angle() - 90) / 360 % 1.0
        color.setHsvF(hue, saturation, self._color.valueF())
        return color

    def _process_mouse_event(self, event: QMouseEvent) -> None:
        """Evaluate and process mouse events."""
        if event.button() == Qt.MouseButton.RightButton:
            self._color.setHsvF(0, 0, 1)
        else:
            self._color = self._map_color(event.pos().x(), event.pos().y())
        self._x = event.pos().x() / self.width()
        self._y = event.pos().y() / self.height()
        self._recalc()

    def mouseMoveEvent(  # pylint: disable=invalid-name
        self, event: QMouseEvent
    ) -> None:
        """Catch mouse move event and redirect to processing."""
        self._process_mouse_event(event)

    def mousePressEvent(  # pylint: disable=invalid-name
        self, event: QMouseEvent
    ) -> None:
        """Catch mouse press event and redirect to processing."""
        self._process_mouse_event(event)

    @property
    def color(self) -> QColor:
        """Return actual color."""
        return self._color

    @color.setter
    def color(self, color: QColor) -> None:
        """Set color accordingly."""
        self._color = color
        self._recalc()

    @property
    def red(self) -> float:
        """Return red int value."""
        return self._color.redF()

    @red.setter
    def red(self, value: float) -> None:
        """Set red int value."""
        if not (0 <= value <= 1):
            raise TypeError("Value must be between 0.0 and 1.0")
        self._color.setRedF(value)
        self._recalc()

    @property
    def green(self) -> float:
        """Return green int value."""
        return self._color.greenF()

    @green.setter
    def green(self, value: float) -> None:
        """Set green int value."""
        if not (0 <= value <= 1):
            raise TypeError("Value must be between 0.0 and 1.0")
        self._color.setGreenF(value)
        self._recalc()

    @property
    def blue(self) -> float:
        """Return blue int value."""
        return self._color.blueF()

    @blue.setter
    def blue(self, value: float) -> None:
        """Set blue int value."""
        if not (0 <= value <= 1):
            raise TypeError("Value must be between 0.0 and 1.0")
        self._color.setBlueF(value)
        self._recalc()

    @property
    def hue(self) -> float:
        """Return actual hue."""
        return self._color.hueF()

    @hue.setter
    def hue(self, hue: float) -> None:
        """Set hue accordingly."""
        if 0 <= hue <= 1:
            self._color.setHsvF(
                hue, self._color.saturationF(), self._color.valueF()
            )
            self._recalc()
        else:
            raise TypeError("Value must be between 0.0 and 1.0")

    @property
    def saturation(self) -> float:
        """Return actual saturation."""
        return self._color.saturationF()

    @saturation.setter
    def saturation(self, saturation: float) -> None:
        """Set saturation accordingly."""
        if 0 <= saturation <= 1:
            self._color.setHsvF(
                self._color.hueF(), saturation, self._color.valueF()
            )
            self._recalc()
        else:
            raise TypeError("Value must be between 0.0 and 1.0")

    @property
    def value(self) -> float:
        """Return actual value."""
        return self._color.valueF()

    @value.setter
    def value(self, value: float) -> None:
        """Set value accordingly."""
        if 0 <= value <= 1:
            self._color.setHsvF(
                self._color.hueF(), self._color.saturationF(), value
            )
            self._recalc()
        else:
            raise TypeError("Value must be between 0.0 and 1.0")
