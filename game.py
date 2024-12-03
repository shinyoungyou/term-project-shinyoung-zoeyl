import itertools
import random
import copy
from typing import Callable, Union
from constants import POTION_PRICE


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
    # print("- You can catch wild pokemons by throwing pokeball when their HP is less than 11.")
    print("- If all six of your Pokémon lose their HP, the game is over.")
    print("- You can only challenge a Gym Leader once you have a full team of six Pokémon.")
    print("- After defeating a Gym Leader, you will earn a Badge, unlocking the next level.")
    print("- Badge Requirements by Level:")
    print("  - Level 1: Defeat the gym leader twice to earn a badge.")
    print("  - Level 2: Defeat the gym leader three times to earn a badge.")
    print("  - Level 3: Defeat the gym leader four times to earn a badge and complete the mission.")
    print("- The mission is complete when you defeat the final Gym Leader at Level 3.")


def make_board(level: int) -> (dict, int, int):
    """
    Make a new game board for the given level.

    :param level: an integer between 1, 2, and 3, representing the current level
    :precondition: level is a positive integer between 1, 2, and 3
    :postcondition: creates a dictionary of new board for the given level
    :return: a tuple of dictionary representing the game board,
            an integer for the number of rows,
            and an integer for the number of columns
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
        return board

    rows, columns, is_accessible, gym_location, store_location = level_config[level]

    for i, j in itertools.product(range(rows), range(columns)):
        board[(i, j)] = True if is_accessible(i, j) else False

    board[gym_location] = "Gym"
    board[store_location] = "Store"

    return board, rows, columns


def display_current_location(board: dict, character: dict, rows: int, columns: int):
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


def check_current_location(board: dict, character: dict) -> bool | str:
    """
    Check the current location of the game board.

    :param board: a dictionary representing the game board
    :param character: a dictionary representing the character
    :precondition: board is a dictionary representing the game board
    :precondition: character is a dictionary representing the character
    :postcondition: retrieves the description of current location from the board
    :return: the description of current location between True, False, Store, and Gym
    """
    is_special_location = False
    current_location = board[character["Current Location"]]
    if current_location == "Store" or current_location == "Gym":
        is_special_location = True
    return is_special_location


def is_alive(character: dict) -> bool:
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


def check_input_is_digit(input_message: str,
                         error_message: str = "Invalid input! Please enter a valid number: ") -> int:
    """
    Check if the user input is digit.

    :param input_message: a string representing the input message
    :param error_message: a string representing the error message
    :precondition input_message: a string representing the input message
    :precondition error_message: a string representing the error message
    :postcondition: prompts the user until they enter a valid digit
    :return: an integer representing valid input
    """
    while True:
        user_input = input(input_message)
        if user_input.isdigit():
            return int(user_input)
        else:
            print(error_message)


def encounter_store(character: dict):
    """
    Give user with options between buy or use potion, or quit the store.

    :param character: a dictionary containing the character's details, including 'Money', 'Poke Ball'
    :precondition: character is a dictionary representing the character
    :postcondition: executes selected option between buy potion, use potion, or quit
    """
    actions = {
        'buy': lambda: buy_potion(character),
        'use': lambda: use_potion(character, select_pokemon(character['Poke Ball'])),
    }

    while True:
        user_input = input("\nEnter 'buy' to buy a potion, 'use' to use a potion, or 'q' to quit: ").lower()
        if user_input in actions:
            actions[user_input]()
        elif user_input == 'q':
            break
        else:
            print("Invalid option. Please try again.")


def select_pokemon(pokeball: dict) -> (str, dict):
    """
    Let user select a Pokémon.

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


def buy_potion(character: dict):
    """
    Calculate the change after a purchase.

    :param character: a dictionary representing character, including their money
    :precondition: character is a dictionary with a key "Money" representing the character's current budget
    :postcondition: updates the character's money if any potion is purchased
    """
    print(f"\nYour budget is ${character['Money']}, and each potion price is ${POTION_PRICE}.")
    while True:
        number_of_potions = check_input_is_digit("Enter the number of potions to purchase: ")
        if number_of_potions > 0:
            break
        print("You need to buy at least one potion.")

    total_price = POTION_PRICE * number_of_potions
    print(f"\nTotal price will be: ${total_price}")
    budget = character["Money"]
    change = budget - total_price

    if change >= 0:
        character["Potion"] += 1 * number_of_potions
        print(f"Purchase successful! Your remaining budget is ${change}")
        character["Money"] = change
    else:
        print("You can't buy with your current budget.")


