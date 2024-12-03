import random
import copy
from typing import Any
from board import display_current_location, make_board, check_current_location
from common import check_input_is_digit
from data import starting_pokemon_collection, get_skill_of, event_pokemon
from event_option import fight, throw_poke_ball, get_probability, change_pokemon
from gym import encounter_gym, level_up, has_six_pokemons
from store import use_potion, encounter_store


def set_up_game() -> dict:
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
        print(f"\n{user_choice} is not included in Starting pokemon")
        user_choice = input("what pokemon would you like? ").capitalize()
    print()
    character['Poke Ball'] = {user_choice: starting_pokemon[user_choice]}
    character['Starting Pokemon'] = user_choice
    return character


def print_instructions():
    """
    Print the game instructions.

    :postcondition: displays the game instructions in detail
    """
    print("\nWelcome to the world of Pokemon! Embark on an exciting journey to become a Pokemon Champion.")
    print("\nImportant notes to know before you begin:")
    print("- Stores are represented by S on the map.")
    print("- Gyms are represented by G on the map.")
    # print("- You can catch wild pokèmons by throwing pokeball when their HP is less than 11.")
    print("- If all six of your Pokémon lose their HP, the game is over.")
    print("- You can only challenge a Gym Leader once you have a full team of six Pokémon.")
    print("- After defeating a Gym Leader, you will earn a Badge, unlocking the next level.")
    print("- Badge Requirements by Level:")
    print("  - Level 1: Defeat the gym leader twice to earn a badge.")
    print("  - Level 2: Defeat the gym leader three times to earn a badge.")
    print("  - Level 3: Defeat the gym leader four times to earn a badge and complete the mission.")
    print("- The mission is complete when you defeat the final Gym Leader at Level 3.")


def is_alive(character: dict[str, Any]) -> bool:
    """
    Check if the character is alive

    :param character: a dictionary representing character, including their Pokémon
    :precondition: character is a dictionary with a key "Balls" including Pokémon's HP
    :postcondition: returns True if at least one Pokémon has HP greater than 0, else False
    :return: True if the character is alive, else False
    """
    alive = True

    if not any(pokemon['currentHP'] > 0 for pokemon in character["Poke Ball"].values()):
        alive = False

    return alive


def select_pokemon(pokeball: dict) -> (str, dict):
    """
    Ask user to select a Pokémon.

    :param pokeball: a dictionary representing collection of Pokémon(s)
    :precondition: pokeball is a dictionary representing collection of Pokémon(s)
    :postcondition: provides selected Pokémon name and the Pokémon's info
    :return: a tuple of a string representing selected Pokémon name,
             and a dictionary of the Pokémon's info
    """
    print("\nYour pokemons' status...")
    for pokemon in pokeball.keys():
        print(f"{pokemon}(HP: {pokeball[pokemon]['currentHP']})")

    while True:
        user_choice = input("\nSelect pokemon to proceed by entering the pokemon name: ").capitalize()
        if user_choice in pokeball.keys():
            break

    return user_choice, pokeball[user_choice]


def current_pokemon_collection(character_level: int, level1: dict, level2: dict, level3: dict) -> dict:
    """
    Decide which Pokémon collection to use based on the character_level.

    :param character_level: an integer that represents user's current level
    :param level1: a dictionary containing level1 Pokémon information
    :param level2: a dictionary containing level2 Pokémon information
    :param level3: a dictionary containing level3 Pokémon information
    :precondition: character_level must be a number between 1 and 3
    :precondition: Pokémon information should not be over wrapped between level1, level2 and level3
    :postcondition: choose a Pokémon collection tailored to the character_level
    :return: a dictionary containing Pokémon collection tailored to the character_level
    """
    if character_level == 2:
        current_level_collection = level2
    elif character_level == 3:
        current_level_collection = level3
    else:
        current_level_collection = level1

    return current_level_collection


def set_event_type() -> str or bool:
    """
    Determine what kind of event has occurred.

    :postcondition: choose a random event type
    :return: a string representing the type of event if an event has occurred
    :return: a boolean value, false if no event has occurred
    """
    event_collection = ("wildPokemon", "Team Rocket", "Strange trainer", False)
    return random.choices(event_collection, weights=[18, 5, 7, 3], k=1)[0]


