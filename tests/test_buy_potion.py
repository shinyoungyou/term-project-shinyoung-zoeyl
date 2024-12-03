import io
from unittest import TestCase
from unittest.mock import patch


from store import buy_potion


class TestBuyPotion(TestCase):

    @patch('builtins.input', side_effect=['2'])  # Added 'q' to terminate the loop
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_buy_potion_character_has_25_dollars_and_wants_to_buy_2_potions(self, mock_output, _):
        expected = "Purchase successful! Your remaining budget is $5"
        character = {'Character Name': 'user1', 'Money': 25, 'Current Level': 1, 'Potion': 0,
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
        buy_potion(character)
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=['3'])  # Added 'q' to terminate the loop
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_buy_potion_character_has_25_dollars_and_wants_to_buy_3_potions(self, mock_output, _):
        expected = "You can't buy with your current budget."
        character = {'Character Name': 'user1', 'Money': 25, 'Current Level': 1, 'Potion': 0,
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
        buy_potion(character)
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=['3'])  # Added 'q' to terminate the loop
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_buy_potion_character_has_30_dollars_and_wants_to_buy_3_potions(self, mock_output, _):
        expected = "Purchase successful! Your remaining budget is $0"
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
        buy_potion(character)
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=['4'])  # Added 'q' to terminate the loop
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_buy_potion_character_has_30_dollars_and_wants_to_buy_4_potions(self, mock_output, _):
        expected = "You can't buy with your current budget."
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
        buy_potion(character)
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=['0', '1'])  # Added 'q' to terminate the loop
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_buy_potion_character_has_30_dollars_and_wants_to_buy_0_potions(self, mock_output, _):
        expected = "You need to buy at least one potion."
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
        buy_potion(character)
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)