def starting_pokemon_collection(character_level: int) -> dict:
    """
    Provide a starting Pokémon collection tailored to the character_level.

    :param character_level: an integer that represents user's current level
    :precondition: character_level must be a number between 1 and 3
    :return: a dictionary containing starting Pokémon's information tailored to the character_level
    """
    level1_starting_pokemon = {'Squirtle': {'type': 'water', 'currentHP': 40},
                               'Charmander': {'type': 'fire', 'currentHP': 40},
                               'Bulbasaur': {'type': 'grass', 'currentHP': 40}}

    level2_starting_pokemon = {'Wartortle': {'type': 'water', 'currentHP': 65},
                               'Charmeleon': {'type': 'fire', 'currentHP': 65},
                               'Ivysaur': {'type': 'grass', 'currentHP': 65}}

    level3_starting_pokemon = {'Blastoise': {'type': 'water', 'currentHP': 100},
                               'Charizard': {'type': 'fire', 'currentHP': 100},
                               'Venusaur': {'type': 'grass', 'currentHP': 100}}

    pokemon_collection = current_pokemon_collection(character_level, level1_starting_pokemon,
                                                    level2_starting_pokemon, level3_starting_pokemon)

    return pokemon_collection


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


def event_pokemon(character_level: int) -> dict:
    """
    Provide an event Pokémon collection tailored to the character_level.

    :param character_level: an integer that represents user's current level
    :precondition: character_level must be a number between 1 and 3
    :postcondition: set up collections of event Pokémon information tailored to the user's level
    :postcondition: get a collection tailored to the character_level
    :return: a dictionary containing event Pokémon's information tailored to the character_level
    """
    level1_pokemon = {'Pichu': {'type': 'electric', 'currentHP': 30},
                      'Shinx': {'type': 'electric', 'currentHP': 30},
                      'Mareep': {'type': 'electric', 'currentHP': 30},
                      'Caterpie': {'type': 'grass', 'currentHP': 30},
                      'Weedle': {'type': 'grass', 'currentHP': 30},
                      'Treecko': {'type': 'grass', 'currentHP': 30},
                      'Pidgey': {'type': 'flying', 'currentHP': 30},
                      'Pidove': {'type': 'flying', 'currentHP': 30},
                      'Slowpoke': {'type': 'water', 'currentHP': 30},
                      'Horsea': {'type': 'water', 'currentHP': 30},
                      'Mudkip': {'type': 'water', 'currentHP': 30},
                      'Cyndaquil': {'type': 'fire', 'currentHP': 30},
                      'Totodile': {'type': 'fire', 'currentHP': 30},
                      'Magby': {'type': 'fire', 'currentHP': 30},
                      'Swinub': {'type': 'ice', 'currentHP': 30},
                      'Spheal': {'type': 'ice', 'currentHP': 30},
                      'Vanillite': {'type': 'ice', 'currentHP': 30},
                      'Geodude': {'type': 'rock', 'currentHP': 30},
                      'Aron': {'type': 'rock', 'currentHP': 30},
                      'Roggenrola': {'type': 'rock', 'currentHP': 30}}

    level2_pokemon = {'Pikachu': {'type': 'electric', 'currentHP': 50},
                      'Luxio': {'type': 'electric', 'currentHP': 50},
                      'Flaaffy': {'type': 'electric', 'currentHP': 50},
                      'Metapod': {'type': 'grass', 'currentHP': 50},
                      'Kakuna': {'type': 'grass', 'currentHP': 50},
                      'Grovyle': {'type': 'grass', 'currentHP': 50},
                      'Pidgeotto': {'type': 'flying', 'currentHP': 50},
                      'Tranquill': {'type': 'flying', 'currentHP': 50},
                      'Slowbro': {'type': 'water', 'currentHP': 50},
                      'Seadra': {'type': 'water', 'currentHP': 50},
                      'Marshtomp': {'type': 'water', 'currentHP': 50},
                      'Quilava': {'type': 'fire', 'currentHP': 50},
                      'Croconaq': {'type': 'fire', 'currentHP': 50},
                      'Magmar': {'type': 'fire', 'currentHP': 50},
                      'Piloswine': {'type': 'ice', 'currentHP': 50},
                      'Sealeo': {'type': 'ice', 'currentHP': 50},
                      'Vanillish': {'type': 'ice', 'currentHP': 50},
                      'Graveler': {'type': 'rock', 'currentHP': 50},
                      'Lairon': {'type': 'rock', 'currentHP': 50},
                      'Boldore': {'type': 'rock', 'currentHP': 50}}

    level3_pokemon = {'Raichu': {'type': 'electric', 'currentHP': 80},
                      'Luxray': {'type': 'electric', 'currentHP': 80},
                      'Ampharos': {'type': 'electric', 'currentHP': 80},
                      'Butterfree': {'type': 'grass', 'currentHP': 80},
                      'Beedrill': {'type': 'grass', 'currentHP': 80},
                      'Sceptile': {'type': 'grass', 'currentHP': 80},
                      'Pidgeot': {'type': 'flying', 'currentHP': 80},
                      'Pidove': {'type': 'flying', 'currentHP': 80},
                      'Slowking': {'type': 'water', 'currentHP': 80},
                      'Kingdra': {'type': 'water', 'currentHP': 80},
                      'Swampert': {'type': 'water', 'currentHP': 80},
                      'Typhlosion': {'type': 'fire', 'currentHP': 80},
                      'Reraligatr': {'type': 'fire', 'currentHP': 80},
                      'Magmortar': {'type': 'fire', 'currentHP': 80},
                      'Mamoswine': {'type': 'ice', 'currentHP': 80},
                      'Walrein': {'type': 'ice', 'currentHP': 80},
                      'Vanilluxe': {'type': 'ice', 'currentHP': 80},
                      'Golem': {'type': 'rock', 'currentHP': 80},
                      'Aggron': {'type': 'rock', 'currentHP': 80},
                      'Gigalith': {'type': 'rock', 'currentHP': 80}}
    event_pokemon_collection = current_pokemon_collection(character_level, level1_pokemon,
                                                          level2_pokemon, level3_pokemon)

    return event_pokemon_collection


