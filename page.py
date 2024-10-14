import sys
from ui_page_NaJia import Ui_Form
from ui_page_NaZi import Ui_NaZiForm
from PySide6.QtWidgets import QApplication, QWidget, QHeaderView
from PySide6.QtGui import QStandardItemModel, QStandardItem, QFont
from PySide6.QtCore import Qt, Slot
from infos import infos


class BasePage(QWidget):
    def __init__(self):
        super(BasePage, self).__init__()

    def set_text_to_model(self, row, col, text):
        item = QStandardItem(text)
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        self.model.setItem(row, col, item)
    
    def set_texts_to_row(self, row, texts):
        self.clear_row(row)
        for col, text in enumerate(texts):
            self.set_text_to_model(row, col, text)

    def clear_row(self, row):
        col_count = self.model.columnCount()
        for col in range(col_count):
            self.model.setItem(row, col, QStandardItem(''))

class NaJiaPage(BasePage):

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
    
    def update_model(self):
        self.set_texts_to_row(0, infos['output']['NaJia']['SpatialXue'])



class NaZiPage(BasePage):
    def __init__(self):
        super(NaZiPage, self).__init__()
        self.ui = Ui_NaZiForm()
        self.ui.setupUi(self)

        self.model = QStandardItemModel(3, 12)
        self.model.setVerticalHeaderLabels(['空间穴位', '营气底盘穴位', '靶向/经验穴位'])

        self.ui.tableView.setModel(self.model)
        self.ui.tableView.verticalHeader().setStyleSheet("font: 700 16pt;")

        self.ui.radioButton.clicked.connect(self.on_click_small)
        self.ui.radioButton_2.clicked.connect(self.on_click_big)



    def update_model(self):
        if self.ui.radioButton.isChecked():
            self.set_texts_to_row(0, infos['output']['NaZi']['XiaoTongJing'])
        elif self.ui.radioButton_2.isChecked():
            self.set_texts_to_row(0, infos['output']['NaZi']['DaTongJing'])
        else:
            pass

        if infos['gender'] == '男':
            self.set_texts_to_row(1, ['申脉', '大椎', '天突', '中脘', '气海'])
        else:
            self.set_texts_to_row(1, ['照海', '大椎', '天突', '中脘', '气海'])

    @Slot()
    def on_click_small(self):
        # self.clear_row(0)
        self.set_texts_to_row(0, infos['output']['NaZi']['XiaoTongJing'])

    @Slot()
    def on_click_big(self):
        # self.clear_row(0)
        self.set_texts_to_row(0, infos['output']['NaZi']['DaTongJing'])