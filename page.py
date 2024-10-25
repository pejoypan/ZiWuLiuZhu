import sys

from ui_page_NaJia import Ui_Form
from ui_page_NaZi import Ui_NaZiForm
from ui_page import Ui_ItemForm

from PySide6.QtWidgets import QApplication, QWidget, QHeaderView, QTableWidgetItem
from PySide6.QtGui import QStandardItemModel, QStandardItem, QFont, QColor
from PySide6.QtCore import Qt, Slot

from infos import infos
from completer import CompleterDelegate

header_style = "font: 700 14pt;"

class BasePage(QWidget):
    def __init__(self):
        super(BasePage, self).__init__()
        self.delegate = CompleterDelegate()

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

class ItemBasePage(QWidget):
    def __init__(self):
        super(ItemBasePage, self).__init__()
        self.delegate = CompleterDelegate()

        self.ui = Ui_ItemForm()
        self.ui.setupUi(self)

        # table
        self.ui.table.setRowCount(1)   # for common header setting
        self.ui.table.setColumnCount(4)
        self.ui.table.setColumnWidth(0, 160)
        self.ui.table.setItemDelegate(self.delegate)

        # set horizontal header
        self.ui.table.setItem(0, 1, self.fake_header('颈背'))
        self.ui.table.setItem(0, 2, self.fake_header('头手'))
        self.ui.table.setItem(0, 3, self.fake_header('胸腹下肢'))

        self.ui.table.setRowHeight(0, 50)

        # table_2
        self.ui.table_2.setRowCount(3)
        self.ui.table_2.setColumnCount(4)
        self.ui.table_2.setItemDelegate(self.delegate)

        # set vertical header
        self.ui.table_2.setItem(0, 0, self.fake_header('靶向/经验穴位'))
        self.ui.table_2.setSpan(0, 0, 3, 1)
        self.ui.table_2.setColumnWidth(0, 160)

    def fake_header(self, text):
        item = QTableWidgetItem(text)
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        item.setFont(QFont("Microsoft YaHei UI", 16, QFont.Bold))
        item.setTextAlignment(Qt.AlignCenter)
        return item

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

class LingGui8Page(ItemBasePage):
    def __init__(self):
        super(LingGui8Page, self).__init__()

        self.ui.label.setText('灵龟八法')

        self.ui.table.setRowCount(7)

        self.ui.table.setItem(1, 0, self.fake_header('中轴'))
        self.ui.table.setItem(4, 0, self.fake_header('两翼'))

        self.ui.table.setSpan(1, 0, 3, 1)
        self.ui.table.setSpan(4, 0, 3, 1)


    def update_model(self):
        pass

class FeiTengPage(ItemBasePage):
    def __init__(self):
        super(FeiTengPage, self).__init__()

        self.ui.label.setText('飞腾八法')

        self.ui.table.setRowCount(6)

        self.ui.table.setItem(1, 0, self.fake_header('中轴'))
        self.ui.table.setItem(3, 0, self.fake_header('两翼'))

        self.ui.table.setSpan(1, 0, 2, 1)
        self.ui.table.setSpan(3, 0, 3, 1)


    def update_model(self):
        pass