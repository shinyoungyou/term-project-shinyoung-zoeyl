from unittest import TestCase
from unittest.mock import patch
from event_option import get_probability


class Test(TestCase):

    @patch('random.choices', return_value=[True])
    def test_get_probability_when_it_is_true(self, _):
        actual = get_probability()
        self.assertEqual(actual, True)

    @patch('random.choices', return_value=[False])
    def test_get_probability_when_it_is_false(self, _):
        actual = get_probability()
        self.assertEqual(actual, False)