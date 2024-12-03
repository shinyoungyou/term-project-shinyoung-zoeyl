from unittest import TestCase

from board import check_if_current_location_is_special


class TestCheckIfCurrentLocationIsSpecial(TestCase):

    def test_check_if_current_location_is_special_character_at_start(self):
        expected = False
        board = {(0, 0): True, (0, 1): True, (0, 2): True, (0, 3): True, (0, 4): True, (0, 5): False,
                 (1, 0): False, (1, 1): True, (1, 2): True, (1, 3): True, (1, 4): True, (1, 5): False,
                 (2, 0): False, (2, 1): True, (2, 2): 'Store', (2, 3): True, (2, 4): True, (2, 5): False,
                 (3, 0): False, (3, 1): True, (3, 2): True, (3, 3): True, (3, 4): True, (3, 5): False,
                 (4, 0): False, (4, 1): True, (4, 2): True, (4, 3): True, (4, 4): True, (4, 5): False,
                 (5, 0): False, (5, 1): True, (5, 2): True, (5, 3): True, (5, 4): True, (5, 5): 'Gym'}
        character = {"Current Location": (0, 0)}
        actual = check_if_current_location_is_special(board, character)
        self.assertEqual(expected, actual)

    def test_display_current_location_character_in_the_middle(self):
        expected = False
        board = {(0, 0): True, (0, 1): True, (0, 2): True, (0, 3): True, (0, 4): True, (0, 5): False,
                 (1, 0): False, (1, 1): True, (1, 2): True, (1, 3): True, (1, 4): True, (1, 5): False,
                 (2, 0): False, (2, 1): True, (2, 2): 'Store', (2, 3): True, (2, 4): True, (2, 5): False,
                 (3, 0): False, (3, 1): True, (3, 2): True, (3, 3): True, (3, 4): True, (3, 5): False,
                 (4, 0): False, (4, 1): True, (4, 2): True, (4, 3): True, (4, 4): True, (4, 5): False,
                 (5, 0): False, (5, 1): True, (5, 2): True, (5, 3): True, (5, 4): True, (5, 5): 'Gym'}
        character = {"Current Location": (3, 2)}
        actual = check_if_current_location_is_special(board, character)
        self.assertEqual(expected, actual)

    def test_display_current_location_character_at_top_right_corner(self):
        expected = False
        board = {(0, 0): True, (0, 1): True, (0, 2): True, (0, 3): True, (0, 4): True, (0, 5): False,
                 (1, 0): False, (1, 1): True, (1, 2): True, (1, 3): True, (1, 4): True, (1, 5): False,
                 (2, 0): False, (2, 1): True, (2, 2): 'Store', (2, 3): True, (2, 4): True, (2, 5): False,
                 (3, 0): False, (3, 1): True, (3, 2): True, (3, 3): True, (3, 4): True, (3, 5): False,
                 (4, 0): False, (4, 1): True, (4, 2): True, (4, 3): True, (4, 4): True, (4, 5): False,
                 (5, 0): False, (5, 1): True, (5, 2): True, (5, 3): True, (5, 4): True, (5, 5): 'Gym'}
        character = {"Current Location": (0, 4)}
        actual = check_if_current_location_is_special(board, character)
        self.assertEqual(expected, actual)

    def test_display_current_location_character_at_bottom_left_corner(self):
        expected = False
        board = {(0, 0): True, (0, 1): True, (0, 2): True, (0, 3): True, (0, 4): True, (0, 5): False,
                 (1, 0): False, (1, 1): True, (1, 2): True, (1, 3): True, (1, 4): True, (1, 5): False,
                 (2, 0): False, (2, 1): True, (2, 2): 'Store', (2, 3): True, (2, 4): True, (2, 5): False,
                 (3, 0): False, (3, 1): True, (3, 2): True, (3, 3): True, (3, 4): True, (3, 5): False,
                 (4, 0): False, (4, 1): True, (4, 2): True, (4, 3): True, (4, 4): True, (4, 5): False,
                 (5, 0): False, (5, 1): True, (5, 2): True, (5, 3): True, (5, 4): True, (5, 5): 'Gym'}
        character = {"Current Location": (5, 1)}
        actual = check_if_current_location_is_special(board, character)
        self.assertEqual(expected, actual)

    def test_check_if_current_location_is_special_character_at_store(self):
        expected = True
        board = {(0, 0): True, (0, 1): True, (0, 2): True, (0, 3): True, (0, 4): True, (0, 5): False,
                 (1, 0): False, (1, 1): True, (1, 2): True, (1, 3): True, (1, 4): True, (1, 5): False,
                 (2, 0): False, (2, 1): True, (2, 2): 'Store', (2, 3): True, (2, 4): True, (2, 5): False,
                 (3, 0): False, (3, 1): True, (3, 2): True, (3, 3): True, (3, 4): True, (3, 5): False,
                 (4, 0): False, (4, 1): True, (4, 2): True, (4, 3): True, (4, 4): True, (4, 5): False,
                 (5, 0): False, (5, 1): True, (5, 2): True, (5, 3): True, (5, 4): True, (5, 5): 'Gym'}
        character = {"Current Location": (2, 2)}
        actual = check_if_current_location_is_special(board, character)
        self.assertEqual(expected, actual)

    def test_check_if_current_location_is_special_character_at_gym(self):
        expected = True
        board = {(0, 0): True, (0, 1): True, (0, 2): True, (0, 3): True, (0, 4): True, (0, 5): False,
                 (1, 0): False, (1, 1): True, (1, 2): True, (1, 3): True, (1, 4): True, (1, 5): False,
                 (2, 0): False, (2, 1): True, (2, 2): 'Store', (2, 3): True, (2, 4): True, (2, 5): False,
                 (3, 0): False, (3, 1): True, (3, 2): True, (3, 3): True, (3, 4): True, (3, 5): False,
                 (4, 0): False, (4, 1): True, (4, 2): True, (4, 3): True, (4, 4): True, (4, 5): False,
                 (5, 0): False, (5, 1): True, (5, 2): True, (5, 3): True, (5, 4): True, (5, 5): 'Gym'}
        character = {"Current Location": (5, 5)}
        actual = check_if_current_location_is_special(board, character)
        self.assertEqual(expected, actual)

    def test_check_if_current_location_is_special_character_at_inaccessible_area(self):
        expected = False
        board = {(0, 0): True, (0, 1): True, (0, 2): True, (0, 3): True, (0, 4): True, (0, 5): False,
                 (1, 0): False, (1, 1): True, (1, 2): True, (1, 3): True, (1, 4): True, (1, 5): False,
                 (2, 0): False, (2, 1): True, (2, 2): 'Store', (2, 3): True, (2, 4): True, (2, 5): False,
                 (3, 0): False, (3, 1): True, (3, 2): True, (3, 3): True, (3, 4): True, (3, 5): False,
                 (4, 0): False, (4, 1): True, (4, 2): True, (4, 3): True, (4, 4): True, (4, 5): False,
                 (5, 0): False, (5, 1): True, (5, 2): True, (5, 3): True, (5, 4): True, (5, 5): 'Gym'}
        character = {"Current Location": (1, 0)}
        actual = check_if_current_location_is_special(board, character)
        self.assertEqual(expected, actual)