def choose_skill_to_challenge(skill_collection: list, character_level: int) -> dict:
    """
    Provide information about skill the user chose.

    :param skill_collection: a list of dictionaries containing information about skills the user Pokémon can use.
    :param character_level: an integer that represents user's current level
    :precondition: character_level must be a number between 1 and 3
    :precondition: skill_collection must contain only information about skills related to the user Pokémon's type
    :postcondition: display what skills the user Pokémon can use
    :postcondition: ask what skill the user want to use
    :return: a dictionary containing skill information chosen by the user
    """
    number = 1
    for skill in skill_collection:
        print(f"{number}. {skill['name']}(damage range: {int(skill['damage'][0] * make_stronger(character_level))} ~ "
              f"{int(skill['damage'][1] * make_stronger(character_level))})")
        number += 1

    while True:
        user_choice = check_input_is_digit("Which skill would you like to use (Enter number)? ")
        if 1 <= user_choice <= len(skill_collection):
            return skill_collection[user_choice - 1]
        else:
            print(f"{user_choice} is not a valid choice! Please choose a valid option between 1 and "
                  f"{len(skill_collection)}.")


def get_probability() -> bool:
    """
    Check probabilities such as skill accuracy or whether the event Pokémon will run away.

    :postcondition: get a random boolean value
    :return: a boolean value
    """
    return random.choices([True, False], weights=[5, 1], k=1)[0]


def level_maximum_hp(character_level: int) -> int:
    """
    Check what maximum hp is based on the user's level.

    :param character_level: an integer that represents user's current level
    :precondition: character_level must be a number between 1 and 3
    :postcondition: set up the maximum hp based on the user's level
    :return: an integer that represents the maximum hp based on the character_level
    """
    if character_level == 1:
        maximum_hp = 40
    elif character_level == 2:
        maximum_hp = 65
    else:
        maximum_hp = 100
    return maximum_hp


def make_stronger(character_level: int) -> int:
    """
    Determine how much stronger the character's skill damage becomes.

    :param character_level: an integer that represents user's current level
    :precondition: character_level must be a number between 1 and 3
    :postcondition: set up how much stronger the character's skill damage will become
    :return: an integer that represent how much stronger the character's skill damage will become
    """
    if character_level == 2:
        stronger = 1.3
    elif character_level == 3:
        stronger = 1.8
    else:
        stronger = 1
    return stronger


def get_money(character: dict, event_type: str) -> None:
    """
    Determine how much money the user receives.

    :param character: a dictionary containing information about the character's status
    :param event_type: a string that represents what kind of event occurs
    :precondition: character has a value about 'Current Level' key and 'Money' key
    :precondition: event_type must be either wild Pokémon, Team Rocket, or Strange trainer
    :postcondition: set up how many times more money the user can receive
    :postcondition: multiply a random number from the range corresponding to the event type
    :postcondition: add the number to the value of the 'Money' key in the character
    """
    earn_money = make_stronger(character['Current Level'])
    if event_type == 'wildPokemon':
        earn_money *= random.randrange(3, 7)
    elif event_type == 'Team Rocket':
        earn_money *= random.randrange(25, 31)
    else:
        earn_money *= random.randrange(10, 20)
    character['Money'] += int(earn_money)
    print(f"You got ${int(earn_money)}!")


def get_attack_result(character_pokemon_skill: dict, event_pokemon_info: tuple, character: dict, event_type: str) \
        -> bool:
    """
    Check whether the event Pokémon is defeated.

    :param character_pokemon_skill: a dictionary containing skill name and skill damage range
    :param event_pokemon_info: a tuple containing the event Pokémon's name and a dictionary with its type and current HP
    :param character: a dictionary containing information about the character's status
    :param event_type: a string that represents what kind of event occurs
    :precondition: character has a value about 'Current Level' key and 'Money' key
    :precondition: event_type must be either wild Pokémon, Team Rocket, Gym Leader or Strange trainer
    :precondition: the event Pokémon must have an HP greater than 0 in the event_pokemon_info
    :postcondition: determine how much damage the character deals to the event Pokémon
    :postcondition: subtract the damage amount from the event Pokémon's hp
    :postcondition: check if the event Pokémon's hp is 0 or less
    :postcondition: get money if the event Pokémon's hp is 0 or less
    :return: a boolean value, false if the event Pokémon has been defeated, true otherwise
    """
    print(f"\n{character_pokemon_skill['name']} hit!")

    damage = int(make_stronger(character['Current Level']) * random.randrange(
        character_pokemon_skill['damage'][0], character_pokemon_skill['damage'][1] + 1))

    event_pokemon_info[1]['currentHP'] -= damage

    if event_pokemon_info[1]['currentHP'] <= 0:
        print(f"You defeated the {event_pokemon_info[0]}")
        if event_type != "Gym Leader":
            get_money(character, event_type)
        return False
    else:
        print(f"\nEvent pokemon status: {event_pokemon_info[0]}(HP: {event_pokemon_info[1]['currentHP']})\n")
        return True


