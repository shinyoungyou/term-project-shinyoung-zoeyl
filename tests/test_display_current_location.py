import io
from unittest import TestCase
from unittest.mock import patch

from board import display_current_location


class TestDisplayCurrentLocation(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_display_current_location_character_at_start(self, mock_output):
        expected = ('[🤠][  ][  ][  ][  ]    '
                    '\n    [  ][  ][  ][  ]    '
                    '\n    [  ][💊][  ][  ]    '
                    '\n    [  ][  ][  ][  ]    '
                    '\n    [  ][  ][  ][  ]    '
                    '\n    [  ][  ][  ][  ][🥊]\n')
        board = {(0, 0): True, (0, 1): True, (0, 2): True, (0, 3): True, (0, 4): True, (0, 5): False,
                 (1, 0): False, (1, 1): True, (1, 2): True, (1, 3): True, (1, 4): True, (1, 5): False,
                 (2, 0): False, (2, 1): True, (2, 2): 'Store', (2, 3): True, (2, 4): True, (2, 5): False,
                 (3, 0): False, (3, 1): True, (3, 2): True, (3, 3): True, (3, 4): True, (3, 5): False,
                 (4, 0): False, (4, 1): True, (4, 2): True, (4, 3): True, (4, 4): True, (4, 5): False,
                 (5, 0): False, (5, 1): True, (5, 2): True, (5, 3): True, (5, 4): True, (5, 5): 'Gym'}
        character = {"Current Location": (0, 0)}
        display_current_location(board, character, 6, 6)
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_display_current_location_character_at_store(self, mock_output):
        expected = ('[  ][  ][  ][  ][  ]    '
                    '\n    [  ][  ][  ][  ]    '
                    '\n    [  ][🤠][  ][  ]    '
                    '\n    [  ][  ][  ][  ]    '
                    '\n    [  ][  ][  ][  ]    '
                    '\n    [  ][  ][  ][  ][🥊]\n')
        board = {(0, 0): True, (0, 1): True, (0, 2): True, (0, 3): True, (0, 4): True, (0, 5): False,
                 (1, 0): False, (1, 1): True, (1, 2): True, (1, 3): True, (1, 4): True, (1, 5): False,
                 (2, 0): False, (2, 1): True, (2, 2): 'Store', (2, 3): True, (2, 4): True, (2, 5): False,
                 (3, 0): False, (3, 1): True, (3, 2): True, (3, 3): True, (3, 4): True, (3, 5): False,
                 (4, 0): False, (4, 1): True, (4, 2): True, (4, 3): True, (4, 4): True, (4, 5): False,
                 (5, 0): False, (5, 1): True, (5, 2): True, (5, 3): True, (5, 4): True, (5, 5): 'Gym'}
        character = {"Current Location": (2, 2)}
        display_current_location(board, character, 6, 6)
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_display_current_location_character_at_gym(self, mock_output):
        expected = ('[  ][  ][  ][  ][  ]    '
                    '\n    [  ][  ][  ][  ]    '
                    '\n    [  ][💊][  ][  ]    '
                    '\n    [  ][  ][  ][  ]    '
                    '\n    [  ][  ][  ][  ]    '
                    '\n    [  ][  ][  ][  ][🤠]\n')
        board = {(0, 0): True, (0, 1): True, (0, 2): True, (0, 3): True, (0, 4): True, (0, 5): False,
                 (1, 0): False, (1, 1): True, (1, 2): True, (1, 3): True, (1, 4): True, (1, 5): False,
                 (2, 0): False, (2, 1): True, (2, 2): 'Store', (2, 3): True, (2, 4): True, (2, 5): False,
                 (3, 0): False, (3, 1): True, (3, 2): True, (3, 3): True, (3, 4): True, (3, 5): False,
                 (4, 0): False, (4, 1): True, (4, 2): True, (4, 3): True, (4, 4): True, (4, 5): False,
                 (5, 0): False, (5, 1): True, (5, 2): True, (5, 3): True, (5, 4): True, (5, 5): 'Gym'}
        character = {"Current Location": (5, 5)}
        display_current_location(board, character, 6, 6)
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_display_current_location_character_in_the_middle(self, mock_output):
        expected = ('[  ][  ][  ][  ][  ]    '
                    '\n    [  ][  ][  ][  ]    '
                    '\n    [  ][💊][  ][  ]    '
                    '\n    [  ][🤠][  ][  ]    '
                    '\n    [  ][  ][  ][  ]    '
                    '\n    [  ][  ][  ][  ][🥊]\n')
        board = {(0, 0): True, (0, 1): True, (0, 2): True, (0, 3): True, (0, 4): True, (0, 5): False,
                 (1, 0): False, (1, 1): True, (1, 2): True, (1, 3): True, (1, 4): True, (1, 5): False,
                 (2, 0): False, (2, 1): True, (2, 2): 'Store', (2, 3): True, (2, 4): True, (2, 5): False,
                 (3, 0): False, (3, 1): True, (3, 2): True, (3, 3): True, (3, 4): True, (3, 5): False,
                 (4, 0): False, (4, 1): True, (4, 2): True, (4, 3): True, (4, 4): True, (4, 5): False,
                 (5, 0): False, (5, 1): True, (5, 2): True, (5, 3): True, (5, 4): True, (5, 5): 'Gym'}
        character = {"Current Location": (3, 2)}
        display_current_location(board, character, 6, 6)
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_display_current_location_character_at_top_right_corner(self, mock_output):
        expected = ('[  ][  ][  ][  ][🤠]    '
                    '\n    [  ][  ][  ][  ]    '
                    '\n    [  ][💊][  ][  ]    '
                    '\n    [  ][  ][  ][  ]    '
                    '\n    [  ][  ][  ][  ]    '
                    '\n    [  ][  ][  ][  ][🥊]\n')
        board = {(0, 0): True, (0, 1): True, (0, 2): True, (0, 3): True, (0, 4): True, (0, 5): False,
                 (1, 0): False, (1, 1): True, (1, 2): True, (1, 3): True, (1, 4): True, (1, 5): False,
                 (2, 0): False, (2, 1): True, (2, 2): 'Store', (2, 3): True, (2, 4): True, (2, 5): False,
                 (3, 0): False, (3, 1): True, (3, 2): True, (3, 3): True, (3, 4): True, (3, 5): False,
                 (4, 0): False, (4, 1): True, (4, 2): True, (4, 3): True, (4, 4): True, (4, 5): False,
                 (5, 0): False, (5, 1): True, (5, 2): True, (5, 3): True, (5, 4): True, (5, 5): 'Gym'}
        character = {"Current Location": (0, 4)}
        display_current_location(board, character, 6, 6)
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_display_current_location_character_at_bottom_left_corner(self, mock_output):
        expected = ('[  ][  ][  ][  ][  ]    '
                    '\n    [  ][  ][  ][  ]    '
                    '\n    [  ][💊][  ][  ]    '
                    '\n    [  ][  ][  ][  ]    '
                    '\n    [  ][  ][  ][  ]    '
                    '\n    [🤠][  ][  ][  ][🥊]\n')
        board = {(0, 0): True, (0, 1): True, (0, 2): True, (0, 3): True, (0, 4): True, (0, 5): False,
                 (1, 0): False, (1, 1): True, (1, 2): True, (1, 3): True, (1, 4): True, (1, 5): False,
                 (2, 0): False, (2, 1): True, (2, 2): 'Store', (2, 3): True, (2, 4): True, (2, 5): False,
                 (3, 0): False, (3, 1): True, (3, 2): True, (3, 3): True, (3, 4): True, (3, 5): False,
                 (4, 0): False, (4, 1): True, (4, 2): True, (4, 3): True, (4, 4): True, (4, 5): False,
                 (5, 0): False, (5, 1): True, (5, 2): True, (5, 3): True, (5, 4): True, (5, 5): 'Gym'}
        character = {"Current Location": (5, 1)}
        display_current_location(board, character, 6, 6)
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)
