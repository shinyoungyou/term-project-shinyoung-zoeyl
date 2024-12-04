import io
from unittest import TestCase
from unittest.mock import patch

from store import select_pokemon


class TestSelectPokemon(TestCase):

    @patch('builtins.input', return_value='Squirtle')
    def test_select_pokemon_user_selects_valid_option(self, _):
        pokeball = {
            'Squirtle': {'type': 'water', 'currentHP': 10},
            'Pichu': {'type': 'electric', 'currentHP': 30},
        }
        expected = ('Squirtle', {'type': 'water', 'currentHP': 10})
        actual = select_pokemon(pokeball)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['Pikachu', 'Pichu'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_pokemon_user_selects_invalid_option(self, mock_output, _):
        expected = "Invalid pokemon!"
        pokeball = {
            'Squirtle': {'type': 'water', 'currentHP': 10},
            'Pichu': {'type': 'electric', 'currentHP': 30},
        }
        select_pokemon(pokeball)
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)
