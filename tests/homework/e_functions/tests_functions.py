#
import unittest
from src.homework.e_functions.value_return import get_hour
from src.homework.e_functions.value_return import get_minutes
from src.homework.e_functions.value_return import get_seconds


class Test_Config(unittest.TestCase):

    def test_get_hour(self):
        self.assertEqual(1, get_hour(3800))
        self.assertEqual(1, get_hour(3600))

    def test_get_minutes(self):
        self.assertEqual(3, get_minutes(3800))
        self.assertEqual(0, get_minutes(3600))

    def test_get_seconds(self):
        self.assertEqual(20, get_seconds(3800))
        self.assertEqual(0, get_seconds(3600))