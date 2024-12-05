from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtGui import QMovie
from PySide6.QtCore import Qt
from ui_loading import Ui_loading_widget

import icons_rc

class LoadingWidget(QWidget):
    def __init__(self):
        super(LoadingWidget, self).__init__()
        self.ui = Ui_loading_widget()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.movie = QMovie(":/icon/icons/Hourglass.gif") 
        self.ui.label.setMovie(self.movie)

        self.movie.start()

    def stop(self):
        self.movie.stop()
        self.hide()

import sys
if __name__ == "__main__":

    app = QApplication(sys.argv)

    test_widget = LoadingWidget()

    test_widget.show()

    sys.exit(app.exec())