from board import display_current_location, make_board, check_if_current_location_is_special
from common import check_input_is_digit, is_alive
from data import starting_pokemon_collection
from event_option import change_pokemon
from event_pokemon_attack import get_attacked
from gym import encounter_gym, level_up, has_six_pokemons
from prepare_event import take_out_pokemon, set_event_type, describe_event, \
    proceed_event_option, select_event_option
from store import use_potion, encounter_store


def set_up_game() -> (dict, int):
    """
    Set up the character's information.

    :postcondition: ask a character's name
    :postcondition: display game instruction
    :postcondition: get the user's choice of which starting Pokémon the user wants
    :postcondition: set up a dictionary containing the character's information
    :return: a dictionary containing the character's information
    """
    character_name = input("What is your name? ").capitalize()
    print_instructions()
    character = {'Character Name': character_name, 'Money': 30, 'Current Level': 1, 'Potion': 0,
                 'Current Location': (0, 0)}
    starting_pokemon = starting_pokemon_collection(character['Current Level'])
    print("\nWhich pokemon would you like to go together?\nSquirtle(Water) | Charmander(Fire) | Bulbasaur(Grass)")
    user_choice = input("Please type pokemon name: ").capitalize()
    while user_choice not in starting_pokemon:
        print(f"\n{user_choice} is not included in Starting Pokémon")
        user_choice = input("what pokemon would you like? ").capitalize()
    print()
    character['Poke Ball'] = {user_choice: starting_pokemon[user_choice]}
    character['Starting Pokémon'] = user_choice
    return character, 1


def print_instructions() -> None:
    """
    Print the game instructions.

    :postcondition: displays the game instructions in detail

    >>> print_instructions()
    <BLANKLINE>
    Welcome to the world of Pokémon! Embark on an exciting journey to become a Pokémon Champion.
    <BLANKLINE>
    Important notes to know before you begin:
    - Stores are represented by S on the map.
    - Gyms are represented by G on the map.
    - You can catch wild pokémon by throwing pokeball when their HP is less than 11.
    - If all six of your Pokémon lose their HP, the game is over.
    - You can only challenge a Gym Leader once you have a full team of six Pokémon.
    - After defeating a Gym Leader, you will earn a Badge, unlocking the next level.
    - Badge Requirements by Level:
      - Level 1: Defeat the gym leader twice to earn a badge.
      - Level 2: Defeat the gym leader three times to earn a badge.
      - Level 3: Defeat the gym leader four times to earn a badge and complete the mission.
    - The mission is complete when you defeat the final Gym Leader at Level 3.
    """
    print("\nWelcome to the world of Pokémon! Embark on an exciting journey to become a Pokémon Champion.")
    print("\nImportant notes to know before you begin:")
    print("- Stores are represented by S on the map.")
    print("- Gyms are represented by G on the map.")
    print("- You can catch wild pokémons by throwing pokeball when their HP is less than 11.")
    print("- If all six of your Pokémon lose their HP, the game is over.")
    print("- You can only challenge a Gym Leader once you have a full team of six Pokémon.")
    print("- After defeating a Gym Leader, you will earn a Badge, unlocking the next level.")
    print("- Badge Requirements by Level:")
    print("  - Level 1: Defeat the gym leader twice to earn a badge.")
    print("  - Level 2: Defeat the gym leader three times to earn a badge.")
    print("  - Level 3: Defeat the gym leader four times to earn a badge and complete the mission.")
    print("- The mission is complete when you defeat the final Gym Leader at Level 3.")


