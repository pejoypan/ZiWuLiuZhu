from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QWidget, QApplication
from ui_feiteng_linggui_custom import Ui_feiteng_linggui_custom
from linggui_custom import LingGuiCustom
from feiteng_custom import FeiTengCustom


class FeiTengLingGuiCustom(QWidget):
    def __init__(self, is_FT=False):

        super(FeiTengLingGuiCustom, self).__init__()
        self.ui = Ui_feiteng_linggui_custom()
        self.ui.setupUi(self)

        self.widget_1 = FeiTengCustom() if is_FT else LingGuiCustom()
        self.widget_2 = FeiTengCustom() if is_FT else LingGuiCustom()
        self.widget_3 = FeiTengCustom() if is_FT else LingGuiCustom()

        self.ui.stackedWidget_1.removeWidget(self.ui.stackedWidget_1Page1)
        self.ui.stackedWidget_1.addWidget(self.widget_1)
        self.ui.stackedWidget_2.removeWidget(self.ui.stackedWidget_2Page1)
        self.ui.stackedWidget_2.addWidget(self.widget_2)
        self.ui.stackedWidget_3.removeWidget(self.ui.stackedWidget_3Page1)
        self.ui.stackedWidget_3.addWidget(self.widget_3)



import sys
if __name__ == "__main__":

    app = QApplication(sys.argv)

    test_widget = FeiTengLingGuiCustom()

    test_widget.show()

    sys.exit(app.exec())