from unittest import TestCase
from unittest.mock import patch
from event_option import get_attack_result


class Test(TestCase):

    @patch('event_option.make_stronger')
    @patch('event_option.get_money')
    @patch('random.randrange', return_value=6)
    def test_get_attack_result_event_type_is_not_gym_leader(self, _, mock_get_money, mock_make_stronger):
        mock_make_stronger.return_value = 1.3

        character_pokemon_skill = {'name': 'Fire Punch', 'damage': (6, 7)}
        event_pokemon_info = ('Piloswine', {'type': 'ice', 'currentHP': 3})
        character = {"Current Level": 2}
        result = get_attack_result(character_pokemon_skill, event_pokemon_info, character, "wildPokemon")

        mock_get_money.assert_called_once()
        self.assertEqual(result, False)

    @patch('event_option.make_stronger')
    @patch('event_option.get_money')
    @patch('random.randrange', return_value=6)
    def test_get_attack_result_event_type_is_gym_leader(self, _, mock_get_money, mock_make_stronger):
        mock_make_stronger.return_value = 1.3

        character_pokemon_skill = {'name': 'Fire Punch', 'damage': (6, 7)}
        event_pokemon_info = ('Piloswine', {'type': 'ice', 'currentHP': 3})
        character = {"Current Level": 2}
        result = get_attack_result(character_pokemon_skill, event_pokemon_info, character, "Gym Leader")

        mock_get_money.assert_not_called()
        self.assertEqual(result, False)

    @patch('event_option.make_stronger')
    @patch('event_option.get_money')
    @patch('random.randrange', return_value=6)
    def test_get_attack_result_event_pokemon_hp_leaves_greater_than_0(self, _, mock_get_money, mock_make_stronger):
        mock_make_stronger.return_value = 1.3

        character_pokemon_skill = {'name': 'Fire Punch', 'damage': (6, 7)}
        event_pokemon_info = ('Piloswine', {'type': 'ice', 'currentHP': 50})
        character = {"Current Level": 2}
        result = get_attack_result(character_pokemon_skill, event_pokemon_info, character, "Team Rocket")

        mock_get_money.assert_not_called()
        self.assertEqual(result, True)

    @patch('event_option.make_stronger')
    @patch('event_option.get_money')
    @patch('random.randrange', return_value=6)
    def test_get_attack_result_event_pokemon_hp_leaves_less_than_0(self, _, mock_get_money, mock_make_stronger):
        mock_make_stronger.return_value = 1.3

        character_pokemon_skill = {'name': 'Fire Punch', 'damage': (6, 7)}
        event_pokemon_info = ('Piloswine', {'type': 'ice', 'currentHP': 2})
        character = {"Current Level": 2}
        result = get_attack_result(character_pokemon_skill, event_pokemon_info, character, "Strange trainer")

        mock_get_money.assert_called_once()
        self.assertEqual(result, False)
