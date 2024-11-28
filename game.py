import random
import copy
from . import POTION_PRICE


def make_character(character_name):
    character = {'Character Name': character_name, 'Money': 30, 'Current Level': 1, 'Potion': 0,
                 'Current Location': (0, 0)}
    starting_pokemon = starting_pokemon_collection(character['Current Level'])
    print("which pokemon would you like to go together?\n")
    print("Squirtle(Water) | Charmander(Fire) | Bulbasaur(Grass)")
    user_choice = input("Please type pokemon name: ").capitalize()
    while user_choice not in starting_pokemon:
        print(f"\n{user_choice} is not included in Starting pokemon")
        user_choice = input("what pokemon would you like? ").capitalize()
    character['Poke Ball'] = {user_choice: starting_pokemon[user_choice]}
    character['Starting Pokemon'] = user_choice
    return character


def print_instructions():
    """
    Print the game instructions.

    :postcondition: displays the game instructions in detail
    """
    print("Welcome to the world of Pokemon! Embark on an exciting journey to become a Pokemon Champion.")
    print("Important notes to know before you begin:")
    print("- Stores are represented by S on the map.")
    print("- Gyms are represented by G on the map.")
    print("- If all six of your Pokémon lose their HP, the game is over.")
    print("- You can only challenge a Gym Leader once you have a full team of six Pokémon.")
    print("- After defeating a Gym Leader, you will earn a Badge, unlocking the next level.")
    print("- Badge Requirements by Level:")
    print("  - Level 1: Defeat the gym leader twice to earn a badge.")
    print("  - Level 2: Defeat the gym leader three times to earn a badge.")
    print("  - Level 3: Defeat the gym leader four times to earn a badge and complete the mission.")
    print("- The mission is complete when you defeat the final Gym Leader at Level 3.")


def generate_store_locations(board):
    """
    Add random stores to the board.

    :param board: a dictionary representing the board
    :precondition: board is a dictionary representing the board
    :postcondition: updates board with randomly generated store locations
    :return: updated board with store locations
    """
    accessible_cells = [key for key, value in board.items() if value is True]
    stores = random.sample(accessible_cells, 3)
    for store in stores:
        board[store] = "Store"
    return board


def make_board(level):
    """
    Make a new game board for the given level.

    :param level: an integer between 1, 2, and 3, representing the current level
    :precondition: level is a positive integer between 1, 2, and 3
    :postcondition: creates a dictionary of new board for the given level
    :return: a dictionary representing the game board
    """
    board = {}

    level_config = {
        1: (6, 6, lambda i, j: (i == 0 and j < 5) or (1 <= i <= 4 and 1 <= j <= 4) or (i == 5 and j > 0), (5, 5)),
        2: (8, 5, lambda i, j: (i == 0 and j == 0) or (1 <= i <= 6 and 0 <= j <= 4) or (i == 7 and j == 4), (7, 4)),
        3: (10, 5, lambda i, j: (i == 0 and j == 4) or (1 <= i <= 8 and 0 <= j <= 4) or (i == 9 and j == 0), (9, 0)),
    }

    if level not in level_config:
        return board

    rows, columns, is_accessible, gym_location = level_config[level]

    for i in range(rows):
        for j in range(columns):
            board[(i, j)] = True if is_accessible(i, j) else False

    board[gym_location] = "Gym"

    board = generate_store_locations(board)

    return board, rows, columns


