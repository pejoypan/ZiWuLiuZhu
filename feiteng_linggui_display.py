from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QWidget, QApplication

from ui_feiteng_linggui_display import Ui_feiteng_linggui_display
from feiteng_display import FeiTengDisplay
from linggui_display import LingGuiDisplay


class FeiTengLingGuiDisplay(QWidget):
    def __init__(self, is_FT=False):

        super(FeiTengLingGuiDisplay, self).__init__()
        self.ui = Ui_feiteng_linggui_display()
        self.ui.setupUi(self)

        self.widget_1 = FeiTengDisplay(left_first=True) if is_FT else LingGuiDisplay(left_first=True)
        self.widget_2 = FeiTengDisplay(left_first=False) if is_FT else LingGuiDisplay(left_first=False)
        self.widget_3 = FeiTengDisplay(left_first=False) if is_FT else LingGuiDisplay(left_first=False)

        idx1 = self.ui.stackedWidget.addWidget(self.widget_1)
        self.ui.stackedWidget.setCurrentIndex(idx1)
        idx2 = self.ui.stackedWidget_2.addWidget(self.widget_2)
        self.ui.stackedWidget_2.setCurrentIndex(idx2)
        idx3 = self.ui.stackedWidget_3.addWidget(self.widget_3)
        self.ui.stackedWidget_3.setCurrentIndex(idx3)

    def set_from_table(self, table):

        self.widget_1.set_from_table(table, col_id=1)

        self.widget_2.set_from_table(table, col_id=2)

        self.widget_3.set_from_table(table, col_id=3)



import sys
if __name__ == "__main__":

    app = QApplication(sys.argv)

    test_widget = FeiTengLingGuiDisplay()

    test_widget.show()

    sys.exit(app.exec())