def event_occurred(character: dict) -> None:
    """
    Handle an event.

    :param character: a dictionary containing information about the character's status
    :postcondition: check if an event has occurred
    :postcondition: set up an event Pokémon and the user's Pokémon for battle if an event has occurred
    :postcondition: get the user's choice of which option the user wants
    :postcondition: execute a function tailored the user choice
    :postcondition: get attacked from the event Pokémon if the event Pokémon is not defeated
    :postcondition: check if the user Pokémon fainted
    """
    event_type = set_event_type()
    process_result = True

    if event_type:
        event_pokemon_info = describe_event(event_type, character)

        character_pokemon = take_out_pokemon(character['Poke Ball'])

        while process_result:
            print(f"{character['Character Name']}'s Pokémon status: {character_pokemon[0]}"
                  f"(HP: {character['Poke Ball'][character_pokemon[0]]['currentHP']})\n")

            user_choice = select_event_option(event_type)

            if user_choice == "Change Pokémon":
                character_pokemon = change_pokemon(character['Poke Ball'], character_pokemon)
            elif user_choice == "Use Potion":
                use_potion(character, character_pokemon)
            else:
                process_result = proceed_event_option(user_choice, character_pokemon, character,
                                                      event_pokemon_info, event_type)

            if process_result:
                process_result = get_attacked(event_pokemon_info, event_type, character, character_pokemon)
    else:
        print("\n\nNo event is occurred\n------------------------------------------\n\n")


def get_user_choice(character: dict, board: dict, rows: int, columns: int) -> int:
    """
    Get the user's choice of direction to move or check the user's status.

    :param character: a dictionary containing information about the character's status
    :param board: a dictionary representing the game board
    :param rows: a positive integer representing number of rows of the game board
    :param columns: a positive integer representing number of columns of the game board
    :precondition: board is a dictionary representing the game board
    :precondition: character is a dictionary representing character's info, including their current location
    :precondition: rows is an integer greater than 0
    :precondition: columns is an integer greater than 0
    :postcondition: get the user's choice of which direction to move or check the user's status
    :postcondition: display the user's status if the user choose number 5
    :return: an integer that represents which direction the user wants to move
    """
    while True:
        print("\n1. Up  2. Down  3. Left  4. Right  5. Check status")
        user_choice = check_input_is_digit("What number would you like to choose (Enter number)? ")

        if 1 <= user_choice <= 4:
            return user_choice
        elif user_choice == 5:
            print("\nCurrent your Pokémon' status is...")
            for name, info in character['Poke Ball'].items():
                print(f"{name}(HP: {info['currentHP']})")
            print(f"\nYou have ${character['Money']} and You have {character['Potion']} potion(s)!\n")
            display_current_location(board, character, rows, columns)
        else:
            print("\nPlease choose a valid direction!")


