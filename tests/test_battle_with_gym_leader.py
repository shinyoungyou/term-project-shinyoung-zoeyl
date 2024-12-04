import io
from unittest import TestCase
from unittest.mock import patch


from gym import battle_with_gym_leader


class TestBattleWithGymLeader(TestCase):

    @patch('gym.select_event_option', return_value="Fight")
    @patch('gym.handle_user_choice',
           return_value=(False, ('Squirtle', {'type': 'water', 'currentHP': 40}), False))
    @patch('gym.win_the_round',
           return_value=(2, True, 3, ('Pidove', {'type': 'flying', 'currentHP': 30})))
    def test_battle_with_gym_leader_user_won(self, _, __, ___):
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
            },
        }
        gym_badge_earned = False
        expected = True
        actual = battle_with_gym_leader(character, gym_badge_earned)
        self.assertEqual(expected, actual)

    @patch('gym.select_event_option', return_value="Fight")
    @patch('gym.handle_user_choice',
           return_value=(True, ('Squirtle', {'type': 'water', 'currentHP': 40}), False))
    @patch('gym.check_if_alive_when_lost_the_round', return_value=(
            False, ('Squirtle', {'type': 'water', 'currentHP': 40}), 1, True))
    def test_battle_with_gym_leader_user_lost(self, _, __, ___):
        character = {
            'Character Name': 'user1',
            'Money': 30,
            'Current Level': 1,
            'Potion': 0,
            'Current Location': (5, 5),
            'Starting Pokemon': 'Squirtle',
            'Poke Ball': {
                'Squirtle': {'type': 'water', 'currentHP': 10},
                'Pichu': {'type': 'electric', 'currentHP': 0},
                'Shinx': {'type': 'electric', 'currentHP': 0},
                'Mareep': {'type': 'electric', 'currentHP': 0},
                'Caterpie': {'type': 'grass', 'currentHP': 0},
                'Weedle': {'type': 'grass', 'currentHP': 0},
            },
        }
        gym_badge_earned = False
        expected = False
        actual = battle_with_gym_leader(character, gym_badge_earned)
        self.assertEqual(expected, actual)
