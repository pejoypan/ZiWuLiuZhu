import unittest
from calculator import Calculator
from datetime import datetime

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_get_date_tian_gan(self):
        # 测试正常日期
        input_date = datetime(1969, 11, 26)
        expected_tian_gan = '乙'
        actual_tian_gan = self.calculator.get_date_tian_gan(input_date.date())
        self.assertEqual(actual_tian_gan, expected_tian_gan)

        # 测试其他日期
        input_date = datetime(2024, 10, 9)
        expected_tian_gan = '丙'
        actual_tian_gan = self.calculator.get_date_tian_gan(input_date.date())
        self.assertEqual(actual_tian_gan, expected_tian_gan)

    def test_get_date_di_zhi(self):
        # 测试正常情况
        input_date = datetime(1969, 11, 26)
        expected_di_zhi = '巳'
        actual_di_zhi = self.calculator.get_date_di_zhi(input_date.date())
        self.assertEqual(actual_di_zhi, expected_di_zhi)

        # 测试其他日期
        input_date = datetime(2024, 10, 9)
        expected_di_zhi = '午'
        actual_di_zhi = self.calculator.get_date_di_zhi(input_date.date())
        self.assertEqual(actual_di_zhi, expected_di_zhi)

    def test_get_hour_tian_gan(self):
        # 测试子时
        input_time = datetime(2024, 10, 8, 0)
        expected_tian_gan = '丙'
        actual_tian_gan = self.calculator.get_hour_tian_gan(input_time)
        self.assertEqual(actual_tian_gan, expected_tian_gan)

        # 测试丑时
        input_time = datetime(2024, 10, 8, 2)
        expected_tian_gan = '丁'
        actual_tian_gan = self.calculator.get_hour_tian_gan(input_time)
        self.assertEqual(actual_tian_gan, expected_tian_gan)

        # 测试寅时
        input_time = datetime(2024, 10, 8, 4)
        expected_tian_gan = '戊'
        actual_tian_gan = self.calculator.get_hour_tian_gan(input_time)
        self.assertEqual(actual_tian_gan, expected_tian_gan)

        # 测试卯时
        input_time = datetime(2024, 10, 8, 6)
        expected_tian_gan = '己'
        actual_tian_gan = self.calculator.get_hour_tian_gan(input_time)
        self.assertEqual(actual_tian_gan, expected_tian_gan)

        # 测试辰时
        input_time = datetime(2024, 10, 8, 8)
        expected_tian_gan = '庚'
        actual_tian_gan = self.calculator.get_hour_tian_gan(input_time)
        self.assertEqual(actual_tian_gan, expected_tian_gan)

        # 测试巳时
        input_time = datetime(2024, 10, 8, 10)
        expected_tian_gan = '辛'
        actual_tian_gan = self.calculator.get_hour_tian_gan(input_time)
        self.assertEqual(actual_tian_gan, expected_tian_gan)

        # 测试午时
        input_time = datetime(2024, 10, 8, 12)
        expected_tian_gan = '壬'
        actual_tian_gan = self.calculator.get_hour_tian_gan(input_time)
        self.assertEqual(actual_tian_gan, expected_tian_gan)

        # 测试未时
        input_time = datetime(2024, 10, 8, 14)
        expected_tian_gan = '癸'
        actual_tian_gan = self.calculator.get_hour_tian_gan(input_time)
        self.assertEqual(actual_tian_gan, expected_tian_gan)

        # 测试申时
        input_time = datetime(2024, 10, 8, 16)
        expected_tian_gan = '甲'
        actual_tian_gan = self.calculator.get_hour_tian_gan(input_time)
        self.assertEqual(actual_tian_gan, expected_tian_gan)

        # 测试酉时
        input_time = datetime(2024, 10, 8, 18)
        expected_tian_gan = '乙'
        actual_tian_gan = self.calculator.get_hour_tian_gan(input_time)
        self.assertEqual(actual_tian_gan, expected_tian_gan)

        # 测试戌时
        input_time = datetime(2024, 10, 8, 20)
        expected_tian_gan = '丙'
        actual_tian_gan = self.calculator.get_hour_tian_gan(input_time)
        self.assertEqual(actual_tian_gan, expected_tian_gan)

        # 测试亥时
        input_time = datetime(2024, 10, 8, 22)
        expected_tian_gan = '丁'
        actual_tian_gan = self.calculator.get_hour_tian_gan(input_time)
        self.assertEqual(actual_tian_gan, expected_tian_gan)

    def test_get_hour_di_zhi(self):
        # 测试凌晨 1 点
        time_1 = datetime(2023, 1, 1, 1)
        expected_1 = '丑'
        self.assertEqual(self.calculator.get_hour_di_zhi(time_1), expected_1)

        # 测试中午 12 点
        time_2 = datetime(2023, 1, 1, 12)
        expected_2 = '午'
        self.assertEqual(self.calculator.get_hour_di_zhi(time_2), expected_2)

        # 测试晚上 11 点
        time_3 = datetime(2023, 1, 1, 23)
        expected_3 = '子'
        self.assertEqual(self.calculator.get_hour_di_zhi(time_3), expected_3)
        
        time_4 = datetime(2024, 10, 8, 0)
        expected_4 = '子'
        self.assertEqual(self.calculator.get_hour_di_zhi(time_4), expected_4)

    def test_calc_LingGui8(self):
        # 测试各种输入组合
        day_gan = '癸'
        day_zhi = '卯'
        hour_gan = '壬'
        hour_zhi = '戌'
        expected_result = (2, '坤', '照海', '列缺')
        self.assertEqual(self.calculator.calc_LingGui8(day_gan, day_zhi, hour_gan, hour_zhi), expected_result)

        day_gan = '乙'
        day_zhi = '巳'
        hour_gan = '丙'
        hour_zhi = '戌'
        expected_result = (4, '巽', '足临泣', '外关')
        self.assertEqual(self.calculator.calc_LingGui8(day_gan, day_zhi, hour_gan, hour_zhi), expected_result)

    def test_get_gan_zhi_index(self):
        # 测试甲和子的索引
        self.assertEqual(self.calculator.get_gan_zhi_index('甲', '子'), 1)

        # 测试乙和丑的索引
        self.assertEqual(self.calculator.get_gan_zhi_index('乙', '丑'), 2)

        # 测试丙和寅的索引
        self.assertEqual(self.calculator.get_gan_zhi_index('丙', '寅'), 3)

        # 测试丁和卯的索引
        self.assertEqual(self.calculator.get_gan_zhi_index('丁', '卯'), 4)

        # 测试戊和辰的索引
        self.assertEqual(self.calculator.get_gan_zhi_index('戊', '辰'), 5)

        # 测试其他天干和地支的索引
        self.assertEqual(self.calculator.get_gan_zhi_index('癸', '酉'), 10)
        self.assertEqual(self.calculator.get_gan_zhi_index('丁', '亥'), 24)
        self.assertEqual(self.calculator.get_gan_zhi_index('甲', '午'), 31)
        self.assertEqual(self.calculator.get_gan_zhi_index('辛', '丑'), 38)
        self.assertEqual(self.calculator.get_gan_zhi_index('辛', '亥'), 48)
        self.assertEqual(self.calculator.get_gan_zhi_index('癸', '亥'), 60)

if __name__ == '__main__':
    unittest.main()