def fight(character_pokemon: tuple, event_pokemon_info: tuple, character: dict, event_type: str) -> bool:
    """
    Check if the event is completed based on the user's selected 'fight' option.

    :param character_pokemon: a tuple containing the user Pokémon's name and a dictionary with its type and current HP
    :param event_pokemon_info: a tuple containing the event Pokémon's name and a dictionary with its type and current HP
    :param character: a dictionary containing information about the character's status
    :param event_type: event_type must be either wild Pokémon, Team Rocket, Gym Leader or Strange trainer
    :precondition: the user Pokémon must have an HP greater than 0 in the character_pokemon
    :precondition: character_pokemon represents the status of one of the user's Pokémon in battle
    :precondition: the event Pokémon must have an HP greater than 0 in the event_pokemon_info
    :precondition: character has a value about 'Current Level' key and 'Money' key
    :precondition: event_type must be either wild Pokémon, Team Rocket, Gym Leader or Strange trainer
    :postcondition: set up which skills the user Pokémon can use
    :postcondition: get the user's choice of which skill to use
    :postcondition: check whether the user Pokémon's skill hit
    :postcondition: check if the event is completed by the user Pokémon's attack if the skill hit
    :return: a boolean value, true if the event is not finished, false otherwise
    """
    print(f"\nEvent pokemon status: {event_pokemon_info[0]}(HP: {event_pokemon_info[1]['currentHP']})\n")
    skill_collection = get_skill_of(character_pokemon[1]['type'])
    character_pokemon_skill = choose_skill_to_challenge(skill_collection, character['Current Level'])
    if get_probability():
        return get_attack_result(character_pokemon_skill, event_pokemon_info, character, event_type)
    else:
        print(f"\n{character_pokemon_skill['name']} missed!\n"
              f"Event pokemon status: {event_pokemon_info[0]}(HP: {event_pokemon_info[1]['currentHP']})\n")
        return True


def change_pokemon(pokeball: dict, character_pokemon: tuple):
    """
    Switch the user's current Pokémon to another one chosen by the user during the Pokémon battle.

    :param pokeball: a dictionary containing information about Pokémon the user has
    :param character_pokemon: a tuple containing the user Pokémon's name and a dictionary with its type and current HP
    :precondition: pokeball should contain Pokémon's name, and their type and current hp
    :precondition: the user Pokémon must have an HP greater than 0 in the character_pokemon
    :precondition: character_pokemon represents the status of one of the user's Pokémon in battle
    :postcondition: display the user's Pokémon that can be switched
    :postcondition: get the user's choice of which Pokémon to switch to
    :postcondition: update character_pokemon's information to reflect the Pokémon the user chose
    :return: a tuple representing information of the Pokémon chosen by the user
    """
    if len(pokeball) == 1:
        print("\nYou has no pokemon to switch to\n")
    else:
        print("\nYour pokemons' status...")
        for pokemon in pokeball.keys():
            if pokemon != character_pokemon[0]:
                print(f"{pokemon}(HP: {pokeball[pokemon]['currentHP']})")

        user_choice = input("\nWhich pokemon would you like to switch to (Entering Pokemon name)? ").capitalize()
        while (user_choice not in pokeball.keys() or pokeball[user_choice]['currentHP'] == 0
               or user_choice == character_pokemon[0]):
            print(f"\n{user_choice} is not included in your Poke Balls or has 0HP")
            user_choice = input("Which pokemon would you like (Entering Pokemon name)? ").capitalize()

        print(f"\nGood job, {character_pokemon[0]}! Come back!\nGo, {user_choice}")

        character_pokemon = (user_choice, pokeball[user_choice])
        print(f"{user_choice}(HP: {character_pokemon[1]['currentHP']})\n")

    return character_pokemon


def check_potion(number_of_potion: int, character_level: int, character_pokemon: tuple) -> bool:
    """
    Check whether the user can use a potion.

    :param number_of_potion: an integer representing the number of potions the user has
    :param character_level: an integer that represents user's current level
    :param character_pokemon: a tuple containing the user Pokémon's name and a dictionary with its type and current HP
    :precondition: the user Pokémon must have an HP greater than 0 in the character_pokemon
    :precondition: character_level must be a number between 1 and 3
    :precondition: number_of_potion must be 0 or greater
    :postcondition: check if the user has no potion or the user's Pokémon has full HP
    :return: a boolean value, true if the user can use a potion on the Pokémon, false otherwise
    """
    validation = False
    if number_of_potion == 0:
        print("\nYou don't have any potion!\n")
    elif character_pokemon[1]["currentHP"] == level_maximum_hp(character_level):
        print(f"\n{character_pokemon[0]} has full HP!\n")
    else:
        validation = True
    return validation


