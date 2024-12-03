from unittest import TestCase


from board import make_board


class TestMakeBoard(TestCase):

    def test_make_board_level_is_1(self):
        level = 1
        expected = ({(0, 0): True, (0, 1): True, (0, 2): True, (0, 3): True, (0, 4): True, (0, 5): False,
                     (1, 0): False, (1, 1): True, (1, 2): True, (1, 3): True, (1, 4): True, (1, 5): False,
                     (2, 0): False, (2, 1): True, (2, 2): 'Store', (2, 3): True, (2, 4): True, (2, 5): False,
                     (3, 0): False, (3, 1): True, (3, 2): True, (3, 3): True, (3, 4): True, (3, 5): False,
                     (4, 0): False, (4, 1): True, (4, 2): True, (4, 3): True, (4, 4): True, (4, 5): False,
                     (5, 0): False, (5, 1): True, (5, 2): True, (5, 3): True, (5, 4): True, (5, 5): 'Gym'}, 6, 6)
        actual = make_board(level)
        self.assertEqual(expected, actual)

    def test_make_board_level_is_2(self):
        level = 2
        expected = ({(0, 0): True, (0, 1): False, (0, 2): False, (0, 3): False, (0, 4): False, (1, 0): True,
                     (1, 1): True, (1, 2): True, (1, 3): True, (1, 4): True, (2, 0): True, (2, 1): True,
                     (2, 2): 'Store', (2, 3): True, (2, 4): True, (3, 0): True, (3, 1): True, (3, 2): True,
                     (3, 3): True, (3, 4): True, (4, 0): True, (4, 1): True, (4, 2): True, (4, 3): True, (4, 4): True,
                     (5, 0): True, (5, 1): True, (5, 2): True, (5, 3): True, (5, 4): True, (6, 0): True, (6, 1): True,
                     (6, 2): True, (6, 3): True, (6, 4): True, (7, 0): False, (7, 1): False, (7, 2): False,
                     (7, 3): False, (7, 4): 'Gym'}, 8, 5)
        actual = make_board(level)
        self.assertEqual(expected, actual)

    def test_make_board_level_is_3(self):
        level = 3
        expected = ({(0, 0): False, (0, 1): False, (0, 2): False, (0, 3): False, (0, 4): True, (1, 0): True,
                     (1, 1): True, (1, 2): True, (1, 3): True, (1, 4): True, (2, 0): True, (2, 1): True,
                     (2, 2): 'Store', (2, 3): True, (2, 4): True, (3, 0): True, (3, 1): True, (3, 2): True,
                     (3, 3): True, (3, 4): True, (4, 0): True, (4, 1): True, (4, 2): True, (4, 3): True, (4, 4): True,
                     (5, 0): True, (5, 1): True, (5, 2): True, (5, 3): True, (5, 4): True, (6, 0): True, (6, 1): True,
                     (6, 2): True, (6, 3): True, (6, 4): True, (7, 0): True, (7, 1): True, (7, 2): True, (7, 3): True,
                     (7, 4): True, (8, 0): True, (8, 1): True, (8, 2): True, (8, 3): True, (8, 4): True, (9, 0): 'Gym',
                     (9, 1): False, (9, 2): False, (9, 3): False, (9, 4): False}, 10, 5)
        actual = make_board(level)
        self.assertEqual(expected, actual)

    def test_make_board_level_is_invalid_0(self):
        level = 0
        expected = {}, 0, 0
        actual = make_board(level)
        self.assertEqual(expected, actual)

    def test_make_board_level_is_invalid_4(self):
        level = 4
        expected = {}, 0, 0
        actual = make_board(level)
        self.assertEqual(expected, actual)
