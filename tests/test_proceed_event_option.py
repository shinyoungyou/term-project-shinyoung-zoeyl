from unittest import TestCase
from unittest.mock import patch
from prepare_event import proceed_event_option
import io


class Test(TestCase):

    @patch('prepare_event.fight')
    def test_proceed_event_option_user_choice_is_fight(self, mock_fight):
        mock_fight.return_value = True

        user_choice = "Fight"
        character_pokemon = ("Squirtle", {'type': 'water', 'currentHP': 40})
        character = {'Poke Ball': {'Squirtle': {'type': 'water', 'currentHP': 40}}, 'Current Level': 1}
        event_pokemon_info = ("Pichu", {'type': 'electric', 'currentHP': 30})
        event_type = "wildPokemon"

        result = proceed_event_option(user_choice, character_pokemon, character, event_pokemon_info, event_type)

        mock_fight.assert_called_once()
        self.assertTrue(result, True)

    @patch('prepare_event.throw_poke_ball')
    def test_proceed_event_option_user_choice_is_throw_poke_ball(self, mock_throw_poke_ball):
        mock_throw_poke_ball.return_value = False

        user_choice = "Throw Poke Ball"
        character_pokemon = ("Squirtle", {'type': 'water', 'currentHP': 40})
        character = {'Poke Ball': {'Squirtle': {'type': 'water', 'currentHP': 40}}, 'Current Level': 1}
        event_pokemon_info = ("Pichu", {'type': 'electric', 'currentHP': 30})
        event_type = "wildPokemon"

        result = proceed_event_option(user_choice, character_pokemon, character, event_pokemon_info, event_type)

        mock_throw_poke_ball.assert_called_once()
        self.assertFalse(result, False)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_proceed_event_option_user_choice_is_run_away(self, mock_output):
        user_choice = "Run Away"
        character_pokemon = ("Squirtle", {'type': 'water', 'currentHP': 40})
        character = {'Character Name': "user", 'Poke Ball': {'Squirtle': {'type': 'water', 'currentHP': 40}},
                     'Current Level': 1}
        event_pokemon_info = ("Pichu", {'type': 'electric', 'currentHP': 30})
        event_type = "wildPokemon"

        proceed_event_option(user_choice, character_pokemon, character, event_pokemon_info, event_type)
        the_game_printed_this = mock_output.getvalue()
        expected = '\nYou escaped from Pichu!\n'
        self.assertIn(expected, the_game_printed_this)