def get_event_pokemon(character: dict) -> tuple:
    """
    Set up an event Pokémon.

    :param character: a dictionary containing information about the character's status
    :precondition: character has a value about 'Current Level' key and 'Poke Ball' key
    :postcondition: get the event Pokémon collection tailored to current user's level
    :postcondition: get a random event Pokémon from the event Pokémon collection
    :return: a tuple representing information about the random event Pokémon
    """
    event_pokemon_collection = event_pokemon(character["Current Level"])

    while True:
        event_pokemon_info = copy.deepcopy(random.choices(list(event_pokemon_collection.items()), k=1)[0])
        if event_pokemon_info[0] not in character["Poke Ball"].keys():
            return event_pokemon_info


def take_out_pokemon(character_pokemons: dict) -> tuple:
    """
    Set up a user's Pokémon for battle

    :param character_pokemons: a dictionary containing information about Pokémon the user has
    :precondition: pokeball should contain Pokémon's name, and its type and current hp
    :postcondition: choose a random user's Pokémon that has HP greater than 0 from the character_pokemons
    :return: a tuple containing the random user's Pokémon's name, type, and HP
    """
    player_pokemon = random.choice(list(character_pokemons.items()))
    while player_pokemon[1]['currentHP'] == 0:
        player_pokemon = random.choice(list(character_pokemons.items()))
    print(f"Go, {player_pokemon[0]}!")
    return player_pokemon


def customize_user_options(event_type: str, gym_round: (int or None) = None) -> list:
    """
    Add an option to the user's options tailored to the event type.

    :param event_type: a string that represents what kind of event occurs
    :param gym_round: an integer representing the number of games played
    :param gym_round: None if the event_type is not "Gym Leader"
    :precondition: event_type must be either wild Pokémon, Team Rocket, Gym Leader or Strange trainer
    :precondition: gym_round must be greater than 0 if its type is an integer
    :postcondition: add "Run Away" option if gym_round is greater than 2
    :postcondition: add use_potion option if event_type is not "Gym Leader"
    :postcondition: add throw_poke_ball and "Run Away" options if event_type is 'wildPokemon'
    :return: a list containing the options the user can choose
    """
    character_option = ["Fight", "Change Pokemon"]
    if event_type == 'Gym Leader':
        if gym_round > 2:
            character_option.append("Run Away")
    else:
        character_option.append("Use Potion")
        if event_type == 'wildPokemon':
            character_option.extend(["Throw Poke Ball", "Run Away"])
    return character_option


def select_event_option(event_type: str, gym_round: (int or None) = None) -> str:
    """
    Decide what to do when an event occurs.

    :param event_type: a string that represents what kind of event occurs
    :param gym_round: an integer representing the number of games played
    :param gym_round: None if the event_type is not "Gym Leader"
    :precondition: gym_round must be greater than 0 if its type is an integer
    :precondition: event_type must be either wild Pokémon, Team Rocket, Gym Leader or Strange trainer
    :postcondition: display the options the user can choose from
    :postcondition: get the user's choice of which option the user wants
    :return: a string representing the option the user wants to do
    """
    character_option = customize_user_options(event_type, gym_round)

    for number, option in enumerate(character_option):
        print(f"{number + 1}. {option}")

    while True:
        user_choice = check_input_is_digit("What do you want to do (Enter number)? ")
        if 1 <= user_choice <= len(character_option):
            return character_option[user_choice - 1]
        print(f"\nInvalid choice! Please enter a number between 1 and {len(character_option)}.")


def proceed_event_option(user_choice: str, character_pokemon: tuple, character: dict,
                         event_pokemon_info: tuple, event_type: str) -> bool:
    """
    Execute the function corresponding to the user's selected option.

    :param user_choice: a string representing the option the user wants to do
    :param character_pokemon: a tuple containing the user Pokémon's name and a dictionary with its type and current HP
    :param character: a dictionary containing information about the character's status
    :param event_pokemon_info: a tuple containing the event Pokémon's name and a dictionary with its type and current HP
    :param event_type: a string that represents what kind of event occurs
    :precondition: the user Pokémon must have an HP greater than 0 in the character_pokemon
    :precondition: the event Pokémon must have an HP greater than 0 in the event_pokemon_info
    :precondition: character_pokemon represents the status of one of the user's Pokémon in battle
    :precondition: event_type must be either wild Pokémon, Team Rocket, Gym Leader or Strange trainer
    :precondition: user_choice must be either "Fight", "Throw Poke Ball" or "Run Away"
    :postcondition: execute the function corresponding to the user's selected option
    :postcondition: finish the event if user_choice is "Run Away"
    :return: a boolean value, false if the event has finished, true otherwise
    """
    if user_choice == "Fight":
        process_result = fight(character_pokemon, event_pokemon_info, character, event_type)
    elif user_choice == "Throw Poke Ball":
        process_result = throw_poke_ball(event_pokemon_info, character)
    else:
        print(f"\nYou escaped from {event_pokemon_info[0]}!\n")
        process_result = False
    return process_result


