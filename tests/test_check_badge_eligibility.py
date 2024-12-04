from unittest import TestCase


from gym import check_badge_eligibility


class TestCheckBadgeEligibility(TestCase):

    def test_check_badge_eligibility_user_did_not_win_in_level_1(self):
        expected = False
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
        current_win_count = 0
        gym_badge_earned = False
        actual = check_badge_eligibility(character, current_win_count, gym_badge_earned)
        self.assertEqual(expected, actual)

    def test_check_badge_eligibility_user_won_once_in_level_1(self):
        expected = False
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
        current_win_count = 1
        gym_badge_earned = False
        actual = check_badge_eligibility(character, current_win_count, gym_badge_earned)
        self.assertEqual(expected, actual)

    def test_check_badge_eligibility_user_won_twice_in_level_1(self):
        expected = True
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
        current_win_count = 2
        gym_badge_earned = False
        actual = check_badge_eligibility(character, current_win_count, gym_badge_earned)
        self.assertEqual(expected, actual)

    def test_check_badge_eligibility_user_won_twice_in_level_2(self):
        expected = False
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 2, 'Potion': 0,
                     'Current Location': (7, 4),
                     'Starting Pokèmon': 'Wartortle',
                     'Poke Ball': {
                         'Wartortle': {'type': 'water', 'currentHP': 65},
                         'Luxray': {'type': 'electric', 'currentHP': 80},
                         'Ampharos': {'type': 'electric', 'currentHP': 80},
                         'Butterfree': {'type': 'grass', 'currentHP': 80},
                         'Beedrill': {'type': 'grass', 'currentHP': 80},
                         'Sceptile': {'type': 'grass', 'currentHP': 80},
                     }}
        current_win_count = 2
        gym_badge_earned = False
        actual = check_badge_eligibility(character, current_win_count, gym_badge_earned)
        self.assertEqual(expected, actual)

    def test_check_badge_eligibility_user_won_three_times_in_level_2(self):
        expected = True
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 2, 'Potion': 0,
                     'Current Location': (7, 4),
                     'Starting Pokèmon': 'Wartortle',
                     'Poke Ball': {
                         'Wartortle': {'type': 'water', 'currentHP': 65},
                         'Luxray': {'type': 'electric', 'currentHP': 80},
                         'Ampharos': {'type': 'electric', 'currentHP': 80},
                         'Butterfree': {'type': 'grass', 'currentHP': 80},
                         'Beedrill': {'type': 'grass', 'currentHP': 80},
                         'Sceptile': {'type': 'grass', 'currentHP': 80},
                     }}
        current_win_count = 3
        gym_badge_earned = False
        actual = check_badge_eligibility(character, current_win_count, gym_badge_earned)
        self.assertEqual(expected, actual)

    def test_check_badge_eligibility_user_won_four_times_in_level_3(self):
        expected = True
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 3, 'Potion': 0,
                     'Current Location': (9, 0),
                     'Starting Pokèmon': 'Blastoise',
                     'Poke Ball': {
                         'Blastoise': {'type': 'water', 'currentHP': 100},
                         'Luxray': {'type': 'electric', 'currentHP': 80},
                         'Ampharos': {'type': 'electric', 'currentHP': 80},
                         'Butterfree': {'type': 'grass', 'currentHP': 80},
                         'Beedrill': {'type': 'grass', 'currentHP': 80},
                         'Sceptile': {'type': 'grass', 'currentHP': 80},
                     }}
        current_win_count = 4
        gym_badge_earned = False
        actual = check_badge_eligibility(character, current_win_count, gym_badge_earned)
        self.assertEqual(expected, actual)
