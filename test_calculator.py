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

if __name__ == '__main__':
    unittest.main()
