from PySide2.QtWidgets import QSpinBox


class SpinBox(QSpinBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet('''QSpinBox {
                        font-family: Microsoft YaHei;
                           }''')
