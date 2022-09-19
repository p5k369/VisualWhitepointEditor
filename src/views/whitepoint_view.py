"""WhitepointView for rect drawing area."""
from PyQt6.QtWidgets import QGraphicsView, QWidget, QGraphicsScene


class WhitepointView(QGraphicsView):
    """View which holds the scene that shows the rect."""
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self.setScene(QGraphicsScene())
