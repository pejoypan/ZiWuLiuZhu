from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QWidget, QApplication, QTableWidgetItem, QTableWidget

from ui_najia_nazi_display import Ui_Form

class NajiaNaziDisplay(QWidget):
    def __init__(self, is_najia=True):
        super(NajiaNaziDisplay, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        if is_najia:
            self.ui.label_2.setText(u'元气底盘穴位：')
        else:
            self.ui.label_2.setText(u'营气底盘穴位：')

    def set_space_acupoint(self, vec_point):
        ncols = self.ui.tableWidget.columnCount()

        for i, pt in enumerate(vec_point):
            self.ui.tableWidget.setItem(i // ncols, i % ncols, QTableWidgetItem(str(pt)))

        # 设置表格为不可选中
        self.ui.tableWidget.setSelectionMode(QTableWidget.NoSelection)
        
        # 设置表格为不可编辑
        self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)

    def set_bottom_acupoint(self, vec_point):
        ncols = self.ui.tableWidget_2.columnCount()

        for i, pt in enumerate(vec_point):
            self.ui.tableWidget_2.setItem(i // ncols, i % ncols, QTableWidgetItem(str(pt)))

        # 设置表格为不可选中
        self.ui.tableWidget_2.setSelectionMode(QTableWidget.NoSelection)
        
        # 设置表格为不可编辑
        self.ui.tableWidget_2.setEditTriggers(QTableWidget.NoEditTriggers)
    


import sys
if __name__ == "__main__":

    app = QApplication(sys.argv)

    test_widget = NajiaNaziDisplay()

    test_widget.show()

    sys.exit(app.exec())