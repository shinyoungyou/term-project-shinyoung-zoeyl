import itertools


def make_board(level: int) -> (dict, int, int):
    """
    Make a new game board for the given level.

    :param level: an integer between 1, 2, and 3, representing the current level
    :precondition: level is a positive integer between 1, 2, and 3
    :postcondition: creates a dictionary of new board for the given level
    :return: a tuple of dictionary representing the game board,
            an integer for the number of rows,
            and an integer for the number of columns

    >>> test_board, test_rows, test_columns = make_board(1)
    >>> test_board[(5, 5)], test_board[(2, 2)], test_board[(1, 0)], test_board[(0, 1)]
    ('Gym', 'Store', False, True)
    >>> test_board, test_rows, test_columns = make_board(2)
    >>> test_board[(7, 4)], test_board[(2, 2)], test_board[(1, 0)], test_board[(0, 1)]
    ('Gym', 'Store', True, False)
    >>> test_board, test_rows, test_columns = make_board(3)
    >>> test_board[(9, 0)], test_board[(2, 2)], test_board[(1, 0)], test_board[(0, 1)]
    ('Gym', 'Store', True, False)
    """
    board = {}

    level_config = {
        1: (6, 6, lambda row, column: (row == 0 and column < 5) or (1 <= row <= 4 and 1 <= column <= 4) or
                                      (row == 5 and column > 0), (5, 5), (2, 2)),
        2: (8, 5, lambda row, column: (row == 0 and column == 0) or (1 <= row <= 6 and 0 <= column <= 4) or
                                      (row == 7 and column == 4), (7, 4), (2, 2)),
        3: (10, 5, lambda row, column: (row == 0 and column == 4) or (1 <= row <= 8 and 0 <= column <= 4) or
                                       (row == 9 and column == 0), (9, 0), (2, 2)),
    }

    if level not in level_config:
        return board, 0, 0

    rows, columns, is_accessible, gym_location, store_location = level_config[level]

    board = {(i, j): is_accessible(i, j) for i, j in itertools.product(range(rows), range(columns))}

    board[gym_location] = "Gym"
    board[store_location] = "Store"

    return board, rows, columns


def display_current_location(board: dict, character: dict, rows: int, columns: int) -> None:
    """
    Display the current location of the game board.

    :param board: a dictionary representing the game board
    :param character: a dictionary representing the character
    :param rows: a positive integer representing the number of rows
    :param columns: a positive integer representing the number of columns
    :precondition: board is a dictionary representing the game board
    :precondition: character is a dictionary representing the character
    :precondition: rows is a positive integers
    :precondition: columns is a positive integers
    :postcondition: prints the current location of character, store, and gym
    """
    if not board:
        return

    for i in range(rows):
        row = ""
        for j in range(columns):
            location = board.get((i, j), False)

            if location is False:
                row += "    "
            elif (i, j) == character["Current Location"]:
                row += "[🤠]"
            elif location == "Store":
                row += "[💊]"
            elif location == "Gym":
                row += "[🥊]"
            else:
                row += "[  ]"
        print(row)


def check_if_current_location_is_special(board: dict, character: dict) -> bool:
    """
    Check if the current location is store or gym

    :param board: a dictionary representing the game board
    :param character: a dictionary representing the character
    :precondition: board is a dictionary representing the game board
    :precondition: character is a dictionary representing the character
    :postcondition: determins if the current location is store or gym
    :return: True if the current location is store or gym, otherwise False

    >>> test_board = {(0, 0): True, (0, 1): True, (0, 2): True, (0, 3): True, (0, 4): True, (0, 5): False,
    ...              (1, 0): False, (1, 1): True, (1, 2): True, (1, 3): True, (1, 4): True, (1, 5): False,
    ...              (2, 0): False, (2, 1): True, (2, 2): 'Store', (2, 3): True, (2, 4): True, (2, 5): False,
    ...              (3, 0): False, (3, 1): True, (3, 2): True, (3, 3): True, (3, 4): True, (3, 5): False,
    ...              (4, 0): False, (4, 1): True, (4, 2): True, (4, 3): True, (4, 4): True, (4, 5): False,
    ...              (5, 0): False, (5, 1): True, (5, 2): True, (5, 3): True, (5, 4): True, (5, 5): 'Gym'}
    >>> test_character = {"Current Location": (5, 5)}
    >>> check_if_current_location_is_special(test_board, test_character)
    True
    >>> test_character = {"Current Location": (1, 0)}
    >>> check_if_current_location_is_special(test_board, test_character)
    False
    """
    is_special_location = False
    current_location = board[character["Current Location"]]
    if current_location in ("Store", "Gym"):
        is_special_location = True
    return is_special_location
