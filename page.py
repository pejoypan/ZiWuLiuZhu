import sys

from ui_page_NaJia import Ui_Form
from ui_page_NaZi import Ui_NaZiForm
from ui_page import Ui_ItemForm

from ui_feiteng_linggui_display import Ui_feiteng_linggui_display
from najia_nazi_time_acupoint import Najia_Nazi_Time_Acupoint
from feiteng_linggui_display import FeiTengLingGuiDisplay

from output import OutputPage

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

        self.output_page = OutputPage()


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

    @Slot()
    def on_click(self):
        # self.output_page.set_space_display(display_widget)
        list_experience = self.get_experience()
        self.output_page.set_experience(list_experience)

        time_acupoint_widget = Najia_Nazi_Time_Acupoint(infos['acupoint_title'], infos['acupoint'])
        idx = self.output_page.ui.stackedWidget_time.addWidget(time_acupoint_widget)
        self.output_page.ui.stackedWidget_time.setCurrentIndex(idx)
        # self.output_page.ui.verticalLayout.replaceWidget(self.output_page.ui.widget, time_acupoint_widget)

        self.model.removeRow(2)
        idx = self.output_page.ui.stackedWidget.addWidget(self.ui.tableView)
        self.output_page.ui.stackedWidget.setCurrentIndex(idx)

        self.output_page.ui.pushButton_custom.setDisabled(True)
        self.output_page.show()
        self.output_page.set_from_infos()
        self.hide()

    def get_experience(self):
        row = self.model.rowCount() - 1

        row_data = []
        for col in range(self.model.columnCount()):
            item = self.model.item(row, col)
            if item is not None:
                row_data.append(item.text())
    
        return row_data


class ItemBasePage(QWidget):
    def __init__(self):
        super(ItemBasePage, self).__init__()

        self.mid_delegate = CompleterDelegate(words=['长强', '腰俞', '腰阳关', '命门', '筋缩', ',至阳', '灵台', '神道', '身柱', '陶道', '大椎', '风府', 
                                                     '后顶', '百会', '上星', '神庭', '人中', '关元', '气海', '阴交', '水分', '中脘', '膻中', '天突', 
                                                     '廉泉', '气穴', '气冲', '大杼', '然谷', '照海', '太冲', '公孙'])

        self.side_delegate = CompleterDelegate(words=['照海', '睛明', '肩髃', '臑俞', '地仓', '承泣', '居髎', '风池', '天突', '廉泉', '期门', '大横',
                                                      '筑宾', '肩井', '本神', '承灵', '头足', '临泣', '风府', '头维'])


        self.ui = Ui_ItemForm()
        self.ui.setupUi(self)

        # self.display_widget = DisplayWidget()
        self.output_page = OutputPage()

        # table
        self.ui.table.setRowCount(1)   # for common header setting
        self.ui.table.setColumnCount(4)
        self.ui.table.setColumnWidth(0, 160)

        # set horizontal header
        self.ui.table.setItem(0, 1, self.fake_header('颈背'))
        self.ui.table.setItem(0, 2, self.fake_header('头手'))
        self.ui.table.setItem(0, 3, self.fake_header('胸腹下肢'))

        self.ui.table.setRowHeight(0, 50)

        # TODO: delegate linggui / feiteng
        self.ui.table.setItemDelegateForRow(1, self.mid_delegate)
        self.ui.table.setItemDelegateForRow(2, self.mid_delegate)
        self.ui.table.setItemDelegateForRow(3, self.side_delegate)
        self.ui.table.setItemDelegateForRow(4, self.side_delegate)
        self.ui.table.setItemDelegateForRow(5, self.side_delegate)


        # table_2
        self.ui.table_2.setRowCount(3)
        self.ui.table_2.setColumnCount(4)
        # self.ui.table_2.setItemDelegate(self.delegate)

        # set vertical header
        self.ui.table_2.setItem(0, 0, self.fake_header('靶向/经验穴位'))
        self.ui.table_2.setSpan(0, 0, 3, 1)
        self.ui.table_2.setColumnWidth(0, 160)

        self.ui.pushButton.clicked.connect(self.on_click)



    def fake_header(self, text):
        item = QTableWidgetItem(text)
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        item.setFont(QFont("Microsoft YaHei UI", 16, QFont.Bold))
        item.setTextAlignment(Qt.AlignCenter)
        return item

    def get_experience(self):
        vec_point = []
        nrows = self.ui.table_2.rowCount()
        ncols = self.ui.table_2.columnCount()

        for row in range(nrows):
            for col in range(1, ncols):
                item = self.ui.table_2.item(row, col)
                if item is not None:
                    vec_point.append(item.text())
        return vec_point


    @Slot()
    def on_click(self):
        is_FT = infos['program'] == '飞腾八法'
        display_widget = FeiTengLingGuiDisplay(is_FT)
        display_widget.set_from_table(self.ui.table)
        self.output_page.set_space_display(display_widget)
        list_experience = self.get_experience()
        self.output_page.set_experience(list_experience)
        self.output_page.show()
        self.output_page.set_from_infos()
        self.hide()

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

        self.ui.next_btn.clicked.connect(self.on_click)
    
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

        self.ui.next_btn.clicked.connect(self.on_click)


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

        self.ui.table.setItemDelegateForRow(1, self.mid_delegate)
        self.ui.table.setItemDelegateForRow(2, self.mid_delegate)
        self.ui.table.setItemDelegateForRow(3, self.mid_delegate)
        self.ui.table.setItemDelegateForRow(4, self.side_delegate)
        self.ui.table.setItemDelegateForRow(5, self.side_delegate)
        self.ui.table.setItemDelegateForRow(6, self.side_delegate)

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

        self.ui.table.setItemDelegateForRow(1, self.mid_delegate)
        self.ui.table.setItemDelegateForRow(2, self.mid_delegate)
        self.ui.table.setItemDelegateForRow(3, self.side_delegate)
        self.ui.table.setItemDelegateForRow(4, self.side_delegate)
        self.ui.table.setItemDelegateForRow(5, self.side_delegate)

    def update_model(self):
        pass


# if __name__ == "__main__":

#     app = QApplication(sys.argv)

#     test_widget = SingleWidget()

#     test_widget.setStyleSheet("background-color: lightblue; border: 1px solid black;")
#     test_widget.setAutoFillBackground(True)
#     test_widget.show()

#     sys.exit(app.exec())