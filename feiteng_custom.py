from PySide6.QtCore import Qt, Slot

from PySide6.QtWidgets import QWidget, QApplication
from ui_feiteng_custom import Ui_FeiTeng_Custom

class FeiTengCustom(QWidget):
    def __init__(self):
        super(FeiTengCustom, self).__init__()
        self.ui = Ui_FeiTeng_Custom()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.on_swap)


    @Slot()
    def on_swap(self):
        text1 = self.ui.label.text()
        text2 = self.ui.label_2.text()

        self.ui.label.setText(text2)
        self.ui.label_2.setText(text1)


import sys
if __name__ == "__main__":

    app = QApplication(sys.argv)

    test_widget = FeiTengCustom()

    test_widget.show()

    sys.exit(app.exec())