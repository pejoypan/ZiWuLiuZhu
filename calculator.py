import pandas as pd
import logging
from datetime import date

logger = logging.getLogger('CALC')
logger.addHandler(logging.StreamHandler())


class Calculator():
    def __init__(self):
        self.day_tian_gan_lut = {
            '甲': 10,
            '己': 10,
            '乙': 9,
            '庚': 9,
            '丁': 8,
            '壬': 8,
            '戊': 7,
            '癸': 7,
            '丙': 7,
            '辛': 7
        }

        self.day_di_zhi_lut = {
            '丑': 10,
            '辰': 10,
            '未': 10,
            '戌': 10,
            '申': 9,            
            '酉': 9,
            '寅': 8,           
            '卯': 8,
            '巳': 7,
            '午': 7,
            '子': 7,
            '亥': 7
        }

        self.hour_tian_gan_lut = {
            '甲': 9,
            '己': 9,
            '乙': 8,
            '庚': 8,
            '丙': 7,
            '辛': 7,
            '丁': 6,
            '壬': 6,
            '戊': 5,
            '癸': 5
        }

        self.hour_di_zhi_lut = {
            '子': 9,
            '午': 9,
            '丑': 8,
            '未': 8,
            '寅': 7,            
            '申': 7,
            '卯': 6,           
            '酉': 6,
            '辰': 5,
            '戌': 5,
            '巳': 4,
            '亥': 4
        }

        self.LingGui8_lut = {
            1: ['坎', '申脉', '后溪'],
            2: ['坤', '照海', '列缺'],
            3: ['震', '外关', '足临泣'],
            4: ['巽', '足临泣', '外关'],
            5: ['坤', '照海', '列缺'],
            6: ['乾', '公孙', '内关'],
            7: ['兑', '后溪', '申脉'],
            8: ['艮', '内关', '公孙'],
            9: ['离', '列缺', '照海']
        }

        self.FeiTeng8_lut = {
            '甲': [1, '乾', '公孙', '内关'],
            '乙': [8, '坤', '申脉', '后溪'],
            '丙': [7, '艮', '内关', '公孙'],
            '丁': [2, '兑', '照海', '列缺'],
            '戊': [6, '坎', '临泣', '外关'],
            '己': [3, '离', '列缺', '照海'],
            '庚': [4, '震', '外关', '临泣'],
            '辛': [5, '巽', '后溪', '申脉'],
            '壬': [1, '乾', '公孙', '内关'],
            '癸': [8, '坤', '申脉', '后溪']
        }

        self.gan_zhi_index_lut = [
            #甲 乙 丙  丁 戊  己 庚  辛 壬  癸 
            [1, 0, 13, 0, 25, 0, 37, 0, 49, 0], # 子
            [0, 2, 0, 14, 0, 26, 0, 38, 0, 50], # 丑
            [51, 0, 3, 0, 15, 0, 27, 0, 39, 0], # 寅
            [0, 52, 0, 4, 0, 16, 0, 28, 0, 40], # 卯
            [41, 0, 53, 0, 5, 0, 17, 0, 29, 0], # 辰
            [0, 42, 0, 54, 0, 6, 0, 18, 0, 30], # 巳
            [31, 0, 43, 0, 55, 0, 7, 0, 19, 0], # 午
            [0, 32, 0, 44, 0, 56, 0, 8, 0, 20], # 未
            [21, 0, 33, 0, 45, 0, 57, 0, 9, 0], # 申
            [0, 22, 0, 34, 0, 46, 0, 58, 0, 10], # 酉
            [11, 0, 23, 0, 35, 0, 47, 0, 59, 0], # 戌
            [0, 12, 0, 24, 0, 36, 0, 48, 0, 60] # 亥
        ]


        self.list_tian_gan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']

        self.list_di_zhi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

        self.base_date = date(1940, 9, 18) # 甲子日

        self.NaZi_lut = pd.read_csv('csv/NaZi.csv', encoding='UTF-8')
        logger.info(self.NaZi_lut)



    # 计算日天干
    def get_date_tian_gan(self, input_date):
        delta_days = (input_date - self.base_date).days
        stem_index = delta_days % 10
        
        return self.list_tian_gan[stem_index]

    # 计算日地支
    def get_date_di_zhi(self, input_date):
        delta_days = (input_date - self.base_date).days
        branch_index = delta_days % 12
        
        return self.list_di_zhi[branch_index]

    # 计算时天干
    def get_hour_tian_gan(self, input_time):       
        day_tian_gan = self.get_date_tian_gan(input_time.date())
        day_tian_gan_idx = self.list_tian_gan.index(day_tian_gan)

        hour = input_time.hour
        hour_idx = ((hour + 1) // 2) % 12

        gan_idx = (day_tian_gan_idx % 5 * 2 + hour_idx) % 10

        return self.list_tian_gan[gan_idx]
        
    # 计算时地支
    def get_hour_di_zhi(self, input_time):
        hour = input_time.hour

        hour_idx = ((hour + 1) // 2) % 12
        
        return self.list_di_zhi[hour_idx]

    def get_gan_zhi(self, input_time):
        date_gan = self.get_date_tian_gan(input_time.date())
        date_zhi = self.get_date_di_zhi(input_time.date())

        hour_gan = self.get_hour_tian_gan(input_time)
        hour_zhi = self.get_hour_di_zhi(input_time)

        return date_gan, date_zhi, hour_gan, hour_zhi
    
    def get_gan_zhi_index(self, gan, zhi):
        gan_idx = self.list_tian_gan.index(gan)
        zhi_idx = self.list_di_zhi.index(zhi)

        return self.gan_zhi_index_lut[zhi_idx][gan_idx]



    def calc_LingGui8(self, day_gan, day_zhi, hour_gan, hour_zhi):
        day_gan_value = self.day_tian_gan_lut[day_gan]
        day_zhi_value = self.day_di_zhi_lut[day_zhi]

        hour_gan_value = self.hour_tian_gan_lut[hour_gan]
        hour_zhi_value = self.hour_di_zhi_lut[hour_zhi]

        # calculate algebra sum
        total_value = day_gan_value + day_zhi_value + hour_gan_value + hour_zhi_value

        # calculate divisor
        day_gan_idx = self.list_tian_gan.index(day_gan)
        divisor = 9 if (day_gan_idx % 2) == 0 else 6

        jiu_gong_shu = total_value % divisor
        jiu_gong_shu = jiu_gong_shu if jiu_gong_shu != 0 else divisor


        return jiu_gong_shu, self.LingGui8_lut[jiu_gong_shu][0], self.LingGui8_lut[jiu_gong_shu][1], self.LingGui8_lut[jiu_gong_shu][2]
    
    def calc_FeiTeng8(self, hour_gan):

        return self.FeiTeng8_lut[hour_gan][0], self.FeiTeng8_lut[hour_gan][1], self.FeiTeng8_lut[hour_gan][2], self.FeiTeng8_lut[hour_gan][3]

    def calc_NaZi(self, hour_zhi):

        row = self.NaZi_lut[self.NaZi_lut.iloc[:, 0] == hour_zhi]

        return row.iloc[0, 1], row.iloc[0, 2], row.iloc[0, 3], row.iloc[0, 4], row.iloc[0, 5], row.iloc[0, 6]