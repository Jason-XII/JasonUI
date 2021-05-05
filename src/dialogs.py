from PySide2.QtGui import QPixmap, QImage
from PySide2.QtWidgets import QMessageBox, QPushButton
from . import buttons
from .resources import information, question, warning
from .resources.error import err
import winsound


class Messages(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(buttons.DarkerButton.css)

    def send_information(self, title: str = 'Default title', text: str = 'Hi', btn: QPushButton = None):
        self.d = buttons.DarkerButton(parent=self.parent(), text='Ok') if btn is None else btn
        self.setWindowTitle(title)
        self.setText(text)
        image = QImage()
        image.loadFromData(information.information)
        self.setIconPixmap(QPixmap(image))
        self.addButton(self.d, QMessageBox.AcceptRole)
        winsound.PlaySound('*', winsound.SND_ASYNC)
        return self.exec_()

    def send_warning(self, title, text, btn=None):
        self.d = buttons.DarkerButton(parent=self.parent(), text='Ok') if btn is None else btn
        self.setWindowTitle(title)
        self.setText(text)
        image = QImage()
        image.loadFromData(warning.warning)
        self.setIconPixmap(QPixmap(image))
        self.addButton(self.d, QMessageBox.AcceptRole)
        winsound.PlaySound('SystemExclamation', winsound.SND_ASYNC)
        return self.exec_()

    def send_error(self, title, text, btn=None):
        self.d = buttons.DarkerButton(parent=self.parent(), text='Ok') if btn is None else btn
        self.setWindowTitle(title)
        self.setText(text)
        image = QImage()
        image.loadFromData(err)
        self.setIconPixmap(QPixmap(image))
        self.addButton(self.d, QMessageBox.AcceptRole)
        winsound.PlaySound('SystemHand', winsound.SND_ASYNC)
        return self.exec_()

    def send_question(self, title, text, btn_yes=None, btn_no=None, btn_cancel=None):
        """
        returns 0 when the user pressed the button on the left.
        returns 4 when the user pressed the button in the middle.
        returns 8 when the user pressed the button on the right.
        """
        self.yes = buttons.DarkerButton(parent=self.parent(), text='Yes') if btn_yes is None else btn_yes
        self.no = buttons.DarkerButton(parent=self.parent(), text='No') if btn_no is None else btn_no
        self.cancel = buttons.DarkerButton(parent=self.parent(),
                                           text='Cancel') if btn_cancel is None else btn_cancel
        self.setWindowTitle(title)
        self.setText(text)
        image = QImage()
        image.loadFromData(question.question)
        self.setIconPixmap(QPixmap(image))
        self.addButton(self.yes, QMessageBox.YesRole)
        self.addButton(self.no, QMessageBox.NoRole)
        self.addButton(self.cancel, QMessageBox.ApplyRole)
        winsound.PlaySound('SystemQuestion', winsound.SND_ASYNC)
        return self.exec_()