"""Colored rectangle."""
from PyQt6.QtGui import QPainter
from PyQt6.QtWidgets import (
    QGraphicsRectItem,
    QStyle,
    QStyleOptionGraphicsItem,
    QWidget,
)


class ColorRect(QGraphicsRectItem):  # pylint: disable=too-few-public-methods
    """Rectangle with solid outline."""

    def paint(
        self,
        painter: QPainter,
        option: QStyleOptionGraphicsItem,
        _: QWidget | None = None,
    ) -> None:
        """Paint the rectangle."""
        option.state = QStyle.StateFlag.State_Active
        return super().paint(painter, option)
