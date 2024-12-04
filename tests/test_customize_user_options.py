from unittest import TestCase
from prepare_event import customize_user_options


class Test(TestCase):

    def test_customize_user_options_event_type_is_wild_pokemon(self):
        result = customize_user_options("wildPokemon")
        expected = ["Fight", "Change Pokemon", "Use Potion", "Throw Poke Ball", "Run Away"]

        self.assertEqual(result, expected)

    def test_customize_user_options_event_type_is_team_rocket(self):
        result = customize_user_options("Team Rocket")
        expected = ["Fight", "Change Pokemon", "Use Potion"]

        self.assertEqual(result, expected)

    def test_customize_user_options_event_type_is_strange_trainer(self):
        result = customize_user_options("Strange trainer")
        expected = ["Fight", "Change Pokemon", "Use Potion"]

        self.assertEqual(result, expected)

    def test_customize_user_options_event_type_is_gym_leader_round_between_1_and_2(self):
        result = customize_user_options("Gym Leader", 2)
        expected = ["Fight", "Change Pokemon"]

        self.assertEqual(result, expected)

    def test_customize_user_options_event_type_is_gym_leader_round_greater_than_2(self):
        result = customize_user_options("Gym Leader", 4)
        expected = ["Fight", "Change Pokemon", "Run Away"]

        self.assertEqual(result, expected)
