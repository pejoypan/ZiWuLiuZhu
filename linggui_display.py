from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QApplication, QLabel
from ui_linggui_single import Ui_LingGui_Single

class LingGuiDisplay(QWidget):
    def __init__(self, left_first=True):
        super(LingGuiDisplay, self).__init__()
        self.ui = Ui_LingGui_Single()
        self.ui.setupUi(self)

        if not left_first:
            self.ui.label.setText(u"\u53f3")
            self.ui.label_2.setText(u"\u5de6")

    def set_from_table(self, table, col_id):
        if table.item(1, col_id) is not None:
            self.ui.label9.setText(table.item(1, col_id).text())

        if table.item(2, col_id) is not None:
            self.ui.label5.setText(table.item(2, col_id).text())

        if table.item(3, col_id) is not None:
            self.ui.label1.setText(table.item(3, col_id).text())

        if table.item(4, col_id) is not None:
            self.ui.label4.setText(table.item(4, col_id).text())
            self.ui.label2.setText(table.item(4, col_id).text())

        if table.item(5, col_id) is not None:
            self.ui.label3.setText(table.item(5, col_id).text())
            self.ui.label7.setText(table.item(5, col_id).text())

        if table.item(6, col_id) is not None:
            self.ui.label8.setText(table.item(6, col_id).text())
            self.ui.label6.setText(table.item(6, col_id).text())