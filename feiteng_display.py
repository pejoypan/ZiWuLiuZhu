from PySide6.QtWidgets import QWidget, QApplication

from ui_feiteng_single import Ui_FeiTeng_Single


class FeiTengDisplay(QWidget):
    def __init__(self, left_first=True):
        super(FeiTengDisplay, self).__init__()
        self.ui = Ui_FeiTeng_Single()
        self.ui.setupUi(self)

        if left_first:
            self.ui.label_tl.setText(u"\u5de6")
            self.ui.label_tr.setText(u"\u53f3")
        else:
            self.ui.label_tl.setText(u"\u53f3")
            self.ui.label_tr.setText(u"\u5de6")

    def set_from_table(self, table, col_id):
        if table.item(1, col_id) is not None:
            self.ui.label_1.setText(table.item(1, col_id).text())

        if table.item(2, col_id) is not None:
            self.ui.label_8.setText(table.item(2, col_id).text())

        if table.item(3, col_id) is not None:
            self.ui.label_2.setText(table.item(3, col_id).text())
            self.ui.label_5.setText(table.item(3, col_id).text())

        if table.item(4, col_id) is not None:
            self.ui.label_3.setText(table.item(4, col_id).text())
            self.ui.label_6.setText(table.item(4, col_id).text())

        if table.item(5, col_id) is not None:
            self.ui.label_4.setText(table.item(5, col_id).text())
            self.ui.label_7.setText(table.item(5, col_id).text())


# import sys

# # 创建应用程序实例
# app = QApplication(sys.argv)

# # 创建自定义背景的 QWidget 实例，传入资源路径
# widget = FeiTengDisplay()
# widget.show()

# sys.exit(app.exec())