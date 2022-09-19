"""Test application."""
import sys

from PyQt6.QtWidgets import QApplication

from src.widgets.visual_whitepoint_editor import VisualWhitePointEditor

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VisualWhitePointEditor()
    window.show()
    sys.exit(app.exec())
