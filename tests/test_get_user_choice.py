from unittest import TestCase
from unittest.mock import patch
from game import get_user_choice
import io


class Test(TestCase):

    @patch('game.check_input_is_digit')
    def test_get_user_choice_user_choice_is_between_1_and_4(self, mock_check_input_is_digit):
        mock_check_input_is_digit.return_value = 1

        character = {'Current Location': (0, 0), 'Poke Ball': {'Squirtle': {'type': 'water', 'currentHP': 40}},
                     'Money': 30, 'Potion': 2}
        board = {(0, 0): True, (0, 1): True, (0, 2): True, (0, 3): True, (0, 4): True, (0, 5): False,
                (1, 0): False, (1, 1): True, (1, 2): True, (1, 3): True, (1, 4): True, (1, 5): False,
                (2, 0): False, (2, 1): True, (2, 2): 'Store', (2, 3): True, (2, 4): True, (2, 5): False,
                (3, 0): False, (3, 1): True, (3, 2): True, (3, 3): True, (3, 4): True, (3, 5): False,
                (4, 0): False, (4, 1): True, (4, 2): True, (4, 3): True, (4, 4): True, (4, 5): False,
                (5, 0): False, (5, 1): True, (5, 2): True, (5, 3): True, (5, 4): True, (5, 5): 'Gym'}

        actual = get_user_choice(character, board, 6, 6)

        self.assertEqual(actual, 1)

    @patch('game.check_input_is_digit')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_user_choice_is_5(self, mock_output, mock_check_input_is_digit):
        mock_check_input_is_digit.side_effect = [5, 3]

        character = {'Current Location': (0, 0), 'Poke Ball': {'Squirtle': {'type': 'water', 'currentHP': 40}},
                     'Money': 30, 'Potion': 2}
        board = {(0, 0): True, (0, 1): True, (0, 2): True, (0, 3): True, (0, 4): True, (0, 5): False,
                 (1, 0): False, (1, 1): True, (1, 2): True, (1, 3): True, (1, 4): True, (1, 5): False,
                 (2, 0): False, (2, 1): True, (2, 2): 'Store', (2, 3): True, (2, 4): True, (2, 5): False,
                 (3, 0): False, (3, 1): True, (3, 2): True, (3, 3): True, (3, 4): True, (3, 5): False,
                 (4, 0): False, (4, 1): True, (4, 2): True, (4, 3): True, (4, 4): True, (4, 5): False,
                 (5, 0): False, (5, 1): True, (5, 2): True, (5, 3): True, (5, 4): True, (5, 5): 'Gym'}

        get_user_choice(character, board, 6, 6)

        the_game_printed_this = mock_output.getvalue()
        expected = "\nCurrent your pokemons' status is...\n"

        self.assertIn(expected, the_game_printed_this)

    @patch('game.check_input_is_digit')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_user_choice_is_not_between_1_and_5(self, mock_output, mock_check_input_is_digit):
        mock_check_input_is_digit.side_effect = [7, 3]

        character = {'Current Location': (0, 0), 'Poke Ball': {'Squirtle': {'type': 'water', 'currentHP': 40}},
                     'Money': 30, 'Potion': 2}
        board = {(0, 0): True, (0, 1): True, (0, 2): True, (0, 3): True, (0, 4): True, (0, 5): False,
                 (1, 0): False, (1, 1): True, (1, 2): True, (1, 3): True, (1, 4): True, (1, 5): False,
                 (2, 0): False, (2, 1): True, (2, 2): 'Store', (2, 3): True, (2, 4): True, (2, 5): False,
                 (3, 0): False, (3, 1): True, (3, 2): True, (3, 3): True, (3, 4): True, (3, 5): False,
                 (4, 0): False, (4, 1): True, (4, 2): True, (4, 3): True, (4, 4): True, (4, 5): False,
                 (5, 0): False, (5, 1): True, (5, 2): True, (5, 3): True, (5, 4): True, (5, 5): 'Gym'}

        get_user_choice(character, board, 6, 6)

        the_game_printed_this = mock_output.getvalue()
        expected = "\nPlease choose a valid direction!\n"

        self.assertIn(expected, the_game_printed_this)