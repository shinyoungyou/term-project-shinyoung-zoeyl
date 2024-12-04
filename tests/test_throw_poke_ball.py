from unittest import TestCase
from unittest.mock import patch
from event_option import throw_poke_ball
import io


class Test(TestCase):

    @patch('event_option.check_total_of_user_pokemons')
    @patch('event_option.level_maximum_hp')
    @patch('event_option.get_probability')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_throw_poke_ball_event_pokemon_hp_less_than_11_condition_is_true(self, mock_output, mock_get_probability,
                                                                             mock_level_maximum_hp,
                                                                             mock_check_total_of_user_pokemons):
        mock_check_total_of_user_pokemons.return_value = True

        event_pokemon_info = ('Luxray', {'type': 'electric', 'currentHP': 8})
        character = {'Poke Ball': {'Metapod': {'type': 'grass', 'currentHP': 50}}, 'Current Level': 2}

        throw_poke_ball(event_pokemon_info, character)

        mock_get_probability.assert_not_called()
        mock_level_maximum_hp.assert_called_once()

        the_game_printed_this = mock_output.getvalue()
        expected = '\nGotcha! Luxray was caught!\n'

        self.assertIn(expected, the_game_printed_this)

    @patch('event_option.check_total_of_user_pokemons')
    @patch('event_option.level_maximum_hp')
    @patch('event_option.get_probability')
    def test_throw_poke_ball_event_pokemon_hp_less_than_11_condition_is_false(self, mock_get_probability,
                                                                              mock_level_maximum_hp,
                                                                              mock_check_total_of_user_pokemons):
        mock_check_total_of_user_pokemons.return_value = False

        event_pokemon_info = ('Luxray', {'type': 'electric', 'currentHP': 8})
        character = {'Poke Ball': {'Metapod': {'type': 'grass', 'currentHP': 50},
                                   'Vanillite': {'type': 'ice', 'currentHP': 30},
                                   'Spheal': {'type': 'ice', 'currentHP': 30},
                                   'Swinub': {'type': 'ice', 'currentHP': 30},
                                   'Magby': {'type': 'fire', 'currentHP': 30},
                                   'Charmander': {'type': 'fire', 'currentHP': 40}}, 'Current Level': 2}

        result = throw_poke_ball(event_pokemon_info, character)

        mock_get_probability.assert_not_called()
        mock_level_maximum_hp.assert_not_called()

        self.assertEqual(result, False)

    @patch('event_option.check_total_of_user_pokemons')
    @patch('event_option.level_maximum_hp')
    @patch('event_option.get_probability')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_throw_poke_ball_event_pokemon_hp_more_than_10(self, mock_output, mock_get_probability,
                                                           mock_level_maximum_hp, mock_check_total_of_user_pokemons):
        event_pokemon_info = ('Luxray', {'type': 'electric', 'currentHP': 40})
        character = {'Poke Ball': {'Metapod': {'type': 'grass', 'currentHP': 50}}, 'Current Level': 2}

        throw_poke_ball(event_pokemon_info, character)

        mock_get_probability.assert_called_once()
        mock_level_maximum_hp.assert_not_called()
        mock_check_total_of_user_pokemons.assert_not_called()

        the_game_printed_this = mock_output.getvalue()
        expected = '\nShoot! It was so close!\n'

        self.assertIn(expected, the_game_printed_this)
