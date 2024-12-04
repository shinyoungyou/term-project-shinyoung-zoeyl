import io
from unittest import TestCase
from unittest.mock import patch

from gym import level_up


class TestLevelUp(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_level_up_to_2(self, mock_output):
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 1, 'Potion': 0,
                     'Current Location': (5, 5),
                     'Starting Pokèmon': 'Squirtle',
                     'Poke Ball': {
                         'Squirtle': {'type': 'water', 'currentHP': 40},
                         'Pichu': {'type': 'electric', 'currentHP': 30},
                         'Shinx': {'type': 'electric', 'currentHP': 30},
                         'Mareep': {'type': 'electric', 'currentHP': 30},
                         'Caterpie': {'type': 'grass', 'currentHP': 30},
                         'Weedle': {'type': 'grass', 'currentHP': 30},
                     }}
        expected = "You've leveled up to 2!"
        level_up(character)
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_level_up_to_3(self, mock_output):
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 2, 'Potion': 0,
                     'Current Location': (7, 4),
                     'Starting Pokèmon': 'Wartortle',
                     'Poke Ball': {
                         'Wartortle': {'type': 'water', 'currentHP': 65},
                         'Luxray': {'type': 'electric', 'currentHP': 80},
                         'Ampharos': {'type': 'electric', 'currentHP': 80},
                         'Butterfree': {'type': 'grass', 'currentHP': 80},
                         'Beedrill': {'type': 'grass', 'currentHP': 80},
                         'Sceptile': {'type': 'grass', 'currentHP': 80},
                     }}
        expected = "You've leveled up to 3!"
        level_up(character)
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)
