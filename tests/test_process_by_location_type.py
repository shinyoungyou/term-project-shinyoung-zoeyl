from unittest import TestCase
from unittest.mock import patch


from game import process_by_location_type


class TestProcessByLocationType(TestCase):

    @patch('game.has_six_pokemons', return_value=True)
    @patch('game.encounter_gym', return_value=True)
    def test_process_by_location_type_character_location_is_gym_and_earned_gym_badge_in_level_1(self, _, __):
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
        board = {(0, 0): True, (0, 1): True, (0, 2): True, (0, 3): True, (0, 4): True, (0, 5): False,
                 (1, 0): False, (1, 1): True, (1, 2): True, (1, 3): True, (1, 4): True, (1, 5): False,
                 (2, 0): False, (2, 1): True, (2, 2): 'Store', (2, 3): True, (2, 4): True, (2, 5): False,
                 (3, 0): False, (3, 1): True, (3, 2): True, (3, 3): True, (3, 4): True, (3, 5): False,
                 (4, 0): False, (4, 1): True, (4, 2): True, (4, 3): True, (4, 4): True, (4, 5): False,
                 (5, 0): False, (5, 1): True, (5, 2): True, (5, 3): True, (5, 4): True, (5, 5): 'Gym'}
        expected = False
        actual = process_by_location_type(character, board)
        self.assertEqual(expected, actual)

    @patch('game.has_six_pokemons', return_value=True)
    @patch('game.encounter_gym', return_value=True)
    def test_process_by_location_type_character_location_is_gym_and_earned_gym_badge_in_level_2(self, _, __):
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 2, 'Potion': 0,
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
        board = {(0, 0): True, (0, 1): True, (0, 2): True, (0, 3): True, (0, 4): True, (0, 5): False,
                 (1, 0): False, (1, 1): True, (1, 2): True, (1, 3): True, (1, 4): True, (1, 5): False,
                 (2, 0): False, (2, 1): True, (2, 2): 'Store', (2, 3): True, (2, 4): True, (2, 5): False,
                 (3, 0): False, (3, 1): True, (3, 2): True, (3, 3): True, (3, 4): True, (3, 5): False,
                 (4, 0): False, (4, 1): True, (4, 2): True, (4, 3): True, (4, 4): True, (4, 5): False,
                 (5, 0): False, (5, 1): True, (5, 2): True, (5, 3): True, (5, 4): True, (5, 5): 'Gym'}
        expected = False
        actual = process_by_location_type(character, board)
        self.assertEqual(expected, actual)

    @patch('game.has_six_pokemons', return_value=True)
    @patch('game.encounter_gym', return_value=True)
    def test_process_by_location_type_character_location_is_gym_and_earned_gym_badge_in_level_3(self, _, __):
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 3, 'Potion': 0,
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
        board = {(0, 0): True, (0, 1): True, (0, 2): True, (0, 3): True, (0, 4): True, (0, 5): False,
                 (1, 0): False, (1, 1): True, (1, 2): True, (1, 3): True, (1, 4): True, (1, 5): False,
                 (2, 0): False, (2, 1): True, (2, 2): 'Store', (2, 3): True, (2, 4): True, (2, 5): False,
                 (3, 0): False, (3, 1): True, (3, 2): True, (3, 3): True, (3, 4): True, (3, 5): False,
                 (4, 0): False, (4, 1): True, (4, 2): True, (4, 3): True, (4, 4): True, (4, 5): False,
                 (5, 0): False, (5, 1): True, (5, 2): True, (5, 3): True, (5, 4): True, (5, 5): 'Gym'}
        expected = True
        actual = process_by_location_type(character, board)
        self.assertEqual(expected, actual)

    @patch('game.encounter_store', return_value=None)
    def test_process_by_location_type_character_location_is_store_in_level_1(self, _):
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 1, 'Potion': 0,
                     'Current Location': (2, 2),
                     'Starting Pokemon': 'Squirtle',
                     'Poke Ball': {
                         'Squirtle': {'type': 'water', 'currentHP': 40},
                         'Pichu': {'type': 'electric', 'currentHP': 30},
                         'Shinx': {'type': 'electric', 'currentHP': 30},
                         'Mareep': {'type': 'electric', 'currentHP': 30},
                         'Caterpie': {'type': 'grass', 'currentHP': 30},
                         'Weedle': {'type': 'grass', 'currentHP': 30},
                     }}
        board = {(0, 0): True, (0, 1): True, (0, 2): True, (0, 3): True, (0, 4): True, (0, 5): False,
                 (1, 0): False, (1, 1): True, (1, 2): True, (1, 3): True, (1, 4): True, (1, 5): False,
                 (2, 0): False, (2, 1): True, (2, 2): 'Store', (2, 3): True, (2, 4): True, (2, 5): False,
                 (3, 0): False, (3, 1): True, (3, 2): True, (3, 3): True, (3, 4): True, (3, 5): False,
                 (4, 0): False, (4, 1): True, (4, 2): True, (4, 3): True, (4, 4): True, (4, 5): False,
                 (5, 0): False, (5, 1): True, (5, 2): True, (5, 3): True, (5, 4): True, (5, 5): 'Gym'}
        expected = False
        actual = process_by_location_type(character, board)
        self.assertEqual(expected, actual)

    @patch('game.encounter_store', return_value=None)
    def test_process_by_location_type_character_location_is_store_in_level_2(self, _):
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 2, 'Potion': 0,
                     'Current Location': (2, 2),
                     'Starting Pokemon': 'Squirtle',
                     'Poke Ball': {
                         'Squirtle': {'type': 'water', 'currentHP': 40},
                         'Pichu': {'type': 'electric', 'currentHP': 30},
                         'Shinx': {'type': 'electric', 'currentHP': 30},
                         'Mareep': {'type': 'electric', 'currentHP': 30},
                         'Caterpie': {'type': 'grass', 'currentHP': 30},
                         'Weedle': {'type': 'grass', 'currentHP': 30},
                     }}
        board = {(0, 0): True, (0, 1): True, (0, 2): True, (0, 3): True, (0, 4): True, (0, 5): False,
                 (1, 0): False, (1, 1): True, (1, 2): True, (1, 3): True, (1, 4): True, (1, 5): False,
                 (2, 0): False, (2, 1): True, (2, 2): 'Store', (2, 3): True, (2, 4): True, (2, 5): False,
                 (3, 0): False, (3, 1): True, (3, 2): True, (3, 3): True, (3, 4): True, (3, 5): False,
                 (4, 0): False, (4, 1): True, (4, 2): True, (4, 3): True, (4, 4): True, (4, 5): False,
                 (5, 0): False, (5, 1): True, (5, 2): True, (5, 3): True, (5, 4): True, (5, 5): 'Gym'}
        expected = False
        actual = process_by_location_type(character, board)
        self.assertEqual(expected, actual)

    @patch('game.encounter_store', return_value=None)
    def test_process_by_location_type_character_location_is_store_in_level_3(self, _):
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 3, 'Potion': 0,
                     'Current Location': (2, 2),
                     'Starting Pokemon': 'Squirtle',
                     'Poke Ball': {
                         'Squirtle': {'type': 'water', 'currentHP': 40},
                         'Pichu': {'type': 'electric', 'currentHP': 30},
                         'Shinx': {'type': 'electric', 'currentHP': 30},
                         'Mareep': {'type': 'electric', 'currentHP': 30},
                         'Caterpie': {'type': 'grass', 'currentHP': 30},
                         'Weedle': {'type': 'grass', 'currentHP': 30},
                     }}
        board = {(0, 0): True, (0, 1): True, (0, 2): True, (0, 3): True, (0, 4): True, (0, 5): False,
                 (1, 0): False, (1, 1): True, (1, 2): True, (1, 3): True, (1, 4): True, (1, 5): False,
                 (2, 0): False, (2, 1): True, (2, 2): 'Store', (2, 3): True, (2, 4): True, (2, 5): False,
                 (3, 0): False, (3, 1): True, (3, 2): True, (3, 3): True, (3, 4): True, (3, 5): False,
                 (4, 0): False, (4, 1): True, (4, 2): True, (4, 3): True, (4, 4): True, (4, 5): False,
                 (5, 0): False, (5, 1): True, (5, 2): True, (5, 3): True, (5, 4): True, (5, 5): 'Gym'}
        expected = False
        actual = process_by_location_type(character, board)
        self.assertEqual(expected, actual)