def use_potion(character: dict, character_pokemon: tuple) -> None:
    """
    Restore the user's Pokémon's HP.

    :param character: a dictionary containing information about the character's status
    :param character_pokemon: a tuple containing the user Pokémon's name and a dictionary with its type and current HP
    :precondition: the user Pokémon must have an HP greater than 0 in the character_pokemon
    :precondition: character has a value about 'Current Level' key and 'Potion' key
    :precondition: check_potion returns a boolean value, true
    :postcondition: check whether the user wants to use a potion on the Pokémon
    :postcondition: add a certain amount to the Pokémon's HP
    """
    if check_potion(character['Potion'], character['Current Level'], character_pokemon):
        print(f"\nYou have {character['Potion']} potion(s)!\n{character_pokemon[0]} has "
              f"{character_pokemon[1]["currentHP"]} HP.")

        user_answer = input("\nWould you like to use a potion (y/n)? ").lower()
        while user_answer not in ('y', 'n'):
            print(f"\n{user_answer} is not a valid option")
            user_answer = input("Please choose a valid option (y/n): ").lower()

        if user_answer == 'y':
            pokemon_maximum_hp = level_maximum_hp(character['Current Level'])
            if character_pokemon[1]["currentHP"] > pokemon_maximum_hp - 15:
                character_pokemon[1]["currentHP"] = pokemon_maximum_hp
            else:
                character_pokemon[1]["currentHP"] += 15
            character['Potion'] -= 1
            print(f"\n{character_pokemon[0]} restored HP!\n{character_pokemon[0]}"
                  f"(HP: {character_pokemon[1]["currentHP"]})\n{character['Potion']} potion(s) left!")


def select_release_pokemon(character: dict) -> None:
    """
    Release one of the Pokémon the user has.

    :param character: a dictionary containing information about the character's status
    :precondition: character has a value about 'Poke Ball' key and 'Starting Pokemon' key
    :postcondition: display the Pokémon the user has along with their HP
    :postcondition: get the user's choice of which Pokémon the user wants to release
    :postcondition: delete the information about the Pokémon chosen by the user from the 'Poke Ball'
    """
    print("\nYou have...")
    for pokemon in character['Poke Ball'].keys():
        print(f"{pokemon}(HP: {character['Poke Ball'][pokemon]['currentHP']})")
    print("You can't choose the Starting Pokemon!")

    user_choice_pokemon = input("what pokemon would you release (Entering pokemon name)? ").capitalize()
    while (user_choice_pokemon not in character['Poke Ball'].keys() or user_choice_pokemon
           == character['Starting Pokemon']):
        print(f"\n{user_choice_pokemon} can't be chosen!")
        user_choice_pokemon = input(
            "Please choose a pokemon that is in your Poke Ball except your Starting Pokemon "
            + "(Entering pokemon name): ").capitalize()

        del character['Poke Ball'][user_choice_pokemon]
        print(f"\nGoodbye, {user_choice_pokemon}")


def check_total_of_user_pokemons(character: dict, event_pokemon_info: tuple) -> bool:
    """
    Check if the user has Pokémon fewer than six.

    :param character: a dictionary containing information about the character's status
    :param event_pokemon_info: a tuple containing the event Pokémon's name and a dictionary with its type and current HP
    :precondition: character has a value about 'Poke Ball' key and 'Starting Pokemon' key
    :precondition: the event Pokémon must have an HP 10 or less in the event_pokemon_info
    :precondition: the event Pokémon must have an HP greater than 0 in the event_pokemon_info
    :postcondition: get the user's choice to release one of the user's Pokémon if the user has six Pokémon
    :postcondition: release one of the user's Pokémon if the user choose 'y'
    :return: a boolean value, true if the user has Pokémon less than six, false otherwise
    """
    catch_pokemon = True
    if len(character['Poke Ball']) == 6:
        user_choice = input("\nYou can only carry up to 6 Pokémon. Would you like to release one (y/n)? ").lower()
        while user_choice not in ['y', 'n']:
            print(f"\n{user_choice} is not a valid option")
            user_choice = input("Please choose a valid option (y/n): ").lower()
        if user_choice == 'y':
            select_release_pokemon(character)
        else:
            print(f"\n{event_pokemon_info[0]} broke free!")
            catch_pokemon = False
    return catch_pokemon


def throw_poke_ball(event_pokemon_info: tuple, character: dict) -> bool:
    """
    Check if the event is completed based on the user's selected 'Throw Poke Ball' option.

    :param event_pokemon_info: a tuple containing the event Pokémon's name and a dictionary with its type and current HP
    :param character: a dictionary containing information about the character's status
    :precondition: the event Pokémon must have an HP greater than 0 in the event_pokemon_info
    :precondition: character has a value about 'Current Level' key, 'Starting Pokemon' key and 'Poke Ball' key
    :postcondition: check if the event Pokémon has HP greater than 10
    :postcondition: check if the user has Pokémon more than five, if the event Pokémon has HP less than 11
    :return: a boolean value, false if the user caught the event Pokémon successfully, true otherwise
    """
    process_result = False
    if event_pokemon_info[1]['currentHP'] <= 10:
        if check_total_of_user_pokemons(character, event_pokemon_info):
            character['Poke Ball'][event_pokemon_info[0]] \
                = {'type': event_pokemon_info[1]['type'],
                   'currentHP': int(level_maximum_hp(character['Current Level']) / 2)}
            print(f"\nGotcha! {event_pokemon_info[0]} was caught!\n")
    else:
        print("\nShoot! It was so close!")
        process_result = get_probability()
    return process_result


