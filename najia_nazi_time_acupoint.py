from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from ui_najia_nazi_time_acupoint import Ui_Form

class Najia_Nazi_Time_Acupoint(QWidget):
    def __init__(self, title, acupoint):
        super(Najia_Nazi_Time_Acupoint, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.label.setText(title)
        self.ui.label_2.setText(acupoint)