from unittest import TestCase
from unittest.mock import patch

from gym import handle_user_choice


class TestHandleUserChoice(TestCase):

    @patch('gym.fight', return_value=False)
    def test_handle_user_choice_user_chose_to_fight_and_didnt_defeat_gym_leader_pokemon(self, mock_fight):
        user_choice = "Fight"
        process_result = False
        selected_pokemon = ('Squirtle', {'type': 'water', 'currentHP': 40})
        gym_leader_pokemon = ('Weedle', {'type': 'grass', 'currentHP': 30})
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 1, 'Potion': 0,
                     'Current Location': (5, 5),
                     'Starting Pokémon': 'Squirtle',
                     'Poke Ball': {
                         'Squirtle': {'type': 'water', 'currentHP': 40},
                         'Pichu': {'type': 'electric', 'currentHP': 30},
                         'Shinx': {'type': 'electric', 'currentHP': 30},
                         'Mareep': {'type': 'electric', 'currentHP': 30},
                         'Caterpie': {'type': 'grass', 'currentHP': 30},
                         'Weedle': {'type': 'grass', 'currentHP': 30},
                     }}
        expected = (mock_fight.return_value, selected_pokemon, False)
        actual = handle_user_choice(user_choice, process_result, selected_pokemon, gym_leader_pokemon, character)
        self.assertEqual(expected, actual)

    @patch('gym.fight', return_value=True)
    def test_handle_user_choice_user_chose_to_fight_and_defeated_gym_leader_pokemon(self, mock_fight):
        user_choice = "Fight"
        process_result = False
        selected_pokemon = ('Squirtle', {'type': 'water', 'currentHP': 40})
        gym_leader_pokemon = ('Weedle', {'type': 'grass', 'currentHP': 30})
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 1, 'Potion': 0,
                     'Current Location': (5, 5),
                     'Starting Pokémon': 'Squirtle',
                     'Poke Ball': {
                         'Squirtle': {'type': 'water', 'currentHP': 40},
                         'Pichu': {'type': 'electric', 'currentHP': 30},
                         'Shinx': {'type': 'electric', 'currentHP': 30},
                         'Mareep': {'type': 'electric', 'currentHP': 30},
                         'Caterpie': {'type': 'grass', 'currentHP': 30},
                         'Weedle': {'type': 'grass', 'currentHP': 30},
                     }}
        expected = (mock_fight.return_value, selected_pokemon, False)
        actual = handle_user_choice(user_choice, process_result, selected_pokemon, gym_leader_pokemon, character)
        self.assertEqual(expected, actual)

    @patch('gym.change_pokemon', return_value=('Pichu', {'type': 'electric', 'currentHP': 30}))
    def test_handle_user_choice_user_chose_to_change_pokemon(self, mock_change_pokemon):
        user_choice = "Change Pokemon"
        process_result = False
        selected_pokemon = ('Squirtle', {'type': 'water', 'currentHP': 40})
        gym_leader_pokemon = ('Weedle', {'type': 'grass', 'currentHP': 30})
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 1, 'Potion': 0,
                     'Current Location': (5, 5),
                     'Starting Pokémon': 'Squirtle',
                     'Poke Ball': {
                         'Squirtle': {'type': 'water', 'currentHP': 40},
                         'Pichu': {'type': 'electric', 'currentHP': 30},
                         'Shinx': {'type': 'electric', 'currentHP': 30},
                         'Mareep': {'type': 'electric', 'currentHP': 30},
                         'Caterpie': {'type': 'grass', 'currentHP': 30},
                         'Weedle': {'type': 'grass', 'currentHP': 30},
                     }}
        expected = (process_result, mock_change_pokemon.return_value, False)
        actual = handle_user_choice(user_choice, process_result, selected_pokemon, gym_leader_pokemon, character)
        self.assertEqual(expected, actual)

    def test_handle_user_choice_user_chose_to_run_away(self):
        user_choice = "Run Away"
        process_result = False
        selected_pokemon = ('Squirtle', {'type': 'water', 'currentHP': 40})
        gym_leader_pokemon = ('Weedle', {'type': 'grass', 'currentHP': 30})
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 1, 'Potion': 0,
                     'Current Location': (5, 5),
                     'Starting Pokémon': 'Squirtle',
                     'Poke Ball': {
                         'Squirtle': {'type': 'water', 'currentHP': 40},
                         'Pichu': {'type': 'electric', 'currentHP': 30},
                         'Shinx': {'type': 'electric', 'currentHP': 30},
                         'Mareep': {'type': 'electric', 'currentHP': 30},
                         'Caterpie': {'type': 'grass', 'currentHP': 30},
                         'Weedle': {'type': 'grass', 'currentHP': 30},
                     }}
        expected = (process_result, selected_pokemon, True)
        actual = handle_user_choice(user_choice, process_result, selected_pokemon, gym_leader_pokemon, character)
        self.assertEqual(expected, actual)
