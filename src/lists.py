# Here are the prettified lists.
from PySide2.QtWidgets import QListWidget, QListWidgetItem
from PySide2.QtGui import QImage
from .buttons import *
from .resources.list_item import list_item


class StandardList(QListWidget):
    """This is the standard prettified list,
    without all the predefined useful buttons."""

    def __init__(self, parent=None, on_item_click=lambda: None,
                 on_item_double_click=lambda: None,
                 add_filter=lambda item: item):
        super().__init__(parent)
        self.setStyleSheet('''
        QListWidget {
            background-color: #f0f0f0
        }
        QListWidget::Item:hover {
            background-color: white;
        }
        QListWidget::Item {
            height: 2.5em;
        }
        QListWidget::Item::selected {
            background-color: rgb(230, 230, 230);
            color: black;
            border: none;
        }        
        ''')
        self.items = []
        self.on_click = on_item_click
        self.on_double_click = on_item_double_click
        self.itemClicked.connect(self.on_click)
        self.itemDoubleClicked.connect(self.on_double_click)
        self.filt = add_filter

    def addItem(self, label):
        label_text = label.text() if isinstance(label, QListWidgetItem) else label
        item = QListWidgetItem(self.filt(label_text))
        image = QImage()
        image.loadFromData(list_item)
        item.setIcon(QIcon(QPixmap(image)))
        self.items.append(label_text)
        super().addItem(item)

    def addItems(self, labels):
        for label in labels:
            self.addItem(label)

    def set_items(self, labels):
        self.clear()
        self.items.clear()
        for label in labels:
            self.addItem(label)


class SmartList(StandardList):
    """
    This List class provides some useful features to lists,
    such as deleting items and clearing lists, "floating"
    items up or down.
    Here are the available button types:
    darker     -> DarkerButton
    lighter    -> LighterButton
    "gradient light" -> GradientLightButton
    info     -> InfoButton
    success  -> SuccessButton
    """

    def __init__(self, parent=None, on_item_click=lambda: None,
                 on_item_double_click=lambda: None,
                 add_filter=lambda item: item):
        super().__init__(parent, on_item_click,
                         on_item_double_click, add_filter)
        self.has_del_btn = False
        self.has_clear_btn = False

    def set_all_buttons_disabled(self):
        if self.has_del_btn:
            self.btn_delete_item.setDisabled(True)
        if self.has_clear_btn:
            self.btn_clear.setDisabled(True)

    def add_delete_item_btn(self, text='delete current item',
                            btn_type: str = 'info', icon=None,
                            delete_callback=lambda: None) -> QPushButton:
        self.has_del_btn = True

        def on_delete_btn_click():
            row = self.currentIndex().row()
            selected = row != -1
            if selected:
                self.takeItem(row)
                del self.items[row]
                if len(self.items) == 0:
                    self.set_all_buttons_disabled()
                delete_callback()

        btn_type_name = btn_type.title().replace(' ', '') + 'Button'
        # example: 'darker' -> 'DarkerButton'
        self.btn_delete_item = eval(btn_type_name)(text, on_press=on_delete_btn_click,
                                                   parent=self, icon=icon)
        return self.btn_delete_item

    def add_clear_btn(self, text='clear all', btn_type: str = 'info', icon=None,
                      clear_callback=lambda: None):
        self.has_clear_btn = True

        def on_clear():
            self.items.clear()
            self.clear()
            self.set_all_buttons_disabled()
            clear_callback()
        btn_type_name = btn_type.title().replace(' ', '') + 'Button'
        self.btn_clear = eval(btn_type_name)(text, on_press=on_clear,
                                             parent=self, icon=icon)
        return self.btn_clear

    def add_btn_add(self, text: str = 'Add item', btn_type: str = 'info', icon=None,
                    on_add=lambda: None,):
        btn_type_name = btn_type.title().replace(' ', '') + 'Button'
        self.btn_add = eval(btn_type_name)(text, on_press=on_add,
                                           parent=self, icon=icon)
        return self.btn_add

    def add_btn_up(self, text='up', btn_type='info', icon=None):
        def up():
            current_index = self.currentIndex().row()
            selected = current_index != -1
            selected_first_item = current_index == 0
            if selected_first_item or not selected:
                return
            else:
                # switch the current item and the upper item
                self.items[current_index], \
                    self.items[current_index - 1] = (self.items[current_index - 1],
                                                     self.items[current_index])
                # reset(refresh) list
                self.set_items(self.items.copy())

        btn_type_name = btn_type.title().replace(' ', '') + 'Button'
        self.btn_up = eval(btn_type_name)(text, on_press=up,
                                          parent=self, icon=icon)
        return self.btn_up

    def add_btn_down(self, text='down', btn_type='info', icon=None):
        def down():
            current_index = self.currentIndex().row()
            print(current_index)
            selected = current_index != -1

            selected_last_item = \
                current_index == len(self.items) - 1

            if selected_last_item or not selected:
                return
            else:
                # switch the current item and the next item
                self.items[current_index], self.items[current_index + 1] = (self.items[current_index + 1],
                                                                            self.items[current_index])
                # reset(refresh) list
                self.set_items(self.items.copy())

        btn_type_name = btn_type.title().replace(' ', '') + 'Button'
        self.btn_down = eval(btn_type_name)(text, on_press=down,
                                            parent=self, icon=icon)

        return self.btn_down
