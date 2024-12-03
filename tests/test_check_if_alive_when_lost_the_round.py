from unittest import TestCase
from unittest.mock import patch


from gym import check_if_alive_when_lost_the_round


class TestCheckIfAliveWhenLostTheRound(TestCase):

    @patch('gym.get_attacked', return_value=False)
    @patch('gym.take_out_pokemon', return_value=('Shinx', {'type': 'electric', 'currentHP': 30}))
    def test_check_if_alive_when_lost_the_round_character_pokemon_fainted_but_alive(
            self, mock_take_out_pokemon, mock_get_attacked):
        gym_leader_pokemon = ('Weedle', {'type': 'grass', 'currentHP': 30})
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 1, 'Potion': 0,
                     'Current Location': (5, 5),
                     'Starting Pokemon': 'Squirtle',
                     'Poke Ball': {
                         'Squirtle': {'type': 'water', 'currentHP': 0},
                         'Pichu': {'type': 'electric', 'currentHP': 30},
                         'Shinx': {'type': 'electric', 'currentHP': 30},
                         'Mareep': {'type': 'electric', 'currentHP': 30},
                         'Caterpie': {'type': 'grass', 'currentHP': 30},
                         'Weedle': {'type': 'grass', 'currentHP': 30},
                     }}
        selected_pokemon = ('Squirtle', {'type': 'water', 'currentHP': 0})
        gym_round = 1
        expected = (mock_get_attacked.return_value, mock_take_out_pokemon.return_value, gym_round + 1, False)
        actual = check_if_alive_when_lost_the_round(gym_leader_pokemon, character, selected_pokemon, gym_round)
        self.assertEqual(expected, actual)

    @patch('gym.get_attacked', return_value=False)
    def test_check_if_alive_when_lost_the_round_character_pokemon_fainted_and_not_alive(self, mock_get_attacked):
        gym_leader_pokemon = ('Weedle', {'type': 'grass', 'currentHP': 30})
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 1, 'Potion': 0,
                     'Current Location': (5, 5),
                     'Starting Pokemon': 'Squirtle',
                     'Poke Ball': {
                         'Squirtle': {'type': 'water', 'currentHP': 0},
                         'Pichu': {'type': 'electric', 'currentHP': 0},
                         'Shinx': {'type': 'electric', 'currentHP': 0},
                         'Mareep': {'type': 'electric', 'currentHP': 0},
                         'Caterpie': {'type': 'grass', 'currentHP': 0},
                         'Weedle': {'type': 'grass', 'currentHP': 0},
                     }}
        selected_pokemon = ('Squirtle', {'type': 'water', 'currentHP': 0})
        gym_round = 1
        expected = (mock_get_attacked.return_value, selected_pokemon, gym_round, True)
        actual = check_if_alive_when_lost_the_round(gym_leader_pokemon, character, selected_pokemon, gym_round)
        self.assertEqual(expected, actual)

    @patch('gym.get_attacked', return_value=True)
    def test_check_if_alive_when_lost_the_round_character_pokemon_didnt_fainted(self, mock_get_attacked):
        gym_leader_pokemon = ('Weedle', {'type': 'grass', 'currentHP': 30})
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 1, 'Potion': 0,
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
        selected_pokemon = ('Squirtle', {'type': 'water', 'currentHP': 10})
        gym_round = 1
        expected = (mock_get_attacked.return_value, selected_pokemon, gym_round, False)
        actual = check_if_alive_when_lost_the_round(gym_leader_pokemon, character, selected_pokemon, gym_round)
        self.assertEqual(expected, actual)
