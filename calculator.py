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

        self.list_tian_gan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']

        self.list_di_zhi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

        self.base_date = date(1940, 9, 18) # 甲子日

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