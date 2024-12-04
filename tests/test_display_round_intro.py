import io
from unittest import TestCase
from unittest.mock import patch

from gym import display_round_intro


class TestDisplayRoundIntro(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_round_intro_gym_round_is_1(self, mock_output):
        gym_leader_pokemon = ('Pidove', {'type': 'flying', 'currentHP': 30})
        selected_pokemon = ('Squirtle', {'type': 'water', 'currentHP': 40})
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
        expected = ("\n❗️Round 1 ❗\n\nEvent pokemon status: Pidove(HP: 30)\n"
                    "\nuser1's pokemon status: Squirtle(HP: 40)\n\n")
        display_round_intro(1, gym_leader_pokemon, selected_pokemon, character)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_round_intro_gym_round_is_2(self, mock_output):
        gym_leader_pokemon = ('Pidove', {'type': 'flying', 'currentHP': 20})
        selected_pokemon = ('Squirtle', {'type': 'water', 'currentHP': 15})
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 1, 'Potion': 0,
                     'Current Location': (5, 5),
                     'Starting Pokèmon': 'Squirtle',
                     'Poke Ball': {
                         'Squirtle': {'type': 'water', 'currentHP': 15},
                         'Pichu': {'type': 'electric', 'currentHP': 30},
                         'Shinx': {'type': 'electric', 'currentHP': 30},
                         'Mareep': {'type': 'electric', 'currentHP': 30},
                         'Caterpie': {'type': 'grass', 'currentHP': 30},
                         'Weedle': {'type': 'grass', 'currentHP': 30},
                     }}
        expected = ("\n❗️Round 2 ❗\n\nEvent pokemon status: Pidove(HP: 20)\n"
                    "\nuser1's pokemon status: Squirtle(HP: 15)\n\n")
        display_round_intro(2, gym_leader_pokemon, selected_pokemon, character)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_round_intro_gym_round_is_3(self, mock_output):
        gym_leader_pokemon = ('Pidove', {'type': 'flying', 'currentHP': 2})
        selected_pokemon = ('Squirtle', {'type': 'water', 'currentHP': 1})
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 1, 'Potion': 0,
                     'Current Location': (5, 5),
                     'Starting Pokèmon': 'Squirtle',
                     'Poke Ball': {
                         'Squirtle': {'type': 'water', 'currentHP': 1},
                         'Pichu': {'type': 'electric', 'currentHP': 30},
                         'Shinx': {'type': 'electric', 'currentHP': 30},
                         'Mareep': {'type': 'electric', 'currentHP': 30},
                         'Caterpie': {'type': 'grass', 'currentHP': 30},
                         'Weedle': {'type': 'grass', 'currentHP': 30},
                     }}
        expected = ("\n❗️Round 3 ❗\n\nEvent pokemon status: Pidove(HP: 2)\n"
                    "\nuser1's pokemon status: Squirtle(HP: 1)\n\n")
        display_round_intro(3, gym_leader_pokemon, selected_pokemon, character)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
