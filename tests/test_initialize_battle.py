import io
from unittest import TestCase
from unittest.mock import patch

from gym import initialize_battle


class TestInitializeBattle(TestCase):

    @patch('gym.take_out_pokemon', return_value=('Squirtle', {'type': 'water', 'currentHP': 40}))
    @patch('gym.get_event_pokemon', return_value=('Pidove', {'type': 'flying', 'currentHP': 30}))
    def test_initialize_battle_in_level_1(self, _, __):
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
        expected = (0, 0, 1, ('Squirtle', {'type': 'water', 'currentHP': 40}),
                    ('Pidove', {'type': 'flying', 'currentHP': 30}))
        actual = initialize_battle(character)
        self.assertEqual(expected, actual)

    @patch('gym.take_out_pokemon', return_value=('Wartortle', {'type': 'water', 'currentHP': 65}))
    @patch('gym.get_event_pokemon', return_value=('Pidgeotto', {'type': 'flying', 'currentHP': 50}))
    def test_initialize_battle_in_level_2(self, _, __):
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 2, 'Potion': 0,
                     'Current Location': (7, 4),
                     'Starting Pokemon': 'Wartortle',
                     'Poke Ball': {
                         'Wartortle': {'type': 'water', 'currentHP': 65},
                         'Luxray': {'type': 'electric', 'currentHP': 80},
                         'Ampharos': {'type': 'electric', 'currentHP': 80},
                         'Butterfree': {'type': 'grass', 'currentHP': 80},
                         'Beedrill': {'type': 'grass', 'currentHP': 80},
                         'Sceptile': {'type': 'grass', 'currentHP': 80},
                     }}
        expected = (0, 0, 1, ('Wartortle', {'type': 'water', 'currentHP': 65}),
                    ('Pidgeotto', {'type': 'flying', 'currentHP': 50}))
        actual = initialize_battle(character)
        self.assertEqual(expected, actual)

    @patch('gym.take_out_pokemon', return_value=('Blastoise', {'type': 'water', 'currentHP': 100}))
    @patch('gym.get_event_pokemon', return_value=('Pidgeot', {'type': 'flying', 'currentHP': 80}))
    def test_initialize_battle_in_level_3(self, _, __):
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 3, 'Potion': 0,
                     'Current Location': (9, 0),
                     'Starting Pokemon': 'Blastoise',
                     'Poke Ball': {
                         'Blastoise': {'type': 'water', 'currentHP': 100},
                         'Luxray': {'type': 'electric', 'currentHP': 80},
                         'Ampharos': {'type': 'electric', 'currentHP': 80},
                         'Butterfree': {'type': 'grass', 'currentHP': 80},
                         'Beedrill': {'type': 'grass', 'currentHP': 80},
                         'Sceptile': {'type': 'grass', 'currentHP': 80},
                     }}
        expected = (0, 0, 1, ('Blastoise', {'type': 'water', 'currentHP': 100}),
                    ('Pidgeot', {'type': 'flying', 'currentHP': 80}))
        actual = initialize_battle(character)
        self.assertEqual(expected, actual)
