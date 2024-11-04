from PySide6.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QMessageBox
from PySide6.QtGui import QPainter, QPageSize, QPixmap
from PySide6.QtPrintSupport import QPrinter
from PySide6.QtCore import Qt, Slot, QPoint
from ui_output import Ui_OutputPage
from infos import infos

class OutputPage(QWidget):
    def __init__(self):
        super(OutputPage, self).__init__()
        self.ui = Ui_OutputPage()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.export_to_img)


    def set_experience(self, vec_point):
        ncols = self.ui.tableWidget.columnCount()

        for i, pt in enumerate(vec_point):
            self.ui.tableWidget.setItem(i // ncols, i % ncols, QTableWidgetItem(str(pt)))

        # 设置表格为不可选中
        self.ui.tableWidget.setSelectionMode(QTableWidget.NoSelection)
        
        # 设置表格为不可编辑
        self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)

    

    def set_from_infos(self):
        self.ui.label_5.setText(infos['gender'])
        
        year = infos['date']['year']
        month = infos['date']['month']
        day = infos['date']['day']
        self.ui.label_7.setText(f'{year}年{month}月{day}日')

        date_gan = infos['output']['date_gan']
        date_zhi = infos['output']['date_zhi']
        self.ui.label_8.setText(f'{date_gan}{date_zhi}')

        self.ui.label_10.setText(str(infos['output']['date_idx']))

        hour_gan = infos['output']['hour_gan']
        hour_zhi = infos['output']['hour_zhi']
        self.ui.label_11.setText(f'{hour_gan}{hour_zhi}')

        self.ui.label_13.setText(str(infos['output']['hour_idx']))

        self.ui.label_15.setText(infos['order'])

        self.ui.label_18.setText(infos['type'])

    @Slot()
    def export_to_img(self):

        pixmap = QPixmap(self.size())
        # 使用 QPainter 将 QWidget 的内容绘制到 QPixmap
        self.ui.pushButton.hide()
        self.render(pixmap)
        self.ui.pushButton.show()

        customer_name = self.ui.lineEdit.text()

        year = infos['date']['year']
        month = infos['date']['month']
        day = infos['date']['day']
        
        file_name = f'{customer_name}_{year}-{month}-{day}'

        pixmap.save(f'{file_name}.png')
        QMessageBox.information(self, "导出成功", f'布穴图导出为:{file_name}.png', QMessageBox.Ok)