def set_event_type() -> Union[str, bool]:
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


def get_skill_of(pokemon_type: str) -> list:
    """
    Provide skills that can be used based on the Pokémon's type.

    :param pokemon_type: a string representing the type of Pokémon
    :precondition: pokemon_type must be one of Water, Fire, Grass, Electric, Flying, Ice, or Rock
    :postcondition: set up skill collections based on Pokémon's type
    :postcondition: get skills base on the Pokémon's type
    :return: a list containing skills the Pokémon of the given pokemon_type can use
    """
    skills_of = {
        'water': [
            {'name': 'Tackle', 'damage': (1, 3)},
            {'name': 'Water Gun', 'damage': (4, 5)},
            {'name': 'Aqua Jet', 'damage': (6, 7)}
        ],
        'fire': [
            {'name': 'Tackle', 'damage': (1, 3)},
            {'name': 'Flamethrower', 'damage': (4, 5)},
            {'name': 'Fire Punch', 'damage': (6, 7)}
        ],
        'grass': [
            {'name': 'Tackle', 'damage': (1, 3)},
            {'name': 'Seed Bomb', 'damage': (4, 5)},
            {'name': 'Solar Beam', 'damage': (6, 7)}
        ],
        'electric': [
            {'name': 'Tackle', 'damage': (1, 3)},
            {'name': 'Thunderbolt', 'damage': (4, 5)},
            {'name': 'Electro Ball', 'damage': (6, 7)}
        ],
        'flying': [
            {'name': 'Pluck', 'damage': (1, 3)},
            {'name': 'Gust', 'damage': (4, 5)},
            {'name': 'Aerial Ace', 'damage': (6, 7)}
        ],
        'ice': [
            {'name': 'Tackle', 'damage': (1, 3)},
            {'name': 'Blizzard', 'damage': (4, 5)},
            {'name': 'Ice Fang', 'damage': (6, 7)}
        ],
        'rock': [
            {'name': 'Tackle', 'damage': (1, 3)},
            {'name': 'Rock Throw', 'damage': (4, 5)},
            {'name': 'Rock Tomb', 'damage': (6, 7)}
        ]
    }

    return skills_of[pokemon_type]


def customize_user_options(event_type: str, gym_round: Union[int, None] = None) -> list:
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
    character_option = [fight, change_pokemon]
    if event_type == 'Gym Leader':
        if gym_round > 2:
            character_option.append("Run Away")
    else:
        character_option.append(use_potion)
        if event_type == 'wildPokemon':
            character_option.extend([throw_poke_ball, "Run Away"])
    return character_option


def select_event_option(event_type: str, gym_round: Union[int, None] = None) -> Union[Callable[[], None], str]:
    """
    Decide what to do when an event occurs.

    :param event_type: a string that represents what kind of event occurs
    :param gym_round: an integer representing the number of games played
    :param gym_round: None if the event_type is not "Gym Leader"
    :precondition: gym_round must be greater than 0 if its type is an integer
    :precondition: event_type must be either wild Pokémon, Team Rocket, Gym Leader or Strange trainer
    :postcondition: display the options the user can choose from
    :postcondition: get the user's choice of which option the user wants
    :return: a function that represents the option the user wants to do
    :return: a string representing the user's intention to escape the event
    """
    character_option = customize_user_options(event_type, gym_round)

    for number, option in enumerate(character_option):
        name = option if option == "Run Away" else option.__name__.replace("_", " ").title()
        print(f"{number + 1}. {name}")

    while True:
        user_choice = check_input_is_digit("What do you want to do (Enter number)? ")
        if 1 <= user_choice <= len(character_option):
            return character_option[user_choice - 1]
        print(f"\nInvalid choice! Please enter a number between 1 and {len(character_option)}.")


def proceed_event_option(user_choice: Union[Callable[[], None], str], character_pokemon: tuple, character: dict,
                         event_pokemon_info: tuple, event_type: str) -> bool:
    """
    Execute the function corresponding to the user's selected option.

    :param user_choice: a function that represents the option the user wants to do
    :param user_choice: a string representing the user's intention to escape the event
    :param character_pokemon: a tuple containing the user Pokémon's name and a dictionary with its type and current HP
    :param character: a dictionary containing information about the character's status
    :param event_pokemon_info: a tuple containing the event Pokémon's name and a dictionary with its type and current HP
    :param event_type: a string that represents what kind of event occurs
    :precondition: the user Pokémon must have an HP greater than 0 in the character_pokemon
    :precondition: the event Pokémon must have an HP greater than 0 in the event_pokemon_info
    :precondition: character_pokemon represents the status of one of the user's Pokémon in battle
    :precondition: event_type must be either wild Pokémon, Team Rocket, Gym Leader or Strange trainer
    :precondition: user_choice must be either fight, throw_poke_ball, change_pokemon, "Run Away", or use_potion
    :postcondition: execute the function corresponding to the user's selected option
    :postcondition: finish the event if user_choice is "Run Away"
    :return: a boolean value, false if the event has finished, true otherwise
    """
    if user_choice == fight:
        process_result = fight(character_pokemon, event_pokemon_info, character, event_type)
    elif user_choice == throw_poke_ball:
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


