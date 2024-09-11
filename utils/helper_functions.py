from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt, Signal


class ClickableLabel(QLabel):
    clicked = Signal()

    def __init__(self, text, default_style=None, hover_style=None):
        super().__init__(text)

        # Use provided styles or default ones
        self.default_stylesheet = default_style or "font-family: 'Cascadia Code SemiBold'; font-weight: bold; font-size: 12px; text-align: left;"
        self.hover_stylesheet = hover_style or "text-decoration: underline;"

        self.setStyleSheet(self.default_stylesheet)
        self.setAlignment(Qt.AlignmentFlag.AlignLeft)

    def enterEvent(self, event):
        self.setStyleSheet(self.default_stylesheet + self.hover_stylesheet)

    def leaveEvent(self, event):
        self.setStyleSheet(self.default_stylesheet)

    def mousePressEvent(self, event):
        self.clicked.emit()
        print(f"Clicked: {self.text()}")
