from PySide2.QtWidgets import QHBoxLayout, QVBoxLayout, QLayout, QWidget


class HorizontalGroup(QHBoxLayout):
    def __init__(self, *widgets, parent=None):
        super().__init__(self, parent)
        for widget in widgets:
            if isinstance(widget, int):
                self.addStretch(widget)
            elif isinstance(widget, QLayout):
                self.addLayout(widget)
            else:
                self.addWidget(widget)


class VerticalGroup(QVBoxLayout):
    def __init__(self, *widgets, parent=None):
        super().__init__(parent)
        for widget in widgets:
            if isinstance(widget, int):
                self.addStretch(widget)
            elif isinstance(widget, QLayout):
                self.addLayout(widget)
            else:
                self.addWidget(widget)
