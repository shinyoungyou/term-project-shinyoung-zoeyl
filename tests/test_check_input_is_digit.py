import io
from unittest import TestCase
from unittest.mock import patch


from common import check_input_is_digit


class TestCheckInputIsDigit(TestCase):

    @patch('builtins.input', side_effect=['3'])
    def test_check_input_is_digit_input_is_digit(self, _):
        expected = 3
        actual = check_input_is_digit("Enter the number of potions to purchase: ")
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['abc', '3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_input_is_digit_input_is_not_digit_until_second_input(self, mock_output, _):
        expected = "Invalid input! Please enter a valid number: \n"
        check_input_is_digit("Enter the number of potions to purchase: ")
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=['abc', 'python', '3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_input_is_digit_input_is_not_digit_until_third_input(self, mock_output, _):
        expected = "Invalid input! Please enter a valid number: \n" * 2
        check_input_is_digit("Enter the number of potions to purchase: ")
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=['abc', 'python', 'java', 'c', '3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_input_is_digit_input_is_not_digit_until_fifth_input(self, mock_output, _):
        expected = "Invalid input! Please enter a valid number: \n" * 4
        check_input_is_digit("Enter the number of potions to purchase: ")
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=['abc', 'python', '', '3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_input_is_digit_inputs_include_empty_string(self, mock_output, _):
        expected = "Invalid input! Please enter a valid number: \n" * 3
        check_input_is_digit("Enter the number of potions to purchase: ")
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)