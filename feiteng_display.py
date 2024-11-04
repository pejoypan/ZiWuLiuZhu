from PySide6.QtCore import Qt, QRect
from PySide6.QtWidgets import QWidget, QApplication, QLabel
from PySide6.QtGui import QPixmap, QPainter, QFont

import icons_rc

class FeiTengDisplay(QWidget):
    def __init__(self, left_first=True):
        super(FeiTengDisplay, self).__init__()
        self.setFixedSize(202, 202)
        self.background = QPixmap(":icon/icons/feiteng_background.png")
        font = QFont()
        font.setPointSize(12)

        self.label_1 = QLabel(self)
        self.label_1.setFont(font)
        self.label_1.setGeometry(QRect(76, 10, 51, 31))
        self.label_1.setAlignment(Qt.AlignCenter)

        self.label_2 = QLabel(self)
        self.label_2.setFont(font)
        self.label_2.setGeometry(QRect(23, 37, 51, 31))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.label_3 = QLabel(self)
        self.label_3.setFont(font)
        self.label_3.setGeometry(QRect(10, 85, 51, 31))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.label_4 = QLabel(self)
        self.label_4.setFont(font)
        self.label_4.setGeometry(QRect(23, 135, 51, 31))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.label_5 = QLabel(self)
        self.label_5.setFont(font)
        self.label_5.setGeometry(QRect(130, 36, 51, 31))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.label_6 = QLabel(self)
        self.label_6.setFont(font)
        self.label_6.setGeometry(QRect(145, 85, 51, 31))
        self.label_6.setAlignment(Qt.AlignCenter)

        self.label_7 = QLabel(self)
        self.label_7.setFont(font)
        self.label_7.setGeometry(QRect(130, 135, 51, 31))
        self.label_7.setAlignment(Qt.AlignCenter)

        self.label_8 = QLabel(self)
        self.label_8.setFont(font)
        self.label_8.setGeometry(QRect(76, 163, 51, 31))
        self.label_8.setAlignment(Qt.AlignCenter)

        font1 = QFont()
        font1.setPointSize(14)

        self.label_tl = QLabel(self)
        self.label_tl.setFont(font1)
        # self.label_tl.setGeometry(QRect(0, 0, 31, 31))
        self.label_tl.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.label_tr = QLabel(self)
        self.label_tr.setFont(font1)
        self.label_tr.setGeometry(QRect(170, 0, 31, 31))
        self.label_tr.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)
        if left_first:
            self.label_tl.setText(u"\u5de6")
            self.label_tr.setText(u"\u53f3")
        else:
            self.label_tl.setText(u"\u53f3")
            self.label_tr.setText(u"\u5de6")


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.background)


# import sys

# # 创建应用程序实例
# app = QApplication(sys.argv)

# # 创建自定义背景的 QWidget 实例，传入资源路径
# widget = FeiTengDisplay()
# widget.show()

# sys.exit(app.exec())