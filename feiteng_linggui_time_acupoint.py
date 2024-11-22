from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from infos import infos, get_hexagram_str

from ui_feiteng_linggui_time_acupoint import Ui_feiteng_linggui_time_acupoint

class Feiteng_Linggui_Time_Acupoint(QWidget):
    def __init__(self, is_FT):
        super(Feiteng_Linggui_Time_Acupoint, self).__init__()
        self.ui = Ui_feiteng_linggui_time_acupoint()
        self.ui.setupUi(self)

        str_type = 'FeiTeng8' if is_FT else 'LingGui8'

        text1 = infos['output'][str_type]['ZhuXue']
        self.ui.text_1.setText(str(text1))

        text2 = infos['output'][str_type]['PeiXue']
        self.ui.text_2.setText(str(text2))

        title3 = '八卦卦位' if is_FT else '九宫位数'
        self.ui.title_3.setText(str(title3))

        text3 = infos['output'][str_type]['GuaWei'] if is_FT else infos['output'][str_type]['JiuGongShu']
        self.ui.text_3.setText(str(text3))

        hexagram = infos['output'][str_type]['Hexagram']

        text4 = get_hexagram_str(hexagram)
        self.ui.text_4.setText(str(text4))