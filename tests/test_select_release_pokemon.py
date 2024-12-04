from unittest import TestCase
from unittest.mock import patch
from event_option import select_release_pokemon
import io


class Test(TestCase):

    @patch('builtins.input', return_value='Vanillite')
    def test_select_release_pokemon_release_pokemon(self, _):
        character = {"Poke Ball": {'Geodude': {'type': 'rock', 'currentHP': 30},
                                   'Vanillite': {'type': 'ice', 'currentHP': 30},
                                   'Spheal': {'type': 'ice', 'currentHP': 30},
                                   'Swinub': {'type': 'ice', 'currentHP': 30},
                                   'Magby': {'type': 'fire', 'currentHP': 30},
                                   'Charmander': {'type': 'fire', 'currentHP': 40}}, 'Starting Pokemon': 'Charmander'}

        select_release_pokemon(character)
        expected = {'Charmander': {'currentHP': 40, 'type': 'fire'},
                    'Geodude': {'currentHP': 30, 'type': 'rock'},
                    'Magby': {'currentHP': 30, 'type': 'fire'},
                    'Spheal': {'currentHP': 30, 'type': 'ice'},
                    'Swinub': {'currentHP': 30, 'type': 'ice'}}

        self.assertEqual(character['Poke Ball'], expected)

    @patch('builtins.input', side_effect=['Charmander', 'Magby'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_release_pokemon_user_chose_starting_pokemon(self, mock_output, _):
        character = {"Poke Ball": {'Geodude': {'type': 'rock', 'currentHP': 30},
                                   'Vanillite': {'type': 'ice', 'currentHP': 30},
                                   'Spheal': {'type': 'ice', 'currentHP': 30},
                                   'Swinub': {'type': 'ice', 'currentHP': 30},
                                   'Magby': {'type': 'fire', 'currentHP': 30},
                                   'Charmander': {'type': 'fire', 'currentHP': 40}}, 'Starting Pokemon': 'Charmander'}

        select_release_pokemon(character)

        the_game_printed_this = mock_output.getvalue()
        expected = "\nCharmander can't be chosen!\n"

        self.assertIn(expected, the_game_printed_this)

    @patch('builtins.input', side_effect=['Flaaffy', 'Magby'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_release_pokemon_user_chose_pokemon_user_does_not_have(self, mock_output, _):
        character = {"Poke Ball": {'Geodude': {'type': 'rock', 'currentHP': 30},
                                   'Vanillite': {'type': 'ice', 'currentHP': 30},
                                   'Spheal': {'type': 'ice', 'currentHP': 30},
                                   'Swinub': {'type': 'ice', 'currentHP': 30},
                                   'Magby': {'type': 'fire', 'currentHP': 30},
                                   'Charmander': {'type': 'fire', 'currentHP': 40}}, 'Starting Pokemon': 'Charmander'}

        select_release_pokemon(character)

        the_game_printed_this = mock_output.getvalue()
        expected = "\nFlaaffy can't be chosen!\n"

        self.assertIn(expected, the_game_printed_this)

