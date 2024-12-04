from unittest import TestCase
from prepare_event import select_event_option
from unittest.mock import patch
import io


class Test(TestCase):

    @patch('prepare_event.customize_user_options')
    @patch('prepare_event.check_input_is_digit')
    def test_select_event_option_option_number_is_3(self, mock_check_input_is_digit, mock_customize_user_options):
        mock_customize_user_options.return_value = ["Fight", "Change Pokemon", "Run Away"]
        mock_check_input_is_digit.return_value = 2

        result = select_event_option("Gym Leader", 3)

        self.assertEqual(result, "Change Pokemon")

    @patch('prepare_event.customize_user_options')
    @patch('prepare_event.check_input_is_digit')
    def test_select_event_option_option_number_is_2(self, mock_check_input_is_digit, mock_customize_user_options):
        mock_customize_user_options.return_value = ["Fight", "Change Pokemon"]
        mock_check_input_is_digit.return_value = 1

        result = select_event_option("Gym Leader", 2)

        self.assertEqual(result, "Fight")

    @patch('prepare_event.customize_user_options')
    @patch('prepare_event.check_input_is_digit')
    def test_select_event_option_option_number_is_5(self, mock_check_input_is_digit, mock_customize_user_options):
        mock_customize_user_options.return_value = ["Fight", "Change Pokemon", "Use Potion", "Throw Poke Ball",
                                                    "Run Away"]
        mock_check_input_is_digit.return_value = 4

        result = select_event_option("wildPokemon")

        self.assertEqual(result, "Throw Poke Ball")

    @patch('prepare_event.customize_user_options')
    @patch('prepare_event.check_input_is_digit')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_event_option_user_choice_is_invalid(self, mock_output, mock_check_input_is_digit,
                                                        mock_customize_user_options):
        mock_customize_user_options.return_value = ["Fight", "Change Pokemon", "Use Potion", "Throw Poke Ball",
                                                    "Run Away"]
        mock_check_input_is_digit.side_effect = [7, 3]

        select_event_option("wildPokemon")

        the_game_printed_this = mock_output.getvalue()
        expected = '\nInvalid choice! Please enter a number between 1 and 5.\n'

        self.assertIn(expected, the_game_printed_this)

    @patch('prepare_event.customize_user_options')
    @patch('prepare_event.check_input_is_digit')
    def test_select_event_option_user_choice_is_valid(self, mock_check_input_is_digit, mock_customize_user_options):
        mock_customize_user_options.return_value = ["Fight", "Change Pokemon", "Use Potion"]
        mock_check_input_is_digit.return_value = 1

        result = select_event_option("Team Rocket")

        self.assertEqual(result, "Fight")