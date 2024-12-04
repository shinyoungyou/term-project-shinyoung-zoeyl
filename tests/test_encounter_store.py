import io
from unittest import TestCase
from unittest.mock import patch


from store import encounter_store


class TestEncounterStore(TestCase):

    @patch('builtins.input', side_effect=['buy', 'q'])
    @patch('store.buy_potion', return_value=None)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_encounter_store_character_enters_buy(self, mock_output, _, __):
        not_expected = "Invalid option. Please try again."
        character = {
            'Character Name': 'user1',
            'Money': 30,
            'Current Level': 1,
            'Potion': 0,
            'Current Location': (5, 5),
            'Starting Pokemon': 'Squirtle',
            'Poke Ball': {
                'Squirtle': {'type': 'water', 'currentHP': 40},
                'Pichu': {'type': 'electric', 'currentHP': 30},
                'Shinx': {'type': 'electric', 'currentHP': 30},
                'Mareep': {'type': 'electric', 'currentHP': 30},
                'Caterpie': {'type': 'grass', 'currentHP': 30},
                'Weedle': {'type': 'grass', 'currentHP': 30},
            }
        }

        encounter_store(character)
        actual = mock_output.getvalue()
        self.assertNotIn(not_expected, actual)

    @patch('builtins.input', side_effect=['use', 'q'])
    @patch('store.use_potion', return_value=None)
    @patch('store.select_pokemon', return_value=('Squirtle', {'type': 'water', 'currentHP': 40}))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_encounter_store_character_enters_use(self, mock_output, _, __, ___):
        not_expected = "Invalid option. Please try again."
        character = {
            'Character Name': 'user1',
            'Money': 30,
            'Current Level': 1,
            'Potion': 0,
            'Current Location': (5, 5),
            'Starting Pokemon': 'Squirtle',
            'Poke Ball': {
                'Squirtle': {'type': 'water', 'currentHP': 40},
                'Pichu': {'type': 'electric', 'currentHP': 30},
                'Shinx': {'type': 'electric', 'currentHP': 30},
                'Mareep': {'type': 'electric', 'currentHP': 30},
                'Caterpie': {'type': 'grass', 'currentHP': 30},
                'Weedle': {'type': 'grass', 'currentHP': 30},
            }
        }

        encounter_store(character)
        actual = mock_output.getvalue()
        self.assertNotIn(not_expected, actual)

    @patch('builtins.input', side_effect=['q'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_encounter_store_character_enters_q(self, mock_output, _):
        not_expected = "Invalid option. Please try again."
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
        encounter_store(character)
        actual = mock_output.getvalue()
        self.assertNotIn(not_expected, actual)

    @patch('builtins.input', side_effect=['python', 'q'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_encounter_store_character_enters_invalid_input(self, mock_output, _):
        expected = "Invalid option. Please try again."
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
        encounter_store(character)
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)
