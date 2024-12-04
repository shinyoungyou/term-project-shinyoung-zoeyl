from unittest import TestCase
from unittest.mock import patch
from event_option import check_total_of_user_pokemons
import io


class Test(TestCase):

    @patch('event_option.select_release_pokemon')
    @patch('builtins.input', return_value='y')
    def test_check_total_of_user_pokemons_user_has_6_pokemon_and_chose_yes(self, _, mock_select_release_pokemon):
        character = {"Poke Ball": {'Geodude': {'type': 'rock', 'currentHP': 30},
                                   'Vanillite': {'type': 'ice', 'currentHP': 30},
                                   'Spheal': {'type': 'ice', 'currentHP': 30},
                                   'Swinub': {'type': 'ice', 'currentHP': 30},
                                   'Magby': {'type': 'fire', 'currentHP': 30},
                                   'Charmander': {'type': 'fire', 'currentHP': 40}}}
        event_pokemon_info = ('Aron', {'type': 'rock', 'currentHP': 30})

        result = check_total_of_user_pokemons(character, event_pokemon_info)

        mock_select_release_pokemon.assert_called_once()
        self.assertEqual(result, True)

    @patch('event_option.select_release_pokemon')
    @patch('builtins.input', return_value='n')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_total_of_user_pokemons_user_has_6_pokemon_and_chose_no(self, mock_output, _, mock_select_release_pokemon):
        character = {"Poke Ball": {'Geodude': {'type': 'rock', 'currentHP': 30},
                                   'Vanillite': {'type': 'ice', 'currentHP': 30},
                                   'Spheal': {'type': 'ice', 'currentHP': 30},
                                   'Swinub': {'type': 'ice', 'currentHP': 30},
                                   'Magby': {'type': 'fire', 'currentHP': 30},
                                   'Charmander': {'type': 'fire', 'currentHP': 40}}}
        event_pokemon_info = ('Aron', {'type': 'rock', 'currentHP': 30})

        check_total_of_user_pokemons(character, event_pokemon_info)

        mock_select_release_pokemon.assert_not_called()
        the_game_printed_this = mock_output.getvalue()
        expected = '\nAron broke free!\n'

        self.assertIn(expected, the_game_printed_this)

    @patch('event_option.select_release_pokemon')
    @patch('builtins.input', side_effect=['u', 'y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_total_of_user_pokemons_user_has_6_pokemon_and_chose_other(self, mock_output, _,
                                                                             mock_select_release_pokemon):
        character = {"Poke Ball": {'Geodude': {'type': 'rock', 'currentHP': 30},
                                   'Vanillite': {'type': 'ice', 'currentHP': 30},
                                   'Spheal': {'type': 'ice', 'currentHP': 30},
                                   'Swinub': {'type': 'ice', 'currentHP': 30},
                                   'Magby': {'type': 'fire', 'currentHP': 30},
                                   'Charmander': {'type': 'fire', 'currentHP': 40}}}
        event_pokemon_info = ('Aron', {'type': 'rock', 'currentHP': 30})

        check_total_of_user_pokemons(character, event_pokemon_info)

        mock_select_release_pokemon.assert_called_once()
        the_game_printed_this = mock_output.getvalue()
        expected = '\nu is not a valid option\n'

        self.assertIn(expected, the_game_printed_this)

    @patch('event_option.select_release_pokemon')
    @patch('builtins.input', side_effect=['u', 'y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_total_of_user_pokemons_user_does_not_have_6_pokemon(self, mock_output, _,
                                                                       mock_select_release_pokemon):
        character = {"Poke Ball": {'Geodude': {'type': 'rock', 'currentHP': 30},
                                   'Vanillite': {'type': 'ice', 'currentHP': 30},
                                   'Spheal': {'type': 'ice', 'currentHP': 30},
                                   'Magby': {'type': 'fire', 'currentHP': 30},
                                   'Charmander': {'type': 'fire', 'currentHP': 40}}}
        event_pokemon_info = ('Aron', {'type': 'rock', 'currentHP': 30})

        result = check_total_of_user_pokemons(character, event_pokemon_info)

        mock_select_release_pokemon.assert_not_called()
        self.assertEqual(result, True)