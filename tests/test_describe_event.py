from unittest import TestCase
from unittest.mock import patch
from game import describe_event
import io


class Test(TestCase):

    @patch('game.get_event_pokemon')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_event_event_type_is_wild_pokemon(self, mock_output, mock_get_event_pokemon):
        mock_get_event_pokemon.return_value = ("Pichu", {'type': 'electric', 'currentHP': 30})

        event_type = "wildPokemon"
        character = {'Poke Ball': {'Squirtle': {'type': 'water', 'currentHP': 40}}, 'Current Level': 1}

        describe_event(event_type, character)

        the_game_printed_this = mock_output.getvalue()
        expected = '\nA wild Pichu appeared!\n'

        self.assertIn(expected, the_game_printed_this)

    @patch('game.get_event_pokemon')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_event_event_type_is_team_rocket(self, mock_output, mock_get_event_pokemon):
        mock_get_event_pokemon.return_value = ("Pichu", {'type': 'electric', 'currentHP': 30})

        event_type = "Team Rocket"
        character = {'Poke Ball': {'Squirtle': {'type': 'water', 'currentHP': 40}}, 'Current Level': 1}

        describe_event(event_type, character)

        the_game_printed_this = mock_output.getvalue()
        expected = '\nYou encountered a Team Rocket!\nTeam Rocket sent out Pichu!\n'

        self.assertIn(expected, the_game_printed_this)

    @patch('game.get_event_pokemon')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_event_event_type_is_strange_trainer(self, mock_output, mock_get_event_pokemon):
        mock_get_event_pokemon.return_value = ("Pichu", {'type': 'electric', 'currentHP': 30})

        event_type = "Strange trainer"
        character = {'Poke Ball': {'Squirtle': {'type': 'water', 'currentHP': 40}}, 'Current Level': 1}

        describe_event(event_type, character)

        the_game_printed_this = mock_output.getvalue()
        expected = '\nYou encountered a Strange trainer!\nStrange trainer sent out Pichu!\n'

        self.assertIn(expected, the_game_printed_this)