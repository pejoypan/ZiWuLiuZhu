import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QButtonGroup
from PySide6.QtCore import QFile, QDate, QTime, Signal, Slot
from ui_mainwindow import Ui_MainWindow
import yaml
import logging
from datetime import datetime
from calculator import Calculator
from infos import infos
from page import NaJiaPage, NaZiPage, LingGui8Page

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



current_date = QDate.currentDate()
current_time = QTime.currentTime()

class MainWindow(QMainWindow):

    date_time_edited = Signal(int)
    gan_zhi_updated = Signal(int)
    acupoint_updated = Signal(int)

    def __init__(self):
        super(MainWindow, self).__init__()

        self.calculator = Calculator()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.najia_page = NaJiaPage()
        self.nazi_page = NaZiPage()
        self.linggui8_page = LingGui8Page()

        self.num_NaJia = 4

        self.ui.program_choices = QButtonGroup()
        self.build_button_group()

        self.ui.label_NaJia_.hide()
        self.ui.Slider_NaJia.hide()
        self.ui.Slider_NaZi.hide()

        self.ui.dateEdit.setDate(current_date)
        self.ui.timeEdit.setTime(current_time)

        # infos['name'] = self.ui.lineEdit.text()
        infos['gender'] = self.ui.comboBox_gender.currentText()

        infos['date']['year'] = self.ui.dateEdit.date().year()
        infos['date']['month'] = self.ui.dateEdit.date().month()
        infos['date']['day'] = self.ui.dateEdit.date().day()

        infos['time']['hour'] = self.ui.timeEdit.time().hour()
        infos['time']['minute'] = self.ui.timeEdit.time().minute()
        # infos['program'] 
        infos['order'] = self.ui.comboBox_order.currentText()
        infos['type'] = self.ui.comboBox_type.currentText()

        self.update_gan_zhi()
        self.update_all_acupoint()
        self.create_connect()
    
    def create_connect(self):
        # self.ui.lineEdit.editingFinished.connect(self.on_input_name)
        self.ui.comboBox_gender.activated.connect(self.on_select_gender)
        self.ui.dateEdit.userDateChanged.connect(self.on_input_date)
        self.ui.timeEdit.userTimeChanged.connect(self.on_input_time)

        self.ui.comboBox_order.activated.connect(self.on_select_order)
        self.ui.comboBox_type.activated.connect(self.on_select_type)

        self.date_time_edited.connect(self.update_gan_zhi)
        self.gan_zhi_updated.connect(self.update_all_acupoint)
        self.acupoint_updated.connect(self.update_acupoint)

        self.ui.program_choices.buttonClicked.connect(self.on_select_program)
        self.ui.program_choices.buttonClicked.connect(self.update_acupoint)

        self.ui.Slider_NaJia.valueChanged.connect(self.on_move_slider_NaJia)
        self.ui.Slider_NaZi.valueChanged.connect(self.on_move_slider_NaZi)

        self.ui.pushButton.clicked.connect(self.on_generate)


    def build_button_group(self):
        self.ui.program_choices.addButton(self.ui.radioButton_NaJia)
        self.ui.program_choices.addButton(self.ui.radioButton_NaZi)
        self.ui.program_choices.addButton(self.ui.radioButton_LingGui8)
        self.ui.program_choices.addButton(self.ui.radioButton_FeiTeng8)

    @Slot()
    def on_generate(self):
        logger.info(infos)
        if infos['program'] == '纳甲法':
            self.najia_page.update_model()
            self.najia_page.show()
        elif infos['program'] == '纳子法':
            self.nazi_page.update_model()
            self.nazi_page.show()
        elif infos['program'] == '灵龟八法':
            self.linggui8_page.update_model()
            self.linggui8_page.show()
        else:
            pass

        
    # @Slot()
    # def on_input_name(self):
    #     infos['name'] = self.ui.lineEdit.text()
    
    @Slot()
    def on_select_gender(self):
        infos['gender'] = self.ui.comboBox_gender.currentText()

    @Slot()
    def on_input_date(self):
        given_date = self.ui.dateEdit.date()
        infos['date']['year'] = given_date.year()
        infos['date']['month'] = given_date.month()
        infos['date']['day'] = given_date.day()
        self.date_time_edited.emit(1)

    @Slot()
    def on_input_time(self):
        given_time = self.ui.timeEdit.time()
        infos['time']['hour'] = given_time.hour()
        infos['time']['minute'] = given_time.minute()
        self.date_time_edited.emit(1)


    @Slot()
    def on_select_program(self):
        infos['program'] = self.ui.program_choices.checkedButton().text()

    @Slot()
    def on_select_order(self):
        infos['order'] = self.ui.comboBox_order.currentText()

    @Slot()
    def on_select_type(self):
        infos['type'] = self.ui.comboBox_type.currentText()

    @Slot(int)
    def on_move_slider_NaJia(self, value):
        if 0 <= value < 25:
            infos['acupoint'] = self.ui.label_NaJia1.text()
            self.remove_label_highlight()
            self.ui.label_NaJia1.setStyleSheet("color: red;")
        elif 25 <= value < 50:
            if self.num_NaJia == 4:
                infos['acupoint'] = self.ui.label_NaJia2.text()
                self.remove_label_highlight()
                self.ui.label_NaJia2.setStyleSheet("color: red;")
            elif self.num_NaJia == 5:
                if value < 38:
                    infos['acupoint'] = self.ui.label_NaJia2.text()
                    self.remove_label_highlight()
                    self.ui.label_NaJia2.setStyleSheet("color: red;")
                else:
                    infos['acupoint'] = self.ui.label_NaJia_.text()
                    self.remove_label_highlight()
                    self.ui.label_NaJia_.setStyleSheet("color: red;")
            else:
                pass
        elif 50 <= value < 75:
            infos['acupoint'] = self.ui.label_NaJia3.text()
            self.remove_label_highlight()
            self.ui.label_NaJia3.setStyleSheet("color: red;")
        elif 75 <= value <= 100:
            infos['acupoint'] = self.ui.label_NaJia4.text()
            self.remove_label_highlight()
            self.ui.label_NaJia4.setStyleSheet("color: red;")
        else:
            pass

    @Slot(int)
    def on_move_slider_NaZi(self, value):
        if 0 <= value < 17:
            infos['acupoint'] = self.ui.label_NaZi1.text()
            self.remove_label_highlight()
            self.ui.label_NaZi1.setStyleSheet("color: red;")
        elif 17 <= value < 33:
            infos['acupoint'] = self.ui.label_NaZi2.text()
            self.remove_label_highlight()
            self.ui.label_NaZi2.setStyleSheet("color: red;")
        elif 33 <= value < 50:
            infos['acupoint'] = self.ui.label_NaZi3.text()
            self.remove_label_highlight()
            self.ui.label_NaZi3.setStyleSheet("color: red;")
        elif 50 <= value <= 67:
            infos['acupoint'] = self.ui.label_NaZi4.text()
            self.remove_label_highlight()
            self.ui.label_NaZi4.setStyleSheet("color: red;")
        elif 67 <= value < 83:
            infos['acupoint'] = self.ui.label_NaZi5.text()
            self.remove_label_highlight()
            self.ui.label_NaZi5.setStyleSheet("color: red;")
        elif 83 <= value <= 100:
            infos['acupoint'] = self.ui.label_NaZi6.text()
            self.remove_label_highlight()
            self.ui.label_NaZi6.setStyleSheet("color: red;")
        else:
            pass

    def remove_label_highlight(self):
        self.ui.label_NaJia1.setStyleSheet("")
        self.ui.label_NaJia2.setStyleSheet("")
        self.ui.label_NaJia3.setStyleSheet("")
        self.ui.label_NaJia4.setStyleSheet("")
        self.ui.label_NaJia_.setStyleSheet("")
        self.ui.label_NaZi1.setStyleSheet("")
        self.ui.label_NaZi2.setStyleSheet("")
        self.ui.label_NaZi3.setStyleSheet("")
        self.ui.label_NaZi4.setStyleSheet("")
        self.ui.label_NaZi5.setStyleSheet("")
        self.ui.label_NaZi6.setStyleSheet("")


    @Slot()
    def update_gan_zhi(self):
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

        self.ui.label_date_gan_zhi.setText(f'{date_gan}{date_zhi}日 {date_idx}')
        self.ui.label_hour_gan_zhi.setText(f'{hour_gan}{hour_zhi}时 {hour_idx}')

        self.gan_zhi_updated.emit(1)

    @Slot()
    def update_all_acupoint(self):
        self.calc_acupoint()
        self.retranslate_acupoint()
        self.acupoint_updated.emit(1)


    def calc_acupoint(self):
        self.update_FeiTeng8()
        self.update_LingGui8()
        self.update_NaJia()
        self.update_NaZi()

    def retranslate_acupoint(self):
        self.retranslate_NaJia()
        self.retranslate_NaZi()
        self.retranslate_LingGui8()
        self.retranslate_FeiTeng8()
    
    @Slot()
    def update_acupoint(self):
        self.remove_label_highlight()
        if self.ui.radioButton_NaJia.isChecked():
            self.on_move_slider_NaJia(self.ui.Slider_NaJia.value())
        elif self.ui.radioButton_NaZi.isChecked():
            self.on_move_slider_NaZi(self.ui.Slider_NaZi.value())
        elif self.ui.radioButton_LingGui8.isChecked():
            infos['acupoint'] = self.ui.label_LingGui3.text()
        elif self.ui.radioButton_FeiTeng8.isChecked():
            infos['acupoint'] = self.ui.label_FeiTeng3.text()
        else:
            pass



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

    def update_NaZi(self):
        hour_zhi = infos['output']['hour_zhi']

        bu1, bu2, bu3, xie_xue, ben_xue, yuan_xue, xiao_tong, da_tong = self.calculator.calc_NaZi(hour_zhi)

        infos['output']['NaZi']['Bu1'] = bu1
        infos['output']['NaZi']['Bu2'] = bu2
        infos['output']['NaZi']['Bu3'] = bu3
        infos['output']['NaZi']['XieXue'] = xie_xue
        infos['output']['NaZi']['BenXue'] = ben_xue
        infos['output']['NaZi']['YuanXue'] = yuan_xue

        xiao_tong_list = xiao_tong.split('|')
        infos['output']['NaZi']['XiaoTongJing'] = xiao_tong_list

        da_tong_list = da_tong.split('|')
        infos['output']['NaZi']['DaTongJing'] = da_tong_list


    def update_NaJia(self):
        zhu_xue, yuan_xue, hu_yong_xue, bu_chong_xue, kong_jian_xue = self.calculator.calc_NaJia(*self.gan_zhi_from_infos())

        if '|' in yuan_xue:
            yuan_xue = yuan_xue.split('|')

        infos['output']['NaJia']['ZhuXue'] = zhu_xue
        infos['output']['NaJia']['YuanXue'] = yuan_xue
        infos['output']['NaJia']['TodayHuYongXue'] = hu_yong_xue
        infos['output']['NaJia']['AdditionalXue'] = bu_chong_xue

        kong_jian_list = kong_jian_xue.split('|')
        infos['output']['NaJia']['SpatialXue'] = kong_jian_list


    def retranslate_NaZi(self):
        self.ui.label_NaZi1.setText(infos['output']['NaZi']['Bu1'])
        self.ui.label_NaZi2.setText(infos['output']['NaZi']['Bu2'])
        self.ui.label_NaZi3.setText(infos['output']['NaZi']['Bu3'])
        self.ui.label_NaZi4.setText(infos['output']['NaZi']['XieXue'])
        self.ui.label_NaZi5.setText(infos['output']['NaZi']['BenXue'])
        self.ui.label_NaZi6.setText(infos['output']['NaZi']['YuanXue'])

    def retranslate_NaJia(self):
        self.ui.label_NaJia1.setText(infos['output']['NaJia']['ZhuXue'])
        if (isinstance(infos['output']['NaJia']['YuanXue'], str)):
            self.ui.label_NaJia_.hide()
            self.num_NaJia = 4
            self.ui.label_NaJia2.setText(infos['output']['NaJia']['YuanXue'])
        elif (isinstance(infos['output']['NaJia']['YuanXue'], list)):
            self.ui.label_NaJia_.show()
            self.num_NaJia = 5
            self.ui.label_NaJia2.setText(infos['output']['NaJia']['YuanXue'][0])
            self.ui.label_NaJia_.setText(infos['output']['NaJia']['YuanXue'][1])

        # self.ui.label_NaJia2.setText(infos['output']['NaJia']['YuanXue'])
        self.ui.label_NaJia3.setText(infos['output']['NaJia']['TodayHuYongXue'])
        self.ui.label_NaJia4.setText(infos['output']['NaJia']['AdditionalXue'])

    def retranslate_LingGui8(self):
        jiu_gong_shu = infos['output']['LingGui8']['JiuGongShu']
        self.ui.label_LingGui1.setText(str(jiu_gong_shu))

        hexagram = infos['output']['LingGui8']['Hexagram']
        str_hexagram = f'{hexagram}{hexagram_map[hexagram]}' if hexagram in hexagram_map else hexagram
        self.ui.label_LingGui2.setText(str_hexagram)

        self.ui.label_LingGui3.setText(infos['output']['LingGui8']['ZhuXue'])
        self.ui.label_LingGui4.setText(infos['output']['LingGui8']['PeiXue'])

    def retranslate_FeiTeng8(self):
        gua_wei = infos['output']['FeiTeng8']['GuaWei']
        self.ui.label_FeiTeng1.setText(str(gua_wei))

        hexagram = infos['output']['FeiTeng8']['Hexagram']
        str_hexagram = f'{hexagram}{hexagram_map[hexagram]}' if hexagram in hexagram_map else hexagram
        self.ui.label_FeiTeng2.setText(str_hexagram)

        self.ui.label_FeiTeng3.setText(infos['output']['FeiTeng8']['ZhuXue'])
        self.ui.label_FeiTeng4.setText(infos['output']['FeiTeng8']['PeiXue'])

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