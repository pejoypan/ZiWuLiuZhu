import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile, QDate, QTime, Signal, Slot
from ui_mainwindow import Ui_MainWindow
import yaml
import logging
from datetime import datetime
from calculator import Calculator

hexagram_map = {
    '乾': '\u2630',
    '兑': '\u2631',
    '离': '\u2632',
    '震': '\u2633',
    '巽': '\u2634',
    '坎': '\u2635',
    '艮': '\u2636',
    '坤': '\u2637',
}


infos = {
    'name': '~', 
    'date': {
        'year': 1900,
        'month': 1,
        'day': 1
        },
    'time': {
        'hour': 0,
        'minute': 0
        },
    'program': '~',
    'order': '~',
    'type': '~',
    'output': {
        'date_gan': '~',
        'date_zhi': '~',
        'date_idx': 0,
        'hour_gan': '~',
        'hour_zhi': '~',
        'hour_idx': 0,
        'LingGui8': {
            'JiuGongShu' : 0,
            'Hexagram': '~',
            'ZhuXue': '~',
            'PeiXue': '~'
            },
        'FeiTeng8': {
            'GuaWei' : 0,
            'Hexagram': '~',
            'ZhuXue': '~',
            'PeiXue': '~'
            },
        }
    }

current_date = QDate.currentDate()
current_time = QTime.currentTime()

