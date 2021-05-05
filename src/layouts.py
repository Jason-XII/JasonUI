from PySide2.QtWidgets import QHBoxLayout, QVBoxLayout, QLayout, QWidget


class Group:
    def __init__(self, *widgets):
        for widget in widgets:
            if isinstance(widget, int):
                self.addStretch(widget)
            elif isinstance(widget, QLayout):
                w = QWidget(parent)
                w.setLayout(widget)
                self.addWidget(w)
            else:
                self.addWidget(w)


class HorizontalGroup(QHBoxLayout, Group):
    def __init__(self, *widgets, parent=None):
        super().__init__(self, parent)
        super().__init__(self, *widgets)


class VerticalGroup(QVBoxLayout, Group):
    def __init__(self, *widgets, parent=None):
        super().__init__(self, parent)
        super().__init__(self, *widgets)
        
