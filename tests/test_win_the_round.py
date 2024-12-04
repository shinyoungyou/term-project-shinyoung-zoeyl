from unittest import TestCase
from unittest.mock import patch

from gym import win_the_round


class TestWinTheRound(TestCase):

    @patch('gym.get_event_pokemon', return_value=('Horsea', {'type': 'water', 'currentHP': 30}))
    def test_win_the_round_user_wins_once_in_gym_round_1_when_level_1(self, mock_get_event_pokemon):
        current_win_count = 0
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
        gym_badge_earned = False
        gym_round = 1
        expected = (current_win_count + 1, gym_badge_earned, gym_round + 1, mock_get_event_pokemon.return_value)
        actual = win_the_round(current_win_count, character, gym_badge_earned, gym_round)
        self.assertEqual(expected, actual)

    @patch('gym.get_event_pokemon', return_value=('Horsea', {'type': 'water', 'currentHP': 30}))
    def test_win_the_round_user_wins_twice_in_gym_round_2_when_level_1(self, mock_get_event_pokemon):
        current_win_count = 1
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
        gym_badge_earned = False
        gym_round = 2
        expected = (current_win_count + 1, True, gym_round + 1, mock_get_event_pokemon.return_value)
        actual = win_the_round(current_win_count, character, gym_badge_earned, gym_round)
        self.assertEqual(expected, actual)

    @patch('gym.get_event_pokemon', return_value=('Horsea', {'type': 'water', 'currentHP': 30}))
    def test_win_the_round_user_wins_twice_in_gym_round_3_when_level_1(self, mock_get_event_pokemon):
        current_win_count = 1
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
        gym_badge_earned = False
        gym_round = 3
        expected = (current_win_count + 1, True, gym_round + 1, mock_get_event_pokemon.return_value)
        actual = win_the_round(current_win_count, character, gym_badge_earned, gym_round)
        self.assertEqual(expected, actual)

    @patch('gym.get_event_pokemon', return_value=('Horsea', {'type': 'water', 'currentHP': 30}))
    def test_win_the_round_user_wins_once_in_gym_round_2_when_level_2(self, mock_get_event_pokemon):
        current_win_count = 0
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 2, 'Potion': 0,
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
        gym_badge_earned = False
        gym_round = 2
        expected = (current_win_count + 1, gym_badge_earned, gym_round + 1, mock_get_event_pokemon.return_value)
        actual = win_the_round(current_win_count, character, gym_badge_earned, gym_round)
        self.assertEqual(expected, actual)

    @patch('gym.get_event_pokemon', return_value=('Horsea', {'type': 'water', 'currentHP': 30}))
    def test_win_the_round_user_wins_twice_in_gym_round_2_when_level_2(self, mock_get_event_pokemon):
        current_win_count = 1
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 2, 'Potion': 0,
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
        gym_badge_earned = False
        gym_round = 2
        expected = (current_win_count + 1, gym_badge_earned, gym_round + 1, mock_get_event_pokemon.return_value)
        actual = win_the_round(current_win_count, character, gym_badge_earned, gym_round)
        self.assertEqual(expected, actual)

    @patch('gym.get_event_pokemon', return_value=('Horsea', {'type': 'water', 'currentHP': 30}))
    def test_win_the_round_user_wins_three_times_in_gym_round_3_when_level_2(self, mock_get_event_pokemon):
        current_win_count = 2
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 2, 'Potion': 0,
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
        gym_badge_earned = False
        gym_round = 3
        expected = (current_win_count + 1, True, gym_round + 1, mock_get_event_pokemon.return_value)
        actual = win_the_round(current_win_count, character, gym_badge_earned, gym_round)
        self.assertEqual(expected, actual)

    @patch('gym.get_event_pokemon', return_value=('Horsea', {'type': 'water', 'currentHP': 30}))
    def test_win_the_round_user_wins_once_in_gym_round_4_when_level_3(self, mock_get_event_pokemon):
        current_win_count = 0
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 3, 'Potion': 0,
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
        gym_badge_earned = False
        gym_round = 4
        expected = (current_win_count + 1, gym_badge_earned, gym_round + 1, mock_get_event_pokemon.return_value)
        actual = win_the_round(current_win_count, character, gym_badge_earned, gym_round)
        self.assertEqual(expected, actual)

    @patch('gym.get_event_pokemon', return_value=('Horsea', {'type': 'water', 'currentHP': 30}))
    def test_win_the_round_user_wins_twice_in_gym_round_4_when_level_3(self, mock_get_event_pokemon):
        current_win_count = 1
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 3, 'Potion': 0,
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
        gym_badge_earned = False
        gym_round = 4
        expected = (current_win_count + 1, gym_badge_earned, gym_round + 1, mock_get_event_pokemon.return_value)
        actual = win_the_round(current_win_count, character, gym_badge_earned, gym_round)
        self.assertEqual(expected, actual)

    @patch('gym.get_event_pokemon', return_value=('Horsea', {'type': 'water', 'currentHP': 30}))
    def test_win_the_round_user_wins_three_times_in_gym_round_4_when_level_3(self, mock_get_event_pokemon):
        current_win_count = 2
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 3, 'Potion': 0,
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
        gym_badge_earned = False
        gym_round = 4
        expected = (current_win_count + 1, gym_badge_earned, gym_round + 1, mock_get_event_pokemon.return_value)
        actual = win_the_round(current_win_count, character, gym_badge_earned, gym_round)
        self.assertEqual(expected, actual)

    @patch('gym.get_event_pokemon', return_value=('Horsea', {'type': 'water', 'currentHP': 30}))
    def test_win_the_round_user_wins_four_times_in_gym_round_4_when_level_3(self, mock_get_event_pokemon):
        current_win_count = 3
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 3, 'Potion': 0,
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
        gym_badge_earned = False
        gym_round = 4
        expected = (current_win_count + 1, True, gym_round + 1, mock_get_event_pokemon.return_value)
        actual = win_the_round(current_win_count, character, gym_badge_earned, gym_round)
        self.assertEqual(expected, actual)

    @patch('gym.get_event_pokemon', return_value=('Horsea', {'type': 'water', 'currentHP': 30}))
    def test_win_the_round_user_wins_four_times_in_gym_round_5_when_level_3(self, mock_get_event_pokemon):
        current_win_count = 3
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 3, 'Potion': 0,
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
        gym_badge_earned = False
        gym_round = 5
        expected = (current_win_count + 1, True, gym_round + 1, mock_get_event_pokemon.return_value)
        actual = win_the_round(current_win_count, character, gym_badge_earned, gym_round)
        self.assertEqual(expected, actual)