def display_current_location(board, character, rows, columns):
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
    :postcondition: prints the current location of character, store, and gym location
    """
    if not board:
        return

    for i in range(rows):
        row = ""
        for j in range(columns):
            location = board.get((i, j), False)

            if location is False:
                row += "   "
            elif (i, j) == character["Current Location"]:
                row += "[#]"
            elif location == "Store":
                row += "[S]"
            elif location == "Gym":
                row += "[G]"
            else:
                row += "[ ]"
        print(row)


def check_current_location(board, character):
    """
    Check the current location of the game board.

    :param board: a dictionary representing the game board
    :param character: a dictionary representing the character
    :precondition: board is a dictionary representing the game board
    :precondition: character is a dictionary representing the character
    :postcondition: retrieves the description of current location from the board
    :return: the description of current location between True, False, Store, and Gym
    """
    return board[character["Current Location"]]


def is_alive(character):
    """
    Check if the character is alive

    :param character: a dictionary representing character, including their pokemon
    :precondition: character is a dictionary with a key "Balls" including pokemon's HP
    :postcondition: returns True if at least one pokemon has HP greater than 0, else False
    :return: True if the character is alive, else False
    """
    alive = True

    if not any(pokemon['Current HP'] > 0 for pokemon in character["Balls"].values()):
        alive = False

    return alive


def buy_potion(character):
    """
    Calculate the change after a purchase.

    :param character: a dictionary representing character, including their money
    :precondition: character is a dictionary with a key "Money" representing the character's current budget
    :postcondition: updates the character's money if a potion is purchased
    """
    user_input = input("Enter 'y' to buy a potion or 'n' to skip: ")

    if user_input != 'y':
        return

    budget = character["Money"]
    change = budget - POTION_PRICE

    if change >= 0:
        print(f"Purchase successful! Your change is ${change}.")
        character["Money"] = change
    else:
        print("You can't buy with your current budget.")


def starting_pokemon_collection(character_level):
    level1_starting_pokemon = {'Squirtle': {'type': 'water', 'currentHP': 30},
                               'Charmander': {'type': 'fire', 'currentHP': 30},
                               'Bulbasaur': {'type': 'grass', 'currentHP': 30}}

    level2_starting_pokemon = {'Wartortle': {'type': 'water', 'currentHP': 50},
                               'Charmeleon': {'type': 'fire', 'currentHP': 50},
                               'Ivysaur': {'type': 'grass', 'currentHP': 50}}

    level3_starting_pokemon = {'Blastoise': {'type': 'water', 'currentHP': 80},
                               'Charizard': {'type': 'fire', 'currentHP': 80},
                               'Venusaur': {'type': 'grass', 'currentHP': 80}}

    pokemon_collection = current_pokemon_collection(character_level, level1_starting_pokemon,
                                                    level2_starting_pokemon, level3_starting_pokemon)

    return pokemon_collection


def current_pokemon_collection(character_level, level1, level2, level3):
    if character_level == 2:
        current_level_collection = level2
    elif character_level == 3:
        current_level_collection = level3
    else:
        current_level_collection = level1

    return current_level_collection


def event_pokemon(character_level):
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


def choose_skill_to_challenge(skill_collection):
    number = 1
    print("")
    for skill in skill_collection:
        print(f"{number}. {skill['name']}(damage range: {skill['damage'][0]} ~ {skill['damage'][1]})")
        number += 1
    user_choice = int(input("Which skill would you like to use (Entering number)? "))
    while user_choice not in range(1, 4):
        print(f"{user_choice} is not a valid skill choice")
        user_choice = int(input("Please choose a valid skill (Entering number): "))
    return skill_collection[user_choice - 1]


def get_probability():
    return random.choices([True, False], weights=[3, 1], k=1)[0]


def level_maximum_hp(character):
    if character['User Level'] == 1:
        maximum_hp = 30
    elif character['User Level'] == 2:
        maximum_hp = 50
    else:
        maximum_hp = 80
    return maximum_hp


def make_stronger(character_level):
    if character_level == 2:
        stronger = 1.3
    elif character_level == 3:
        stronger = 1.5
    else:
        stronger = 1
    return stronger


def get_money(character, event_type):
    money = make_stronger(character['Current Level'])
    if event_type == 'wildPokemon':
        money *= random.randrange(3, 7)
    elif event_type == 'Team Rocket':
        money *= random.randrange(11, 15)
    else:
        money *= random.randrange(7, 11)
    character['Money'] += money
    print(f"You got {money}!")


def get_attack_result(user_pokemon_skill, event_pokemon_info, character, event_type):
    print(f"\n{user_pokemon_skill['name']} hit!")

    damage = make_stronger(character['Current Level']) * random.randrange(
        user_pokemon_skill['damage'][0], user_pokemon_skill['damage'][1] + 1)

    event_pokemon_info['currentHP'] -= damage

    if event_pokemon_info['currentHP'] <= 0:
        print(f"You defeated the {event_pokemon_info[0]}")
        get_money(character, event_type)
        return False
    else:
        print(f"{event_pokemon_info[0]}(HP: {event_pokemon_info[1]['currentHP']})\n")
        return True


def fight(character_pokemon, event_pokemon_info, event_type):
    print(f"{event_pokemon_info[0]}(HP: {event_pokemon_info[1]['currentHP']})\n")
    skill_collection = get_skill_of(character_pokemon[1]['type'])
    user_pokemon_skill = choose_skill_to_challenge(skill_collection)
    skill_accuracy = get_probability()
    if skill_accuracy:
        return get_attack_result(user_pokemon_skill, event_pokemon_info, event_type)
    else:
        print(f"\n{user_pokemon_skill['name']} missed!")
        return True


def change_pokemon(character, user_pokemon):
    if len(character['Poke Ball']) == 1:
        print("\nYou has no pokemon to switch to\n")
    else:
        print("\nYour pokemons' status...")
        for pokemon in character['Poke Ball'].keys():
            print(f"{pokemon}(HP: {character['Poke Ball'][pokemon]['currentHP']})")

        user_choice = input("\nwhat pokemon would you like to switch to (Entering Pokemon name)? ").capitalize()
        while user_choice not in character['Poke Ball'].keys() or character['Poke Ball'][user_choice]['currentHP'] == 0:
            print(f"\n{user_choice} is not included in your Poke Balls or has 0HP")
            user_choice = input("what pokemon would you like (Entering Pokemon name)? ").capitalize()

        print(f"\nGood job, {user_pokemon}! Come back!")
        print(f"Go, {user_choice}")

        user_pokemon = user_choice
        print(f"{user_choice}(HP: {character['Poke Ball'][user_choice]['currentHP']})\n")

    return user_pokemon


def check_potion(character, user_pokemon):
    validation = False
    if character['Potion'] == 0:
        print("\nYou don't have any potion!\n")
    elif character['Poke Ball'][user_pokemon]['currentHP'] == level_maximum_hp(character):
        print(f"\n{user_pokemon} has full HP!\n")
    else:
        validation = True
    return validation


def use_potion(character, user_pokemon):
    if check_potion(character, user_pokemon):
        print(f"\nYou have {character['Potion']} potion(s)!\n{user_pokemon} has "
              f"{character['Poke Ball'][user_pokemon]['currentHP']}.")
        user_answer = input("Would you like to use a potion (y/n)? ").lower()
        while user_answer not in ['y', 'n']:
            print(f"\n{user_answer} is not a valid option")
            user_answer = input("Please choose a valid option (y/n): ").lower()
        if user_answer == 'y':
            if character['Poke Ball'][user_pokemon]['currentHP'] >= 15:
                character['Poke Ball'][user_pokemon]['currentHP'] = level_maximum_hp(character)
            else:
                character['Poke Ball'][user_pokemon]['currentHP'] += 5
            character['potion'] -= 1
            print(f"\n{user_pokemon} restored HP!\n{user_pokemon} "
                  f"(HP: {character['Poke Ball'][user_pokemon]['currentHP']}\n{character['potion']} potion(s) left!")


def select_release_pokemon(character):
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


def throw_poke_ball(event_pokemon_info, character):
    process_result = False
    if event_pokemon_info[1]['currentHP'] <= 5:
        if len(character['Poke Ball']) == 6:
            user_choice = input("\nYou can only carry up to 6 Pokémon. Would you like to release one (y/n)? ").lower()
            while user_choice not in ['y', 'n']:
                print(f"\n{user_choice} is not a valid option")
                user_choice = input("Please choose a valid option (y/n): ").lower()
            if user_choice == 'y':
                select_release_pokemon(character, event_pokemon_info)
            else:
                print(f"\n{event_pokemon_info[0]} broke free!")
        character['Poke Ball'][event_pokemon_info[0]] = {'type': event_pokemon_info[1]['type'],
                                                         'currentHP': level_maximum_hp(character) / 2}
        print(f"\nGotcha! {event_pokemon_info[0]} was caught!")
    else:
        print("\nShoot! It was so close, too!")
        process_result = get_probability()
    return process_result


def set_event_type():
    event_collection = ("wildPokemon", "Team Rocket", "Strange trainer", False)
    return random.choices(event_collection, weights=[4, 3, 4, 2], k=1)[0]


def get_event_pokemon(character_level):
    event_pokemon_collection = event_pokemon(character_level)
    return copy.deepcopy(random.choices(list(event_pokemon_collection.items()), k=1)[0])


def take_out_pokemon(character_pokemons):
    player_pokemon = random.choice(
        list(character_pokemons.items()))
    print(player_pokemon)
    while player_pokemon[1]['currentHP'] == 0:
        player_pokemon = random.choice(list(character_pokemons.items()))
    print(f"Go, {player_pokemon[0]}!")
    return player_pokemon


def get_skill_of(pokemon_type):
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


def select_event_option(event_type):
    character_option = [fight, change_pokemon, use_potion]  # change list type to dictionary
    if event_type == 'wildPokemon':
        character_option.extend([throw_poke_ball, "Run"])

    for print_option in range(len(character_option)):
        if print_option == 4:
            print(f"{print_option + 1}. {character_option[print_option]}")
        else:
            print(f"{print_option + 1}. {character_option[print_option].__name__.replace("_", " ").title()}")

    user_choice = int(input("What do you want to do (Entering number)? "))
    while user_choice <= 0 or user_choice > len(character_option):
        print("\nThat is not option you can choose!")
        user_choice = input("Please choose valid option(Entering number): ")

    return character_option[user_choice - 1]


def proceed_event_option(user_choice, character_pokemon, character, event_pokemon_info, event_type):
    if user_choice == fight:
        process_result = fight(character_pokemon, event_pokemon_info, event_type)
    elif user_choice == throw_poke_ball:
        process_result = throw_poke_ball(event_pokemon_info, character)
    else:
        print(f"\nYou escaped from {event_pokemon_info[0]}!")
        process_result = False
    return process_result


def set_times(event_type=None, character=None):
    if event_type == 'Team Rocket' or character['User Level'] == 3:
        times = 1.5
    elif event_type == 'Strange trainer' or character['User Level'] == 2:
        times = 1.3
    else:
        times = 1
    return times


def check_status(character, user_pokemon):
    if character['Poke Ball'][user_pokemon]['currentHP'] <= 0:
        character['Poke Ball'][user_pokemon]['currentHP'] = 0
        print(f"{user_pokemon} fainted!")
        status = False
    else:
        status = True
    return status


def get_attacked(event_pokemon_info, event_type, character, user_pokemon):
    skill_collection = get_skill_of(event_pokemon_info[1]['type'])
    event_pokemon_skill = random.choices(list(skill_collection), k=1)[0]
    damage = set_times(event_type)
    damage *= random.choice(range(event_pokemon_skill['damage'][0], event_pokemon_skill['damage'][1] + 1))
    skill_accuracy = get_probability()
    print(f"{event_pokemon_info[0]} used {event_pokemon_skill['name']}!\n")
    if skill_accuracy:
        print(f"{event_pokemon_skill['name']} hit!")
        character['Poke Ball'][user_pokemon]['currentHP'] -= damage
        print(f"{user_pokemon} took {damage} damage!")
    else:
        print(f"{event_pokemon_skill['name']} missed!")
    process_result = check_status(character, user_pokemon)
    return process_result


def describe_event(event_type, character_level):
    event_pokemon_info = get_event_pokemon(character_level)
    if event_type == "wildPokemon":
        print(f"\nA wild {event_pokemon_info[0]} appeared!(HP: {event_pokemon_info[1]['currentHP']})\n")
    else:
        print(f"\nYou encountered a {event_type}!\n{event_type} sent out {event_pokemon_info[0]}!"
              f"(HP: {event_pokemon_info[1]['currentHP']})\n")
    return event_pokemon_info


def event_occurred(character):
    event_type = set_event_type()
    process_result = True

    if event_type:
        event_pokemon_info = describe_event(event_type, character['Current Level'])

        character_pokemon = take_out_pokemon(character['Poke Ball'])

        while process_result:
            # Check HP part I would like put like character_pokemon[1]['currentHP']
            print(f"Current status: {character_pokemon[0]}"
                  f"(HP: {character['Poke Ball'][character_pokemon[0]]['currentHP']})\n")

            user_choice = select_event_option(event_type)

            if user_choice == change_pokemon:
                character_pokemon = change_pokemon(character, character_pokemon)
            elif user_choice == use_potion:
                use_potion(character, character_pokemon)
            else:
                process_result = proceed_event_option(user_choice, character_pokemon, character,
                                                      event_pokemon_info, event_type)

            if process_result:
                process_result = get_attacked(event_pokemon_info, event_type, character, character_pokemon)


def get_user_choice():
    print("1. Up \n 2. Down \n 3. Left \n 4. Right")
    user_choice = int(input("Which direction would you like to go (Entering number)? "))
    while user_choice not in range(1, 5):
        print("\nPlease, choose a valid direction!")
        user_choice = int(input("What direction would you like to go (Entering number)? "))
    return user_choice


def validate_move(board, character, direction):
    user_row = character['Current Location'][0]
    user_col = character['Current Location'][1]

    if direction == 1:
        user_col -= 1
    elif direction == 2:
        user_col += 1
    elif direction == 3:
        user_row -= 1
    else:
        user_row += 1

    if (user_row, user_col) in board:
        return True
    else:
        return False


def move_character(character, direction):
    if direction == 1:
        character['Current Location'][1] -= 1
    elif direction == 2:
        character['Current Location'][1] += 1
    elif direction == 3:
        character['Current Location'][0] -= 1
    else:
        character['Current Location'][0] += 1


def game():
    character = make_character()
    event_occurred(character)


def battle_with_gym_leader(character):
    """
    Drive the battle with gym leader.

    Give character a gym badge if they win, else do not.

    :param character: a dictionary including character's current level and other related details
    :precondition: character is a dictionary including Current Location, Current Level, Current EXP, Money, and Balls
    :postcondition: return True if the battle wins else False
    :return: True if the battle wins else False
    """
    gym_badges = {'Level 1': False, 'Level 2': False,
                  'Level 3': False}  # level 1에서 2번, level 2에서 3번, level 3에서 4번, -> 레벨업
    is_gym_badge_earned = False
    user_input = input("Encountered a gym! Enter y to challenge, n to quit: ")
    if user_input == 'n':
        return False
    print("Gym Leader: Welcome to the gym! Here is one rule, you can't use potions to accurately assess your skills.")

    pokemon_types = {
        'Charmander': 'fire',
        'Pikachu': 'electric',
        'Caterpie': 'grass',
        'Pidove': 'flying',
        'Slowpoke': 'water',
        'Horsea': 'water'
    }

    selected_pokemon = choose_pokemon_to_challenge(character, pokemon_types)

    gym_leader_pokemon = generate_gym_leader_pokemon()

    # TODO: decompose, function name: choose_skills()
    pokemon_type = pokemon_types[selected_pokemon]
    skills_of_selected_pokemon = get_skill_of(pokemon_type)
    skill_names = [skill['name'] for skill in skills_of_selected_pokemon]

    while character['Balls'][selected_pokemon]['Current HP'] > 0 and gym_leader_pokemon['Current HP'] > 0:
        user_input = input(f"Choose a skill between {skill_names}: ")

        selected_skill = next((skill for skill in skills_of_selected_pokemon if skill['name'] == user_input), None)

        # TODO: decompose, function name: battle_with_gym_leader()
        if selected_skill:
            damage_to_gym_leader = selected_skill['damage']
            gym_leader_pokemon['Current HP'] -= damage_to_gym_leader
            print(f"You used {user_input}! It dealt {damage_to_gym_leader} damage.")
            print(f"Gym Leader's {gym_leader_pokemon['name']} HP: {max(gym_leader_pokemon['Current HP'], 0)}")
        else:
            print("Invalid skill selection. Try again.")
            continue

        if gym_leader_pokemon['Current HP'] > 0:
            damage_from_gym_leader = random.choice([3, 5, 7])
            character['Balls'][selected_pokemon]['Current HP'] -= damage_from_gym_leader
            print(f"Gym Leader's {gym_leader_pokemon['name']} attacked! You took {damage_from_gym_leader} damage.")
            print(f"Your {selected_pokemon}'s HP: {max(character['Balls'][selected_pokemon]['Current HP'], 0)}")

    # TODO: decompose, function name: result_of_battle()
    if character['Balls'][selected_pokemon]['Current HP'] <= 0:
        print(f"Your {selected_pokemon} fainted! You couldn't won the gym badge.")
    elif gym_leader_pokemon['Current HP'] <= 0:
        gym_badges[character['Current Level']] = True
        is_gym_badge_earned = True
        character['Current Level'] += 1
        print(f"Gym leader's {gym_leader_pokemon['name']} fainted. You won the gym badge!")
    return is_gym_badge_earned


def choose_pokemon_to_challenge(character, pokemon_types):
    selected_pokemon = input(f"Choose a pokemon to challenge between {list(character['Balls'].keys())}: ").capitalize()

    if selected_pokemon not in pokemon_types:
        print("Invalid pokemon selection.")
        return False

    print(f"You have chosen {selected_pokemon}")
    return selected_pokemon


def generate_gym_leader_pokemon():
    gym_leader_pokemons = [
        {'name': 'Bulbasaur', 'type': 'grass', 'Current HP': 20},
        {'name': 'Squirtle', 'type': 'water', 'Current HP': 20},
        {'name': 'Pidgeotto', 'type': 'flying', 'Current HP': 20},
        {'name': 'Growlithe', 'type': 'fire', 'Current HP': 20},
        {'name': 'Raichu', 'type': 'electric', 'Current HP': 20},
    ]
    return random.choice(gym_leader_pokemons)


def main():
    """
    Drive the program.
    """
    # game()
    character = {
        "Current Location": (5, 2),
        "Current Level": 1,
        "Current EXP": 20,
        "Money": 10,
        "Balls": {
            'Charmander': {'Current HP': 20},
            'Pikachu': {'Current HP': 20},
            'Caterpie': {'Current HP': 20},
            'Pidove': {'Current HP': 20},
            'Slowpoke': {'Current HP': 20},
            'Horsea': {'Current HP': 20}
        }
    }
    board, rows, columns = make_board(character["Current Level"])
    display_current_location(board, character, rows, columns)
    print(check_current_location(board, character))
    # battle_with_gym_leader(character)
    # print_instructions()


if __name__ == "__main__":
    main()
