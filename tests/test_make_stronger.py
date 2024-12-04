from unittest import TestCase
from event_option import make_stronger


class Test(TestCase):

    def test_make_stronger_user_level_is_1(self):
        actual = make_stronger(1)
        self.assertEqual(actual, 1)

    def test_make_stronger_user_level_is_2(self):
        actual = make_stronger(2)
        self.assertEqual(actual, 1.3)

    def test_make_stronger_user_level_is_3(self):
        actual = make_stronger(3)
        self.assertEqual(actual, 1.8)
