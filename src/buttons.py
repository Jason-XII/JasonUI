from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QPushButton


# Down here are the buttons.
# Info: If you want to change the font of the buttons, after you've edited the
#       font-family, you might need to change the padding by decreasing it.
#       Because if you don't, the button will be very big.
class MyStandardButton(QPushButton):
    def __init__(self, text='', on_press=lambda: None, parent=None, icon=None):
        super().__init__(text, parent)
        self.on_press = on_press
        self.clicked.connect(self.on_press)
        if icon is not None:
            self.setIcon(QIcon(QPixmap(icon)))


class DarkerButton(MyStandardButton):
    """darker when hovered, and even darker when pressed"""
    css = '''
            QPushButton {
                background-color: white;
                border: 0.1em solid rgb(200, 200, 200);
                border-radius: 5px;
                padding: 0.5em;
                font-family: 微软雅黑;

            }
            QPushButton:hover {
                background-color: rgb(235, 235, 235)
            }
            QPushButton:pressed {
                background-color: rgb(220, 220, 220);
            }'''

    def __init__(self, text='', on_press=lambda: None, parent=None, icon=None):
        super().__init__(text, on_press, parent, icon)
        self.setStyleSheet(self.css)


class LighterButton(MyStandardButton):
    """Lighter when hovered, darker when pressed"""
    css = '''
            QPushButton {
                background-color: rgb(254, 254, 254);
                border: 0.1em solid rgb(200, 200, 200);
                border-radius: 5px;
                padding: 0.5em;
                font-family: 微软雅黑;
            }
            QPushButton:hover {
                background-color: white;
                border-color: rgb(235, 235, 235);
            }
            QPushButton:pressed {
                background-color: rgb(220, 220, 220);
                border-color: rgb(200, 200, 200)
            }'''

    def __init__(self, text='', on_press=lambda: None, parent=None, icon=None):
        super().__init__(text, on_press, parent, icon)
        self.setStyleSheet(self.css)


class GradientLightButton(MyStandardButton):
    css = '''
            QPushButton {
                border: 0.1em solid rgb(200, 200, 200);
                border-radius: 5px;
                padding: 0.5em;
                font-family: 微软雅黑;
                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                        stop: 0 #FAFAFA, 
                                        stop: 1.0 #EAEAEA);
            }
            QPushButton:hover {
                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                        stop: 0 #FFFFFF, 
                                        stop: 1.0 #F0F0F0);
            }
            QPushButton:pressed {
                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                        stop: 0 rgb(240, 240, 240), 
                                        stop: 1.0 #E6E6E6);
                border-color: rgb(200, 200, 200)
            }
            '''

    def __init__(self, text='', on_press=lambda: None, parent=None, icon=None):
        super().__init__(text, on_press, parent, icon)
        self.setStyleSheet(self.css)


class InfoButton(MyStandardButton):
    def __init__(self, text='', on_press=lambda: None, parent=None, icon=None):
        super().__init__(text, on_press, parent, icon)
        self.setStyleSheet('''
        QPushButton {
            font-family: 微软雅黑, calibri, Arial;
            font-weight: bold;
            color: #000;
            background-color: #006699;
            border: 0.2em solid #3366cc;
            border-radius: 5px;
        }
        QPushButton:hover {
            color: #000;
            border-color: #006699;
        }
        QPushButton:pressed {
            color: #000;
            background-color: #336666;
            border-color: #336666;
        }
        ''')


class SuccessButton(MyStandardButton):
    def __init__(self, text='', on_press=lambda: None, parent=None, icon=None):
        super().__init__(text, on_press, parent, icon)
        self.setStyleSheet('''
        QPushButton {
            font-family: 微软雅黑, calibri, Arial;
            font-weight: bold;
            color: #000;
            background-color: #00cc33;
            border: 0.2em solid lightgreen;
            border-radius: 5px;
        }
        QPushButton:hover {
            color: #000;
            border-color: #00cc33;
        }
        QPushButton:pressed {
            color: #000;
            background-color: #009900;
            border-color: #009900;
        }
        ''')


class DangerButton(MyStandardButton):
    def __init__(self, text='', on_press=lambda: None, parent=None, icon=None):
        super().__init__(text, on_press, parent, icon)
        self.setStyleSheet('''
        QPushButton {
            font-family: 微软雅黑, calibri, Arial;
            font-weight: bold;
            color: #000;
            background-color: red;
            border: 0.2em solid #cc3300;
            border-radius: 5px;
        }
        QPushButton:hover {
            color: #000;
            border-color: red;
        }
        QPushButton:pressed {
            color: #000;
            background-color: #cc0000;
            border-color: #cc0000;
        }
        ''')