import io
from unittest import TestCase
from unittest.mock import patch

from store import use_potion


class TestBuyPotion(TestCase):

    @patch('builtins.input', side_effect=['y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_use_potion_character_has_2_potions_and_wants_to_use_potion(self, mock_output, _):
        expected_remaining_potion = 1
        character = {'Character Name': 'user1', 'Money': 25, 'Current Level': 1, 'Potion': 2,
                     'Current Location': (5, 5),
                     'Starting Pokemon': 'Squirtle',
                     'Poke Ball': {
                         'Squirtle': {'type': 'water', 'currentHP': 10},
                         'Pichu': {'type': 'electric', 'currentHP': 30},
                         'Shinx': {'type': 'electric', 'currentHP': 30},
                         'Mareep': {'type': 'electric', 'currentHP': 30},
                         'Caterpie': {'type': 'grass', 'currentHP': 30},
                         'Weedle': {'type': 'grass', 'currentHP': 30},
                     }}
        character_pokemon = ('Squirtle', {'type': 'water', 'currentHP': 10})
        use_potion(character, character_pokemon)
        actual_remaining_potion = character['Potion']
        self.assertEqual(expected_remaining_potion, actual_remaining_potion)

    @patch('builtins.input', side_effect=['n'])
    def test_use_potion_character_has_2_potions_but_does_not_want_to_use_potion(self, _):
        expected_remaining_potion = 2
        character = {'Character Name': 'user1', 'Money': 25, 'Current Level': 1, 'Potion': 2,
                     'Current Location': (5, 5),
                     'Starting Pokemon': 'Squirtle',
                     'Poke Ball': {
                         'Squirtle': {'type': 'water', 'currentHP': 10},
                         'Pichu': {'type': 'electric', 'currentHP': 30},
                     }}
        character_pokemon = ('Squirtle', {'type': 'water', 'currentHP': 10})
        use_potion(character, character_pokemon)
        actual_remaining_potion = character['Potion']
        self.assertEqual(expected_remaining_potion, actual_remaining_potion)

    @patch('builtins.input', side_effect=['y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_use_potion_character_has_no_potions_but_wants_to_use_potion(self, mock_output, _):
        expected_remaining_potion = 0
        character = {'Character Name': 'user1', 'Money': 25, 'Current Level': 1, 'Potion': 0,
                     'Current Location': (5, 5),
                     'Starting Pokemon': 'Squirtle',
                     'Poke Ball': {
                         'Squirtle': {'type': 'water', 'currentHP': 10},
                         'Pichu': {'type': 'electric', 'currentHP': 30},
                         'Shinx': {'type': 'electric', 'currentHP': 30},
                         'Mareep': {'type': 'electric', 'currentHP': 30},
                         'Caterpie': {'type': 'grass', 'currentHP': 30},
                         'Weedle': {'type': 'grass', 'currentHP': 30},
                     }}
        character_pokemon = ('Squirtle', {'type': 'water', 'currentHP': 10})
        use_potion(character, character_pokemon)
        actual_remaining_potion = character['Potion']
        self.assertEqual(expected_remaining_potion, actual_remaining_potion)

    @patch('builtins.input', side_effect=['invalid', 'y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_use_potion_invalid_input_entered(self, mock_output, _):
        expected = ('\nYou have 2 potion(s)!'
                    '\nSquirtle has 10 HP.\n'
                    '\ninvalid is not a valid option\n'
                    '\nSquirtle restored HP!'
                    '\nSquirtle(HP: 25)'
                    '\n1 potion(s) left!\n')
        character = {'Character Name': 'user1', 'Money': 25, 'Current Level': 1, 'Potion': 2,
                     'Current Location': (5, 5),
                     'Starting Pokemon': 'Squirtle',
                     'Poke Ball': {
                         'Squirtle': {'type': 'water', 'currentHP': 10},
                         'Pichu': {'type': 'electric', 'currentHP': 30},
                     }}
        character_pokemon = ('Squirtle', {'type': 'water', 'currentHP': 10})
        use_potion(character, character_pokemon)
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=['y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_use_potion_pokemon_hp_is_already_full(self, mock_output, _):
        expected_restored_hp = 40
        character = {'Character Name': 'user1', 'Money': 25, 'Current Level': 1, 'Potion': 1,
                     'Current Location': (5, 5),
                     'Starting Pokemon': 'Squirtle',
                     'Poke Ball': {
                         'Squirtle': {'type': 'water', 'currentHP': 40},
                         'Pichu': {'type': 'electric', 'currentHP': 30},
                     }}
        character_pokemon = ('Squirtle', {'type': 'water', 'currentHP': 40})
        use_potion(character, character_pokemon)
        actual_restored_hp = character_pokemon[1]['currentHP']
        self.assertEqual(expected_restored_hp, actual_restored_hp)

    @patch('builtins.input', side_effect=['y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_use_potion_pokemon_hp_is_almost_full(self, mock_output, _):
        expected_restored_hp = 40
        character = {'Character Name': 'user1', 'Money': 25, 'Current Level': 1, 'Potion': 1,
                     'Current Location': (5, 5),
                     'Starting Pokemon': 'Squirtle',
                     'Poke Ball': {
                         'Squirtle': {'type': 'water', 'currentHP': 35},
                         'Pichu': {'type': 'electric', 'currentHP': 30},
                     }}
        character_pokemon = ('Squirtle', {'type': 'water', 'currentHP': 35})
        use_potion(character, character_pokemon)
        actual_restored_hp = character_pokemon[1]['currentHP']
        self.assertEqual(expected_restored_hp, actual_restored_hp)