def get_stronger_collection(character_level: int) -> tuple:
    """
    Provide stronger number collection based on the user's level.

    :param character_level: an integer that represents user's current level
    :precondition: character_level must be a number between 1 and 3
    :postcondition: retrieve a collection of values showing the increase in the event Pokémon's skill damage
    :return: a tuple containing values representing the potential increase in the event Pokémon's skill damage
    """
    if character_level == 1:
        stronger_collection = (1, 1.3, 1.4, 1.5)
    elif character_level == 2:
        stronger_collection = (1.3, 1.5, 1.7, 2)
    else:
        stronger_collection = (1.5, 1.7, 2, 2.5)

    return stronger_collection


def make_damage_stronger(event_type: str, character_level: int) -> int:
    """
    Determine how strong the event Pokémon skill will be based on the event_type.

    :param event_type: a string that represents what kind of event occurs
    :param character_level: an integer that represents user's current level
    :precondition: event_type must be either wild Pokémon, Team Rocket, Gym Leader or Strange trainer
    :precondition: character_level must be a number between 1 and 3
    :postcondition: get the corresponding tuple index value based on the event type
    :return: an integer representing how much stronger the event Pokémon's skill becomes
    """
    stronger_collection = get_stronger_collection(character_level)

    if event_type == 'Team Rocket':
        stronger = stronger_collection[2]
    elif event_type == 'Strange trainer':
        stronger = stronger_collection[1]
    elif event_type == 'wildPokemon':
        stronger = stronger_collection[0]
    else:
        stronger = stronger_collection[3]

    return stronger


def check_status(character_pokemon: tuple) -> bool:
    """
    Check if the user's Pokémon has fainted.

    :param character_pokemon: a tuple containing the user Pokémon's name and a dictionary with its type and current HP
    :precondition: character_pokemon represents the status of one of the user's Pokémon in battle
    :postcondition: check the status of user's Pokémon
    :return: a boolean value, false if the user's Pokémon has fainted, true otherwise
    """
    if character_pokemon[1]['currentHP'] <= 0:
        character_pokemon[1]['currentHP'] = 0
        print(f"{character_pokemon[0]} fainted!")
        status = False
    else:
        status = True
    return status


def get_attacked(event_pokemon_info: tuple, event_type: str, character: dict, character_pokemon: tuple) -> bool:
    """
    Check if the user's Pokémon has fainted and the event is over.

    :param event_pokemon_info: a tuple containing the event Pokémon's name and a dictionary with its type and current HP
    :param event_type: a string that represents what kind of event occurs
    :param character: a dictionary containing information about the character's status
    :param character_pokemon: a tuple containing the user Pokémon's name and a dictionary with its type and current HP
    :precondition: the user Pokémon must have an HP greater than 0 in the character_pokemon
    :precondition: character_pokemon represents the status of one of the user's Pokémon in battle
    :precondition: the event Pokémon must have an HP greater than 0 in the event_pokemon_info
    :precondition: the user Pokémon must have an HP greater than 0 in the character_pokemon
    :precondition: character_pokemon represents the status of one of the user's Pokémon in battle
    :postcondition: set up the skill the event Pokémon will use to attack
    :postcondition: check if the event Pokémon's skill hit
    :postcondition: check the status of user's Pokémon
    :return: a boolean value, false if the event is over due to the user's Pokémon fainting, true otherwise
    """
    skill_collection = get_skill_of(event_pokemon_info[1]['type'])
    event_pokemon_skill = random.choices(list(skill_collection), k=1)[0]
    damage = int(make_damage_stronger(event_type, character['Current Level']) *
                 random.choice(range(event_pokemon_skill['damage'][0], event_pokemon_skill['damage'][1] + 1)))

    print(f"{event_pokemon_info[0]} used {event_pokemon_skill['name']}!\n")

    if get_probability():
        print(f"{event_pokemon_skill['name']} hit!")
        character_pokemon[1]['currentHP'] -= damage
        print(f"{character_pokemon[0]} took {damage} damage!")
    else:
        print(f"{event_pokemon_skill['name']} missed!")

    return check_status(character_pokemon)


