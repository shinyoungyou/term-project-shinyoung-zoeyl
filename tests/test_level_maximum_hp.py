from unittest import TestCase
from event_option import level_maximum_hp


class Test(TestCase):

    def test_level_maximum_hp_user_level_is_1(self):
        result = level_maximum_hp(1)
        self.assertEqual(result, 40)

    def test_level_maximum_hp_user_level_is_2(self):
        result = level_maximum_hp(2)
        self.assertEqual(result, 65)

    def test_level_maximum_hp_user_level_is_3(self):
        result = level_maximum_hp(3)
        self.assertEqual(result, 100)
