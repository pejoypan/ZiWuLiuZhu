import sys
from ui_page_NaJia import Ui_Form
from PySide6.QtWidgets import QApplication, QWidget, QHeaderView
from PySide6.QtGui import QStandardItemModel, QStandardItem, QFont
from PySide6.QtCore import Qt



class NaJiaPage(QWidget):

    def __init__(self):
        super(NaJiaPage, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.model = QStandardItemModel(3, 6)
        self.model.setVerticalHeaderLabels(['空间穴位', '元气底盘穴位', '靶向/经验穴位'])

        self.set_text_to_model(1, 0, '天枢')
        self.set_text_to_model(1, 1, '气海')
        self.set_text_to_model(1, 2, '关元')
        self.set_text_to_model(1, 3, '气穴')

        self.ui.tableView.setModel(self.model)
        self.ui.tableView.verticalHeader().setStyleSheet("font: 700 16pt;")


    def set_text_to_model(self, row, col, text):
        item = QStandardItem(text)
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        self.model.setItem(row, col, item)
