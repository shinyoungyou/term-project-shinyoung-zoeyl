from unittest import TestCase
from event_option import choose_skill_to_challenge
from unittest.mock import patch
import io


class Test(TestCase):

    @patch('event_option.check_input_is_digit')
    def test_choose_skill_to_challenge_user_input_is_between_1_and_3(self, mock_check_input_is_digit):
        mock_check_input_is_digit.return_value = 2

        skill_collection = [{'name': 'Tackle', 'damage': (1, 3)}, {'name': 'Seed Bomb', 'damage': (4, 5)},
                            {'name': 'Solar Beam', 'damage': (6, 7)}]
        actual = choose_skill_to_challenge(skill_collection, 2)
        self.assertEqual(actual, {'name': 'Seed Bomb', 'damage': (4, 5)})

    @patch('event_option.check_input_is_digit')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_skill_to_challenge_user_input_is_not_between_1_and_3(self, mock_output, mock_check_input_is_digit):
        mock_check_input_is_digit.side_effect = [5, 3]

        skill_collection = [{'name': 'Tackle', 'damage': (1, 3)}, {'name': 'Seed Bomb', 'damage': (4, 5)},
                            {'name': 'Solar Beam', 'damage': (6, 7)}]
        choose_skill_to_challenge(skill_collection, 1)

        the_game_printed_this = mock_output.getvalue()
        expected = "5 is not a valid choice! Please choose a valid option between 1 and 3.\n"

        self.assertIn(expected, the_game_printed_this)
