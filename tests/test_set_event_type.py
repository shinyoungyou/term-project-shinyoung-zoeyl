from unittest import TestCase
from game import set_event_type
from unittest.mock import patch


class Test(TestCase):

    @patch('random.choices', return_value=["wildPokemon"])
    def test_set_event_type_random_choice_is_wild_pokemon(self, _):
        actual = set_event_type()
        self.assertEqual(actual, "wildPokemon")

    @patch('random.choices', return_value=["Team Rocket"])
    def test_set_event_type_random_choice_is_team_rocket(self, _):
        actual = set_event_type()
        self.assertEqual(actual, "Team Rocket")

    @patch('random.choices', return_value=["Strange trainer"])
    def test_set_event_type_random_choice_is_strange_strainer(self, _):
        actual = set_event_type()
        self.assertEqual(actual, "Strange trainer")

    @patch('random.choices', return_value=[False])
    def test_set_event_type_random_choice_is_false(self, _):
        actual = set_event_type()
        self.assertEqual(actual, False)