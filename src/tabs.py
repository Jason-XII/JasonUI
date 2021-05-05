from PySide2.QtWidgets import QTabWidget, QToolBox


class LightTab(QTabWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet('''
            QTabWidget::pane {
                border-top:1px solid black;
            }
             
            QTabBar {
                background-color:rgb(210, 210, 210);
                font-family: 微软雅黑;
            }
             
            QTabWidget QTabBar::tab {
                padding: 0.8em;
                border-width:0px;
                font-size:12px;
                border-top-left-radius: 0px;
                color:black;
            }
             
            QTabWidget QTabBar::tab::selected {
                color:black;
                background-color:white;
            }
             
            QTabWidget QTabBar::scroller {
                width:0px;
            } 
             
            QTabWidget QTabBar::tear {
                width: 0px; 
                border: none;
            }
            QTabWidget {
                margin: 30px;
            }
            ''')


class ToolBox(QToolBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet('''
            QToolBox {
                background-color:rgb(220, 225, 230);
                font-family: 微软雅黑;
            }

            QToolBox::tab {
                padding: 0.3em;
                border-width:0px;
                font-size:12px;
                border-top-left-radius: 0px;
                color:black;
            }

            QToolBox::tab::selected {
                color:black;
                background-color:white;
            }
            QToolBox {
                margin: 30px;
            }
            ''')