class MainWindow(QMainWindow):

    input_edited = Signal(int)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.calculator = Calculator()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.dateEdit.setDate(current_date)
        self.ui.timeEdit.setTime(current_time)
        self.ui.verticalWidget_choose_acupoint.hide()
        infos['name'] = self.ui.lineEdit.text()
        infos['date']['year'] = self.ui.dateEdit.date().year()
        infos['date']['month'] = self.ui.dateEdit.date().month()
        infos['date']['day'] = self.ui.dateEdit.date().day()
        infos['time']['hour'] = self.ui.timeEdit.time().hour()
        infos['time']['minute'] = self.ui.timeEdit.time().minute()
        # infos['program'] 
        infos['order'] = self.ui.comboBox_order.currentText()
        infos['type'] = self.ui.comboBox_type.currentText()
        self.update_output()
        self.create_connect()
    
    def create_connect(self):
        self.ui.lineEdit.editingFinished.connect(self.on_input_name)
        self.ui.dateEdit.userDateChanged.connect(self.on_input_date)
        self.ui.timeEdit.userTimeChanged.connect(self.on_input_time)
        self.ui.radioButton_NaJia.clicked.connect(self.on_click_NaJia)
        self.ui.radioButton_NaZi.clicked.connect(self.on_click_NaZi)
        self.ui.radioButton_LingGui8.clicked.connect(self.on_click_LingGui8)
        self.ui.radioButton_FeiTeng8.clicked.connect(self.on_click_FeiTeng8)
        self.ui.radioButton_NaZi.clicked.connect(self.retranslate_NaZi)
        self.ui.radioButton_NaJia.clicked.connect(self.retranslate_NaJia)
        self.ui.radioButton_LingGui8.clicked.connect(self.retranslate_LingGui8)
        self.ui.radioButton_FeiTeng8.clicked.connect(self.retranslate_FeiTeng8)
        self.ui.comboBox_order.activated.connect(self.on_select_order)
        self.ui.comboBox_type.activated.connect(self.on_select_type)
        self.input_edited.connect(self.update_output)

        
    @Slot()
    def on_input_name(self):
        infos['name'] = self.ui.lineEdit.text()
        self.input_edited.emit(1)

    @Slot()
    def on_input_date(self):
        given_date = self.ui.dateEdit.date()
        infos['date']['year'] = given_date.year()
        infos['date']['month'] = given_date.month()
        infos['date']['day'] = given_date.day()
        self.input_edited.emit(1)

    @Slot()
    def on_input_time(self):
        given_time = self.ui.timeEdit.time()
        infos['time']['hour'] = given_time.hour()
        infos['time']['minute'] = given_time.minute()
        self.input_edited.emit(1)

    @Slot()
    def on_click_NaJia(self):
        infos['program'] = 'NaJia'
        self.input_edited.emit(1)

    @Slot()
    def on_click_NaZi(self):
        infos['program'] = 'NaZi'
        self.input_edited.emit(1)

    @Slot()
    def on_click_LingGui8(self):
        infos['program'] = 'LingGui8'
        self.input_edited.emit(1)

    @Slot()
    def on_click_FeiTeng8(self):
        infos['program'] = 'FeiTeng8'
        self.input_edited.emit(1)

    @Slot()
    def on_select_order(self):
        infos['order'] = self.ui.comboBox_order.currentText()
        self.input_edited.emit(1)

    @Slot()
    def on_select_type(self):
        infos['type'] = self.ui.comboBox_type.currentText()
        self.input_edited.emit(1)

    @Slot()
    def update_output(self):
        input_time = datetime(infos['date']['year'], infos['date']['month'], infos['date']['day'], infos['time']['hour'], infos['time']['minute'])
        date_gan, date_zhi, hour_gan, hour_zhi = self.calculator.get_gan_zhi(input_time)

        infos['output']['date_gan'] = date_gan
        infos['output']['date_zhi'] = date_zhi
        date_idx = self.calculator.get_gan_zhi_index(date_gan, date_zhi)
        infos['output']['date_idx'] = date_idx

        infos['output']['hour_gan'] = hour_gan
        infos['output']['hour_zhi'] = hour_zhi
        hour_idx = self.calculator.get_gan_zhi_index(hour_gan, hour_zhi)
        infos['output']['hour_idx'] = hour_idx

        self.update_LingGui8()
        self.update_FeiTeng8()

        if self.ui.radioButton_FeiTeng8.isChecked():
            self.retranslate_FeiTeng8()
        elif self.ui.radioButton_LingGui8.isChecked():
            self.retranslate_LingGui8()
        else:
            pass


        logger.info(infos)
        self.ui.label_date_gan_zhi.setText(f'{date_gan}{date_zhi}日 {date_idx}')
        self.ui.label_hour_gan_zhi.setText(f'{hour_gan}{hour_zhi}时 {hour_idx}')


    def update_LingGui8(self):
        jiu_gong_shu, hexagram, zhu_xue, pei_xue = self.calculator.calc_LingGui8(*self.gan_zhi_from_infos())

        infos['output']['LingGui8']['JiuGongShu'] = jiu_gong_shu
        infos['output']['LingGui8']['Hexagram'] = hexagram
        infos['output']['LingGui8']['ZhuXue'] = zhu_xue
        infos['output']['LingGui8']['PeiXue'] = pei_xue

    
    def update_FeiTeng8(self):
        hour_gan = infos['output']['hour_gan']

        gua_wei, hexagram, zhu_xue, pei_xue = self.calculator.calc_FeiTeng8(hour_gan)

        infos['output']['FeiTeng8']['GuaWei'] = gua_wei
        infos['output']['FeiTeng8']['Hexagram'] = hexagram
        infos['output']['FeiTeng8']['ZhuXue'] = zhu_xue
        infos['output']['FeiTeng8']['PeiXue'] = pei_xue


    @Slot()
    def retranslate_NaZi(self):
        self.ui.label_a.setText('\u88651')      # 补1
        self.ui.label_b.setText('\u88652')      # 补2
        self.ui.label_c.setText('\u88653')      # 补3
        self.ui.label_d.setText('\u6cc4\u7a74') # 泄穴
        self.ui.label_e.setText('\u672c\u7a74') # 本穴
        self.ui.label_f.setText('\u539f\u7a74') # 原穴

    @Slot()
    def retranslate_NaJia(self):
        self.ui.label_a.setText('\u4e3b\u7a74') # 主穴
        self.ui.label_b.setText('\u539f\u7a74') # 原穴
        self.ui.label_c.setText('\u4eca\u65e5\n\u4e92\u7528\u7a74') # 今日互用穴
        self.ui.label_d.setText('\u8865\u5145\n\u7a74\u4f4d')       # 补充穴位

    @Slot()
    def retranslate_LingGui8(self):
        self.ui.label_a.setText('\u4e5d\u5bab\u6570') # 九宫数
        self.ui.label_b.setText('\u5366') # 卦
        self.ui.label_c.setText('\u4e3b\u7a74') # 主穴
        self.ui.label_d.setText('\u914d\u7a74') # 配穴
        jiu_gong_shu = infos['output']['LingGui8']['JiuGongShu']
        hexagram = infos['output']['LingGui8']['Hexagram']
        zhu_xue = infos['output']['LingGui8']['ZhuXue']
        pei_xue = infos['output']['LingGui8']['PeiXue']
        self.ui.label_digit.setText(str(jiu_gong_shu))
        self.ui.label_hexgram.setText(f'{hexagram}{hexagram_map[hexagram]}')
        self.ui.label_ZhuXue.setText(zhu_xue)
        self.ui.label_PeiXue.setText(pei_xue)

    @Slot()
    def retranslate_FeiTeng8(self):
        self.ui.label_a.setText('\u5366\u4f4d') # 卦位
        self.ui.label_b.setText('\u5366') # 卦
        self.ui.label_c.setText('\u4e3b\u7a74') # 主穴
        self.ui.label_d.setText('\u914d\u7a74') # 配穴
        gua_wei = infos['output']['FeiTeng8']['GuaWei']
        hexagram = infos['output']['FeiTeng8']['Hexagram']
        zhu_xue = infos['output']['FeiTeng8']['ZhuXue']
        pei_xue = infos['output']['FeiTeng8']['PeiXue']
        self.ui.label_digit.setText(str(gua_wei))
        self.ui.label_hexgram.setText(f'{hexagram}{hexagram_map[hexagram]}')
        self.ui.label_ZhuXue.setText(zhu_xue)
        self.ui.label_PeiXue.setText(pei_xue)

    def gan_zhi_from_infos(self):
        return infos['output']['date_gan'], infos['output']['date_zhi'], infos['output']['hour_gan'], infos['output']['hour_zhi']

def initialize():
    pass

if __name__ == "__main__":
    log_file_name = f'{current_date.toPython()}-{current_time.hour()}{current_time.minute()}{current_time.second()}.log'
    logging.basicConfig(filename = log_file_name, filemode = 'w', level = logging.DEBUG)
    logger = logging.getLogger('@')
    logger.addHandler(logging.StreamHandler())

    app = QApplication(sys.argv)

    initialize()

    window = MainWindow()
    window.show()

    sys.exit(app.exec())