import sys
from ui_page_NaJia import Ui_Form
from ui_page_NaZi import Ui_NaZiForm
from ui_page_LingGui8 import Ui_Form_LingGui8
from PySide6.QtWidgets import QApplication, QWidget, QHeaderView
from PySide6.QtGui import QStandardItemModel, QStandardItem, QFont
from PySide6.QtCore import Qt, Slot
from infos import infos

header_style = "font: 700 14pt;"

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

        self.model = QStandardItemModel(3, 8)
        self.model.setVerticalHeaderLabels(['空间穴位', '元气底盘穴位', '靶向/经验穴位'])

        self.set_text_to_model(1, 0, '天枢')
        self.set_text_to_model(1, 1, '气海')
        self.set_text_to_model(1, 2, '关元')
        self.set_text_to_model(1, 3, '气穴')

        self.ui.tableView.setModel(self.model)
        self.ui.tableView.verticalHeader().setStyleSheet(header_style)
    
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
        self.ui.tableView.verticalHeader().setStyleSheet(header_style)

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

class LingGui8Page(BasePage):
    def __init__(self):
        super(LingGui8Page, self).__init__()
        self.ui = Ui_Form_LingGui8()
        self.ui.setupUi(self)

        self.model = QStandardItemModel(6, 3)
        self.model.setVerticalHeaderLabels(['', '  中轴', '', '', '  两翼', ''])
        self.model.setHorizontalHeaderLabels(['颈背', '头手', '胸腹下肢'])

        self.ui.tableView.setModel(self.model)
        self.ui.tableView.verticalHeader().setStyleSheet("font: 700 16pt;")
        self.ui.tableView.verticalHeader().setMinimumWidth(144) #100
        self.ui.tableView.horizontalHeader().setStyleSheet("font: 700 16pt;")


        self.model_2 = QStandardItemModel(1, 3)
        self.model_2.setVerticalHeaderLabels(['靶向/经验穴位'])

        self.ui.tableView_2.setModel(self.model_2)
        self.ui.tableView_2.verticalHeader().setStyleSheet("font: 700 16pt;")


    def update_model(self):
        pass