def event_occurred(character):
    # docstrings
    event_type = set_event_type()
    process_result = True

    if event_type:
        event_pokemon_info = describe_event(event_type, character)

        character_pokemon = take_out_pokemon(character['Poke Ball'])

        while process_result:
            # Check HP part I would like put like character_pokemon[1]['currentHP']
            print(f"\n{character['Character Name']}'s pokemon status: {character_pokemon[0]}"
                  f"(HP: {character['Poke Ball'][character_pokemon[0]]['currentHP']})\n")

            user_choice = select_event_option(event_type)

            if user_choice == change_pokemon:
                character_pokemon = change_pokemon(character['Poke Ball'], character_pokemon)
            elif user_choice == use_potion:
                use_potion(character, character_pokemon)
            else:
                process_result = proceed_event_option(user_choice, character_pokemon, character,
                                                      event_pokemon_info, event_type)

            if process_result:
                process_result = get_attacked(event_pokemon_info, event_type, character, character_pokemon)
    else:
        print("\nNo event is occurred.")
        print("\n------------------------------------------\n")


def get_user_choice(character, board, rows, columns):
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
    """
    directions = {1: (-1, -0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}

    new_position = None
    if direction in directions:
        dx, dy = directions[direction]
        new_position = (character['Current Location'][0] + dx, character['Current Location'][1] + dy)

        return board.get(new_position, False), new_position

    return False, new_position


def move_character(character: dict, new_position: (int, int), board: dict, rows: int, columns: int):
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


def process_by_location_type(character: dict, board: dict) -> bool:
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


def check_badge_eligibility(character, current_win_count, gym_badge_earned):
    """
    Check if the character is eligible to earn a gym badge.

    :param character: a dictionary representing the character, including their current level
    :param current_win_count: a positive integer representing the character's current number of wins
    :param gym_badge_earned: a boolean representing if the gym badge earned
    :precondition: character is a dictionary with a key "Current Level"
    :precondition: current_win_count is a positive integer
    :param gym_badge_earned: gym_badge_earned is a boolean
    :postcondition: updates gym_badge_earned to True if the character is eligible for the badge
    :return: True if the gym badge is earned, else False
    """
    current_level = character["Current Level"]

    win_count = {1: 2, 2: 3, 3: 4}.get(current_level)
    if win_count is None:
        print("Invalid level")
        return

    count_left_for_badge = win_count - current_win_count

    if count_left_for_badge > 0:
        print(f"\nYou need to win {count_left_for_badge} more time(s) to earn the badge.\n")
        return gym_badge_earned
    else:
        gym_badge_earned = True

    return gym_badge_earned


def has_six_pokemons(character: dict) -> bool:
    """
    Check if the character has six Pokèmons.

    :param character: a dictionary representing character's info, including their Pokèmons' info
    :precondition: character is a dictionary which has Pokèmons' info that the character has
    :postcondition: counts the number of Pokèmons needed to enter the gym
    :return: True if the character has six Pokèmons, otherwise False
    """
    more = 6 - len(character['Poke Ball'])
    if more > 0:
        print(f"You need to earn {more} more pokemon(s) to enter the gym.")

    return not more


def encounter_gym(character):
    gym_badge_earned = False

    while True:
        user_input = input("\nEncountered a gym! Enter y to challenge, n to quit: ")
        if user_input == 'y' or user_input == 'n':
            break

    if user_input == 'n':
        return gym_badge_earned

    print("\nGym Leader: Welcome to the gym! "
          "Here is one rule: you can't use potions to accurately assess your skills.\n")

    gym_badge_earned = battle_with_gym_leader(character, gym_badge_earned)
    return gym_badge_earned


def battle_with_gym_leader(character, gym_badge_earned):
    """
    handle the gtm battle.

    """
    current_win_count, prev_round, gym_round, selected_pokemon, gym_leader_pokemon = initialize_battle(character)
    while prev_round != gym_round and is_alive(character) and not gym_badge_earned:
        process_result = True  # process_result: the ability to continue the game
        prev_round += 1
        display_round_intro(gym_round, gym_leader_pokemon, selected_pokemon, character)
        while process_result:
            user_choice = select_event_option("Gym Leader", gym_round)

            process_result, selected_pokemon, stop_process = (
                handle_user_choice(user_choice, process_result, selected_pokemon, gym_leader_pokemon, character))

            if stop_process:
                break

            if process_result:
                process_result, selected_pokemon, gym_round, stop_process \
                    = check_if_alive_when_lost_the_round(gym_leader_pokemon, character, selected_pokemon, gym_round)
                if stop_process:
                    break
            else:
                current_win_count, gym_badge_earned, gym_round, gym_leader_pokemon = (
                    win_the_round(current_win_count, character, gym_badge_earned, gym_round))
    return gym_badge_earned


def initialize_battle(character):
    current_win_count = 0
    prev_round = 0
    gym_round = 1
    selected_pokemon = take_out_pokemon(character['Poke Ball'])
    gym_leader_pokemon = get_event_pokemon(character)
    return current_win_count, prev_round, gym_round, selected_pokemon, gym_leader_pokemon


def display_round_intro(gym_round, gym_leader_pokemon, selected_pokemon, character):
    print(f"\n❗️Round {gym_round} ❗\n")
    print(f"Event pokemon status: {gym_leader_pokemon[0]}(HP: {gym_leader_pokemon[1]['currentHP']})\n")
    print(f"{character['Character Name']}'s pokemon status: {selected_pokemon[0]}"
          f"(HP: {character['Poke Ball'][selected_pokemon[0]]['currentHP']})\n")


def handle_user_choice(user_choice, process_result, selected_pokemon, gym_leader_pokemon, character):
    stop_process = False
    if user_choice == fight:
        process_result = fight(selected_pokemon, gym_leader_pokemon, character, "Gym Leader")
    elif user_choice == change_pokemon:
        selected_pokemon = change_pokemon(character['Poke Ball'], selected_pokemon)
    elif user_choice == "Run Away":
        print("\nGym Leader: Running away, huh? I guess today's not your day. "
              "Come back when you're ready to battle!")
        stop_process = True
    return process_result, selected_pokemon, stop_process


def check_if_alive_when_lost_the_round(gym_leader_pokemon, character, selected_pokemon, gym_round):
    stop_process = False
    process_result = get_attacked(gym_leader_pokemon, "Gym Leader", character, selected_pokemon)
    if not process_result:
        print(f"\nGym Leader: You lost in round {gym_round}.\n")
        if is_alive(character):
            selected_pokemon = take_out_pokemon(character['Poke Ball'])
            gym_round += 1
        else:
            stop_process = True
    return process_result, selected_pokemon, gym_round, stop_process


def win_the_round(current_win_count, character, gym_badge_earned, gym_round):
    current_win_count += 1
    gym_badge_earned = check_badge_eligibility(character, current_win_count, gym_badge_earned)
    gym_round += 1
    gym_leader_pokemon = get_event_pokemon(character)
    return current_win_count, gym_badge_earned, gym_round, gym_leader_pokemon


def evolve_pokemon(character: dict):
    """
    Evolve character's starting pokèmon based on the character's level.

    :param character: a dictionary including character's info such as their poke ball and starting pokèmon
    :precondition: character is a dictionary including 'Poke Ball', 'Starting Pokemon' keys
    :postcondition: handles starting pokèmon evolution according to the character's level
    """
    evolution_map = {
        'Squirtle': 'Wartortle',
        'Wartortle': 'Blastoise',
        'Charmander': 'Charmeleon',
        'Charmeleon': 'Charizard',
        'Bulbasaur': 'Ivysaur',
        'Ivysaur': 'Venusaur',
    }

    current_starting_pokemon_name = character['Starting Pokemon']
    if current_starting_pokemon_name in evolution_map:
        evolved_starting_pokemon_name = evolution_map[current_starting_pokemon_name]
        available_starting_pokemons = starting_pokemon_collection(character['Current Level'])
        if evolved_starting_pokemon_name in available_starting_pokemons:
            character['Starting Pokemon'] = evolved_starting_pokemon_name
            character['Poke Ball'] = {}
            character['Poke Ball'][evolved_starting_pokemon_name] \
                = available_starting_pokemons[evolved_starting_pokemon_name]
            print(f"\n{current_starting_pokemon_name} has evolved into {evolved_starting_pokemon_name}!")


def level_up(character: dict):
    """
    Level up the character.

    :param character: a dictionary including character's info, such as current level, and other related details
    :preconditoin: character is a dictionary including 'Current Level', 'Money', and other related details
    :postcondition: updates the character's information according to their next level
    """
    character['Current Level'] += 1
    evolve_pokemon(character)

    if character['Current Level'] == 2:
        character['Current Location'] = (0, 0)
        character['Money'] += 50
    elif character['Current Level'] == 3:
        character['Current Location'] = (0, 4)
        character['Money'] += 70
    print(f"You've leveled up to {character['Current Level']}!\n")


def choose_pokemon_to_challenge(character, pokemon_types):
    selected_pokemon = input(f"Choose a pokemon to challenge between {list(character['Balls'].keys())}: ").capitalize()

    if selected_pokemon not in pokemon_types:
        print("Invalid pokemon selection.")
        return False

    print(f"You have chosen {selected_pokemon}")
    return selected_pokemon


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
    # game()
    test_gym()


if __name__ == "__main__":
    main()