def describe_event(event_type: str, character: dict) -> tuple:
    """
    Identify the event that has occurred.

    :param event_type: a string that represents what kind of event occurs
    :param character: a dictionary containing information about the character's status
    :precondition: event_type must be either wild Pokémon, Team Rocket or Strange trainer
    :postcondition: set up information about a random event Pokémon
    :postcondition: display what event has occurred
    :return: a tuple containing the event Pokémon's name and a dictionary containing its type and current HP
    """
    event_pokemon_info = get_event_pokemon(character)
    if event_type == "wildPokemon":
        print(f"\nA wild {event_pokemon_info[0]} appeared!\n")
        print(f"\nEvent pokemon status: {event_pokemon_info[0]}(HP: {event_pokemon_info[1]['currentHP']})\n")
    else:
        print(f"\nYou encountered a {event_type}!\n{event_type} sent out {event_pokemon_info[0]}!\n")
    return event_pokemon_info


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
            print(f"\n{character['Character Name']}'s pokemon status: {character_pokemon[0]}"
                  f"(HP: {character['Poke Ball'][character_pokemon[0]]['currentHP']})\n")

            user_choice = select_event_option(event_type)

            if user_choice == "Change Pokemon":
                character_pokemon = change_pokemon(character['Poke Ball'], character_pokemon)
            elif user_choice == "Use Potion":
                use_potion(character, character_pokemon)
            else:
                process_result = proceed_event_option(user_choice, character_pokemon, character,
                                                      event_pokemon_info, event_type)

            if process_result:
                process_result = get_attacked(event_pokemon_info, event_type, character, character_pokemon)
    else:
        print("\nNo event is occurred.\n------------------------------------------\n")


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
            print("\nCurrent your pokemons' status is...")
            for name, info in character['Poke Ball'].items():
                print(f"{name}(HP: {info['currentHP']})")
            print(f"\nYou have ${character['Money']} and You have {character['Potion']} potion(s)!\n")
            display_current_location(board, character, rows, columns)
        else:
            print("\nPlease choose a valid direction!")


def validate_move(board: dict[(int, int), bool | str], character: dict[str, Any], direction: int) -> (bool, (int, int)):
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
    """
    directions = {1: (-1, -0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}

    new_position = None
    if direction in directions:
        dx, dy = directions[direction]
        new_position = (character['Current Location'][0] + dx, character['Current Location'][1] + dy)

        return board.get(new_position, False), new_position

    return False, new_position


def move_character(character: dict[str, Any], new_position: (int, int),
                   board: dict[(int, int), bool | str], rows: int, columns: int):
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
    character = set_up_game()
    board, rows, columns = make_board(character['Current Level'])
    achieved_goal = False
    prev_level = character['Current Level']

    while is_alive(character) and not achieved_goal:
        if prev_level != character['Current Level']:
            board, rows, columns = make_board(character['Current Level'])
            prev_level += 1
        display_current_location(board, character, rows, columns)
        direction = get_user_choice(character, board, rows, columns)

        is_valid_move, new_position = validate_move(board, character, direction)
        if is_valid_move:
            move_character(character, new_position, board, rows, columns)
            is_special_location = check_current_location(board, character)
            if is_special_location:
                achieved_goal = process_by_location_type(character, board)
            else:
                event_occurred(character)
        else:
            print("You can't go in that direction!")

        if achieved_goal:
            print("Congratulations! You have successfully finished your journey :)")
        elif not is_alive(character):
            print("GAME OVER")


def process_by_location_type(character: dict[str, Any],
                             board: dict[(int, int), bool | str][(int, int), bool | str]) -> bool:
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


def test_gym():
    character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 1, 'Potion': 0,
                 'Current Location': (5, 5),
                 'Starting Pokemon': 'Squirtle',
                 'Poke Ball': {
                     'Squirtle': {'type': 'water', 'currentHP': 40},
                     'Pichu': {'type': 'electric', 'currentHP': 30},
                     'Shinx': {'type': 'electric', 'currentHP': 30},
                     'Mareep': {'type': 'electric', 'currentHP': 30},
                     'Caterpie': {'type': 'grass', 'currentHP': 30},
                     'Weedle': {'type': 'grass', 'currentHP': 30},
                 }}
    board, rows, columns = make_board(character['Current Level'])
    process_by_location_type(character, board)


def main():
    """
    Drive the program.
    """
    game()
    # test_gym()


if __name__ == "__main__":
    main()
