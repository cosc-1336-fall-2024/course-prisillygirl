import unittest 
from src.homework.d_repetition.repetition import get_factorial_y, sum_odd_numbers_y
class Test_Config(unittest.TestCase):

    def test_for_range_loop(self):
        self.assertEqual(24, get_factorial_y(4))
        self.assertEqual(120, get_factorial_y(5))
        self.assertEqual(720, get_factorial_y(6))
    def test_while_loop(self):
        self.assertEqual(16, sum_odd_numbers_y(7))
        self.assertEqual(25, sum_odd_numbers_y(9))
        self.assertEqual(25, sum_odd_numbers_y(10))
        