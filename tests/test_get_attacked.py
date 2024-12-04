from unittest import TestCase
from unittest.mock import patch
from event_pokemon_attack import get_attacked
import io


class Test(TestCase):

    @patch('event_pokemon_attack.get_skill_of')
    @patch('event_pokemon_attack.make_damage_stronger')
    @patch('event_pokemon_attack.get_probability')
    @patch('event_pokemon_attack.check_status')
    @patch('random.choices', side_effect=[[{'name': 'Tackle', 'damage': (1, 3)}], 2])
    def test_get_attacked_skill_hit(self, _, mock_check_status, mock_get_probability, mock_make_damage_stronger,
                                    mock_get_skill_of):

        mock_get_probability.return_value = True
        mock_get_skill_of.return_value = [{'name': 'Tackle', 'damage': (1, 3)}, {'name': 'Water Gun', 'damage': (4, 5)},
                                          {'name': 'Aqua Jet', 'damage': (6, 7)}]
        mock_make_damage_stronger.return_value = 1.4

        event_pokemon_info = ('Marshtomp', {'type': 'water', 'currentHP': 50})
        character = {'Current Level': 2, 'Poke Ball': {'Kakuna': {'type': 'grass', 'currentHP': 50}}}
        character_pokemon = ('Kakuna', {'type': 'grass', 'currentHP': 50})

        get_attacked(event_pokemon_info, "Team Rocket", character, character_pokemon)

        mock_check_status.assert_called_once()

        self.assertEqual(character_pokemon[1]['currentHP'], 48)

    @patch('event_pokemon_attack.get_skill_of')
    @patch('event_pokemon_attack.make_damage_stronger')
    @patch('event_pokemon_attack.get_probability')
    @patch('event_pokemon_attack.check_status')
    @patch('random.choices', return_value=[{'name': 'Tackle', 'damage': (1, 3)}])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_attacked_skill_missed(self, mock_output, _, mock_check_status, mock_get_probability,
                                       mock_make_damage_stronger, mock_get_skill_of):
        mock_get_probability.return_value = False
        mock_get_skill_of.return_value = [{'name': 'Tackle', 'damage': (1, 3)}, {'name': 'Water Gun', 'damage': (4, 5)},
                                          {'name': 'Aqua Jet', 'damage': (6, 7)}]

        event_pokemon_info = ('Marshtomp', {'type': 'water', 'currentHP': 50})
        character = {'Current Level': 2, 'Poke Ball': {'Kakuna': {'type': 'grass', 'currentHP': 50}}}
        character_pokemon = ('Kakuna', {'type': 'grass', 'currentHP': 50})

        get_attacked(event_pokemon_info, "Team Rocket", character, character_pokemon)

        mock_check_status.assert_called_once()
        mock_make_damage_stronger.assert_called_once()

        the_game_printed_this = mock_output.getvalue()
        expected = 'Tackle missed!\n'

        self.assertIn(expected, the_game_printed_this)