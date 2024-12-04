import io
from unittest import TestCase
from unittest.mock import patch

from gym import encounter_gym


class TestEncounterGym(TestCase):

    @patch('gym.battle_with_gym_leader', return_value=False)
    @patch('builtins.input', side_effect=['y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_encounter_gym_user_enters_y(self, mock_output, _, __):
        expected = "Gym Leader: Welcome to the gym!"
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 1, 'Potion': 0,
                     'Current Location': (5, 5),
                     'Starting Pokemon': 'Squirtle',
                     'Poke Ball': {
                         'Squirtle': {'type': 'water', 'currentHP': 40},
                         'Pichu': {'type': 'electric', 'currentHP': 30},
                         'Shinx': {'type': 'electric', 'currentHP': 30},
                         'Mareep': {'type': 'electric', 'currentHP': 30},
                         'Caterpie': {'type': 'grass', 'currentHP': 30},
                         'Weedle': {'type': 'grass', 'currentHP': 30},
                     }}
        encounter_gym(character)
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('gym.battle_with_gym_leader', return_value=False)
    @patch('builtins.input', side_effect=['n'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_encounter_gym_user_enters_n(self, mock_output, _, __):
        not_expected = "Gym Leader: Welcome to the gym!"
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 1, 'Potion': 0,
                     'Current Location': (5, 5),
                     'Starting Pokemon': 'Squirtle',
                     'Poke Ball': {
                         'Squirtle': {'type': 'water', 'currentHP': 40},
                         'Pichu': {'type': 'electric', 'currentHP': 30},
                         'Shinx': {'type': 'electric', 'currentHP': 30},
                         'Mareep': {'type': 'electric', 'currentHP': 30},
                         'Caterpie': {'type': 'grass', 'currentHP': 30},
                         'Weedle': {'type': 'grass', 'currentHP': 30},
                     }}
        encounter_gym(character)
        actual = mock_output.getvalue()
        self.assertNotIn(not_expected, actual)

    @patch('gym.battle_with_gym_leader', return_value=False)
    @patch('builtins.input', side_effect=['q', 'n'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_encounter_gym_user_enters_invalid_input(self, mock_output, _, __):
        expected = "Please Enter y or n."
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 1, 'Potion': 0,
                     'Current Location': (5, 5),
                     'Starting Pokemon': 'Squirtle',
                     'Poke Ball': {
                         'Squirtle': {'type': 'water', 'currentHP': 40},
                         'Pichu': {'type': 'electric', 'currentHP': 30},
                         'Shinx': {'type': 'electric', 'currentHP': 30},
                         'Mareep': {'type': 'electric', 'currentHP': 30},
                         'Caterpie': {'type': 'grass', 'currentHP': 30},
                         'Weedle': {'type': 'grass', 'currentHP': 30},
                     }}
        encounter_gym(character)
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)
