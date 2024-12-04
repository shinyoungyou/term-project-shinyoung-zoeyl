from unittest import TestCase
from game import set_up_game
from unittest.mock import patch
import io


class Test(TestCase):

    @patch('builtins.input', side_effect=['Zoey', 'pokemon', 'Charmander'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_set_up_game_when_user_input_is_wrong(self, mock_output, _):
        set_up_game()
        the_game_printed_this = mock_output.getvalue()
        expected = 'Pokemon is not included in Starting Pokémon\n'
        self.assertIn(expected, the_game_printed_this)

    @patch('builtins.input', side_effect=['Zoey', 'Charmander'])
    def test_set_up_game_contains_character_name_key(self, _):
        result = set_up_game()
        self.assertIn('Character Name', result[0])

    @patch('builtins.input', side_effect=['Zoey', 'Charmander'])
    def test_set_up_game_contains_money_key(self, _):
        result = set_up_game()
        self.assertIn("Money", result[0])

    @patch('builtins.input', side_effect=['Zoey', 'Charmander'])
    def test_set_up_game_contains_character_current_level_key(self, _):
        result = set_up_game()
        self.assertIn("Current Level", result[0])

    @patch('builtins.input', side_effect=['Zoey', 'Charmander'])
    def test_set_up_game_contains_character_potion_key(self, _):
        result = set_up_game()
        self.assertIn("Potion", result[0])

    @patch('builtins.input', side_effect=['Zoey', 'Charmander'])
    def test_set_up_game_contains_character_current_location_key(self, _):
        result = set_up_game()
        self.assertIn("Current Location", result[0])

    @patch('builtins.input', side_effect=['Zoey', 'Charmander'])
    def test_set_up_game_character_name_value_is_user_input(self, _):
        result = set_up_game()
        actual = result[0]["Character Name"]
        expected = "Zoey"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['Zoey', 'Charmander'])
    def test_set_up_game_character_money_value_is_30(self, _):
        result = set_up_game()
        actual = result[0]["Money"]
        expected = 30
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['Zoey', 'Charmander'])
    def test_set_up_game_character_current_level_value_is_1(self, _):
        result = set_up_game()
        actual = result[0]["Current Level"]
        expected = 1
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['Zoey', 'Charmander'])
    def test_set_up_game_character_potion_value_is_0(self, _):
        result = set_up_game()
        actual = result[0]["Potion"]
        expected = 0
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['Zoey', 'Charmander'])
    def test_set_up_game_character_current_location_value_is_0(self, _):
        result = set_up_game()
        actual = result[0]["Current Location"]
        expected = (0, 0)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['Zoey', 'Charmander'])
    def test_set_up_game_character_poke_ball_value_is_user_input_pokemon_and_its_data(self, _):
        result = set_up_game()
        actual = result[0]["Poke Ball"]
        expected = {'Charmander': {'type': 'fire', 'currentHP': 40}}
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['Zoey', 'Charmander'])
    def test_set_up_game_character_starting_pokemon_value_is_user_input(self, _):
        result = set_up_game()
        actual = result[0]["Starting Pokémon"]
        expected = "Charmander"
        self.assertEqual(expected, actual)
