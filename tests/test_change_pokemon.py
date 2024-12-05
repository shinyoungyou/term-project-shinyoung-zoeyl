from unittest import TestCase
from unittest.mock import patch
from event_option import change_pokemon
import io


class Test(TestCase):

    @patch('builtins.input', return_value='Luxio')
    def test_change_pokemon_user_has_pokemon_more_than_1(self, _):
        pokeball = {'Metapod': {'type': 'grass', 'currentHP': 50}, 'Luxio': {'type': 'electric', 'currentHP': 50}}
        character_pokemon = ('Metapod', {'type': 'grass', 'currentHP': 50})

        result = change_pokemon(pokeball, character_pokemon)
        expected = ('Luxio', {'type': 'electric', 'currentHP': 50})

        self.assertEqual(result, expected)

    @patch('builtins.input', side_effect=['Seadra', 'Luxio'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_change_pokemon_user_input_is_wrong(self, mock_output, _):
        pokeball = {'Metapod': {'type': 'grass', 'currentHP': 50}, 'Luxio': {'type': 'electric', 'currentHP': 50}}
        character_pokemon = ('Metapod', {'type': 'grass', 'currentHP': 50})

        change_pokemon(pokeball, character_pokemon)

        the_game_printed_this = mock_output.getvalue()
        expected = '\nSeadra is not included in your Poké Balls or has 0HP\n'

        self.assertIn(expected, the_game_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_change_pokemon_user_has_one_pokemon(self, mock_output):
        pokeball = {'Metapod': {'type': 'grass', 'currentHP': 50}}
        character_pokemon = ('Metapod', {'type': 'grass', 'currentHP': 50})

        change_pokemon(pokeball, character_pokemon)

        the_game_printed_this = mock_output.getvalue()
        expected = '\nYou has no Pokémon to switch to\n'

        self.assertIn(expected, the_game_printed_this)

    @patch('builtins.input', return_value='Metapod')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_change_pokemon_only_current_pokemon_has_hp(self, mock_output, _):
        pokeball = {
            'Metapod': {'type': 'grass', 'currentHP': 50},
            'Luxio': {'type': 'electric', 'currentHP': 0},
            'Charmander': {'type': 'fire', 'currentHP': 0}
        }
        character_pokemon = ('Metapod', {'type': 'grass', 'currentHP': 50})

        change_pokemon(pokeball, character_pokemon)

        the_game_printed_this = mock_output.getvalue()
        expected = "\nNo other Pokémon is available for switching (All have 0HP).\n"
        self.assertIn(expected, the_game_printed_this)
