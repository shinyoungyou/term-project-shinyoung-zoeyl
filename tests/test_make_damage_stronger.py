from unittest import TestCase
from event_pokemon_attack import make_damage_stronger
from unittest.mock import patch


class Test(TestCase):

    @patch('event_pokemon_attack.get_stronger_collection')
    def test_make_damage_stronger_event_type_is_wildPokemon(self, mock_get_stronger_collection):
        mock_get_stronger_collection.return_value = (1.3, 1.5, 1.7, 2)

        result = make_damage_stronger("wildPokemon", 2)

        self.assertEqual(result, 1.3)

    @patch('event_pokemon_attack.get_stronger_collection')
    def test_make_damage_stronger_event_type_is_team_rocket(self, mock_get_stronger_collection):
        mock_get_stronger_collection.return_value = (1.3, 1.5, 1.7, 2)

        result = make_damage_stronger("Team Rocket", 2)

        self.assertEqual(result, 1.7)

    @patch('event_pokemon_attack.get_stronger_collection')
    def test_make_damage_stronger_event_type_is_strange_trainer(self, mock_get_stronger_collection):
        mock_get_stronger_collection.return_value = (1.3, 1.5, 1.7, 2)

        result = make_damage_stronger("Strange trainer", 2)

        self.assertEqual(result, 1.5)

    @patch('event_pokemon_attack.get_stronger_collection')
    def test_make_damage_stronger_event_type_is_gym_leader(self, mock_get_stronger_collection):
        mock_get_stronger_collection.return_value = (1.3, 1.5, 1.7, 2)

        result = make_damage_stronger("Gym Leader", 2)

        self.assertEqual(result, 2)