def validate_move(board: dict, character: dict, direction: int) -> (bool, (int, int)):
    """
    Validate user move.

    :param board: a dictionary representing the game board
    :param character: a dictionary representing character's info, including their current location
    :param direction: a positive integer representing the direction between 'Up', 'Down', 'Left', or 'Right'
    :precondition: board is a dictionary representing the game board
    :precondition: character is a dictionary representing character's info, including their current location
    :precondition: direction is a positive integer from 1 to 4
                    representing 'Up', 'Down', 'Left', or 'Right' respectively
    :postcondition: check if the move is within the boundaries of the game board
    :return: a tuple of boolean representing whether the move is within the boundaries of the game board
             and a tuple representing the corresponding new position,
             including an integer representing X-coordinate, and an integer representing Y-coordinate

    >>> test_board = {(0, 0): True, (0, 1): True, (0, 2): True, (0, 3): True, (0, 4): True, (0, 5): False,
    ...          (1, 0): False, (1, 1): True, (1, 2): True, (1, 3): True, (1, 4): True, (1, 5): False,
    ...          (2, 0): False, (2, 1): True, (2, 2): 'Store', (2, 3): True, (2, 4): True, (2, 5): False,
    ...          (3, 0): False, (3, 1): True, (3, 2): True, (3, 3): True, (3, 4): True, (3, 5): False,
    ...          (4, 0): False, (4, 1): True, (4, 2): True, (4, 3): True, (4, 4): True, (4, 5): False,
    ...          (5, 0): False, (5, 1): True, (5, 2): True, (5, 3): True, (5, 4): True, (5, 5): 'Gym'}
    >>> test_character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 1, 'Potion': 0,
    ...              'Current Location': (0, 0),
    ...              'Starting Pokémon': 'Squirtle',
    ...              'Poke Ball': {
    ...                  'Squirtle': {'type': 'water', 'currentHP': 40},
    ...                  'Pichu': {'type': 'electric', 'currentHP': 30},
    ...                  'Shinx': {'type': 'electric', 'currentHP': 30},
    ...                  'Mareep': {'type': 'electric', 'currentHP': 30},
    ...                  'Caterpie': {'type': 'grass', 'currentHP': 30},
    ...                  'Weedle': {'type': 'grass', 'currentHP': 30},
    ...              }}
    >>> validate_move(test_board, test_character, 1)
    (False, None)
    >>> validate_move(test_board, test_character, 4)
    (True, (0, 1))
    """
    directions = {1: (-1, -0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
    valid_move = False

    new_position = None
    if direction in directions:
        dx, dy = directions[direction]
        new_position = (character['Current Location'][0] + dx, character['Current Location'][1] + dy)
        valid_move = board.get(new_position, False)
        return valid_move, new_position if valid_move else None

    return valid_move, new_position


def move_character(character: dict, new_position: (int, int),
                   board: dict, rows: int, columns: int) -> None:
    """
    Move character.

    :param character: a dictionary representing character's info, including their current location
    :param new_position: a tuple representing the new location
    :param board: a dictionary representing the game board
    :param rows: a positive integer representing number of rows of the game board
    :param columns: a positive integer representing number of columns of the game board
    :precondition: character is a dictionary representing character's info, including their current location
    :precondition: new_position is a tuple representing the new location,
                   including an integer representing X-coordinate, and an integer representing Y-coordinate
    :precondition: board is a dictionary representing the game board
    :precondition: rows is an integer greater than 0
    :precondition: columns is an integer greater than 0
    :postcondition: updates the character's current location based on the new position
    """
    character['Current Location'] = new_position

    print()
    display_current_location(board, character, rows, columns)


def game():
    """
    Drive the game.
    """
    character, prev_level = set_up_game()
    board, rows, columns = make_board(character['Current Level'])
    achieved_goal = False

    while is_alive(character) and not achieved_goal:
        if prev_level != character['Current Level']:
            board, rows, columns = make_board(character['Current Level'])
            prev_level += 1
        display_current_location(board, character, rows, columns)
        direction = get_user_choice(character, board, rows, columns)

        is_valid_move, new_position = validate_move(board, character, direction)
        if is_valid_move:
            move_character(character, new_position, board, rows, columns)
            is_special_location = check_if_current_location_is_special(board, character)
            if is_special_location:
                achieved_goal = process_by_location_type(character, board)
            else:
                event_occurred(character)
        else:
            print("You can't go in that direction!")

        if achieved_goal:
            print("\nCongratulations! You have successfully finished your journey :)")
        elif not is_alive(character):
            print("\nGAME OVER: You don't have any Pokémon to continue the adventure")


def process_by_location_type(character: dict,
                             board: dict) -> bool:
    """
    Process actions when character's location is gym or store.

    :param character: a dictionary representing character's info, including their current location and level
    :param board: a dictionary representing the game board
    :precondition: character is a dictionary which has 'Current Location' and 'Current Level' keys
    :precondition: board is a dictionary which has all the available coordinates keys
    :postcondition: executes specific actions when character is currently located in gym or store
    :return: True if the character achieved their goal as a result of going through the specific location,
             otherwise False
    """
    achieved_goal = False
    current_location = board[character['Current Location']]
    if current_location == "Gym":
        if has_six_pokemons(character):
            gym_badge_earned = encounter_gym(character)
            if gym_badge_earned:
                if character['Current Level'] == 3:
                    achieved_goal = True
                else:
                    level_up(character)
    elif current_location == "Store":
        encounter_store(character)
    return achieved_goal


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
