import random
import copy


def make_character():
    character = {'Money': 30, 'User Level': 1, 'Potion': 0, 'Current Location': (0, 0)}
    starting_pokemon = {'Squirtle': {'type': 'water', 'currentHP': 20},
                        'Charmander': {'type': 'fire', 'currentHP': 20},
                        'Bulbasaur': {'type': 'grass', 'currentHP': 20}}
    print("which pokemon would you like to go together?\n")
    print("Squirtle(Water) | Charmander(Fire) | Bulbasaur(Grass)")
    user_choice = input("Please type pokemon name: ").capitalize()
    while user_choice not in starting_pokemon:
        print(f"\n{user_choice} is not included in Starting pokemon")
        user_choice = input("what pokemon would you like? ").capitalize()
    character['Poke Ball'] = {user_choice: starting_pokemon[user_choice]}
    character['Starting Pokemon'] = user_choice
    return character


def event_pokemon(user_level):
    level1_pokemon = {'Pichu': {'type': 'electric', 'currentHP': 20},
                      'Shinx': {'type': 'electric', 'currentHP': 20},
                      'Mareep': {'type': 'electric', 'currentHP': 20},
                      'Caterpie': {'type': 'grass', 'currentHP': 20},
                      'Weedle': {'type': 'grass', 'currentHP': 20},
                      'Treecko': {'type': 'grass', 'currentHP': 20},
                      'Pidgey': {'type': 'flying', 'currentHP': 20},
                      'Pidove': {'type': 'flying', 'currentHP': 20},
                      'Slowpoke': {'type': 'water', 'currentHP': 20},
                      'Horsea': {'type': 'water', 'currentHP': 20},
                      'Mudkip': {'type': 'water', 'currentHP': 20},
                      'Cyndaquil': {'type': 'fire', 'currentHP': 20},
                      'Totodile': {'type': 'fire', 'currentHP': 20},
                      'Magby': {'type': 'fire', 'currentHP': 20},
                      'Swinub': {'type': 'ice', 'currentHP': 20},
                      'Spheal': {'type': 'ice', 'currentHP': 20},
                      'Vanillite': {'type': 'ice', 'currentHP': 20},
                      'Geodude': {'type': 'rock', 'currentHP': 20},
                      'Aron': {'type': 'rock', 'currentHP': 20},
                      'Roggenrola': {'type': 'rock', 'currentHP': 20}}

    level2_pokemon = {'Pikachu': {'type': 'electric', 'currentHP': 40},
                      'Luxio': {'type': 'electric', 'currentHP': 40},
                      'Flaaffy': {'type': 'electric', 'currentHP': 40},
                      'Metapod': {'type': 'grass', 'currentHP': 40},
                      'Kakuna': {'type': 'grass', 'currentHP': 40},
                      'Grovyle': {'type': 'grass', 'currentHP': 40},
                      'Pidgeotto': {'type': 'flying', 'currentHP': 40},
                      'Tranquill': {'type': 'flying', 'currentHP': 40},
                      'Slowbro': {'type': 'water', 'currentHP': 40},
                      'Seadra': {'type': 'water', 'currentHP': 40},
                      'Marshtomp': {'type': 'water', 'currentHP': 40},
                      'Quilava': {'type': 'fire', 'currentHP': 40},
                      'Croconaq': {'type': 'fire', 'currentHP': 40},
                      'Magmar': {'type': 'fire', 'currentHP': 40},
                      'Piloswine': {'type': 'ice', 'currentHP': 40},
                      'Sealeo': {'type': 'ice', 'currentHP': 40},
                      'Vanillish': {'type': 'ice', 'currentHP': 40},
                      'Graveler': {'type': 'rock', 'currentHP': 40},
                      'Lairon': {'type': 'rock', 'currentHP': 40},
                      'Boldore': {'type': 'rock', 'currentHP': 40}}

    level3_pokemon = {'Raichu': {'type': 'electric', 'currentHP': 70},
                      'Luxray': {'type': 'electric', 'currentHP': 70},
                      'Ampharos': {'type': 'electric', 'currentHP': 70},
                      'Butterfree': {'type': 'grass', 'currentHP': 70},
                      'Beedrill': {'type': 'grass', 'currentHP': 70},
                      'Sceptile': {'type': 'grass', 'currentHP': 70},
                      'Pidgeot': {'type': 'flying', 'currentHP': 70},
                      'Pidove': {'type': 'flying', 'currentHP': 70},
                      'Slowking': {'type': 'water', 'currentHP': 70},
                      'Kingdra': {'type': 'water', 'currentHP': 70},
                      'Swampert': {'type': 'water', 'currentHP': 70},
                      'Typhlosion': {'type': 'fire', 'currentHP': 70},
                      'Reraligatr': {'type': 'fire', 'currentHP': 70},
                      'Magmortar': {'type': 'fire', 'currentHP': 70},
                      'Mamoswine': {'type': 'ice', 'currentHP': 70},
                      'Walrein': {'type': 'ice', 'currentHP': 70},
                      'Vanilluxe': {'type': 'ice', 'currentHP': 70},
                      'Golem': {'type': 'rock', 'currentHP': 70},
                      'Aggron': {'type': 'rock', 'currentHP': 70},
                      'Gigalith': {'type': 'rock', 'currentHP': 70}}
    current_user_level = level1_pokemon

    if user_level == 2:
        current_user_level = level2_pokemon
    elif user_level == 3:
        current_user_level = level3_pokemon

    return current_user_level


def choose_skill_to_challenge(skill_collection):
    number = 1
    print("")
    for skill in skill_collection:
        print(f"{number}. {skill['name']}(damage range: {skill['damage'][0]} ~ {skill['damage'][1]})")
        number += 1
    user_choice = input("Which skill would you like to use (Entering skill name)? ").title()
    while user_choice not in [userSkill['name'] for userSkill in skill_collection]:
        print(f"{user_choice} is not a valid skill choice")
        user_choice = input("Please choose a valid skill (Entering skill name): ").title()
    return user_choice


def get_possibility():
    return random.choices([True, False], weights=[3, 1], k=1)[0]


def level_maximum_hp(character):
    if character['User Level'] == 1:
        maximum_hp = 20
    elif character['User Level'] == 2:
        maximum_hp = 40
    else:
        maximum_hp = 70
    return maximum_hp


def skill_result(user_pokemon_skill, skill_collection, event_pokemon_info, character):
    print(f"\n{user_pokemon_skill} hit!")

    damage = random.randrange(skill_collection[user_pokemon_skill]['damage'][0],
                              skill_collection[user_pokemon_skill]['damage'][1] + 1)
    event_pokemon_info['currentHP'] -= damage

    if event_pokemon_info['currentHP'] <= 0:
        event_pokemon_info['currentHP'] = level_maximum_hp(character)
        print(f"You defeated the {event_pokemon_info[0]}")
        return False
    else:
        print(f"{event_pokemon_info[0]}(HP: {event_pokemon_info[1]['currentHP']})\n")
        return True


def fight(user_pokemon, event_pokemon_info, character):
    skill_collection = get_skill_of(character['Poke Ball'][user_pokemon]['type'])
    user_pokemon_skill = choose_skill_to_challenge(skill_collection)
    skill_accuracy = get_possibility()
    if skill_accuracy:
        return skill_result(user_pokemon_skill, skill_collection, event_pokemon_info, character)
    else:
        print(f"\n{user_pokemon_skill} missed!")
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
        process_result = get_possibility()
    return process_result


def set_event_type():
    event_collection = ("wildPokemon", "Team Rocket", "Strange trainer", False)
    return random.choices(event_collection, weights=[4, 3, 4, 2], k=1)[0]


def get_event_pokemon(character):
    event_pokemon_collection = event_pokemon(character['User Level'])
    return copy.deepcopy(random.choices(list(event_pokemon_collection.items()), k=1)[0])


def take_out_pokemon(character):
    player_pokemon = random.choice(list(character['Poke Ball'].keys()))  # change way to save player pokemon info(with type and HP)
    while character['Poke Ball'][player_pokemon]['currentHP'] == 0:
        player_pokemon = random.choice(list(character['Poke Ball'].keys()))
    print(f"Go, {player_pokemon}!")
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
    user_option = [fight, change_pokemon, use_potion]  # change list type to dictionary
    if event_type == 'wildPokemon':
        user_option.extend([throw_poke_ball, "Run"])

    for print_option in range(len(user_option)):
        if print_option == 4:
            print(f"{print_option + 1}. {user_option[print_option]}")
        else:
            print(f"{print_option + 1}. {user_option[print_option].__name__.replace("_", " ").title()}")

    user_choice = int(input("What do you want to do (Entering number)? "))
    while user_choice <= 0 or user_choice > len(user_option):
        print("\nThat is not option you can choose!")
        user_choice = input("Please choose valid option(Entering number): ")

    return user_option[user_choice - 1]


def proceed_event_option(user_choice, user_pokemon, character, event_pokemon_info):
    if user_choice == fight:
        process_result = fight(user_pokemon, event_pokemon_info, character)
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
    skill_accuracy = get_possibility()
    print(f"{event_pokemon_info[0]} used {event_pokemon_skill['name']}!\n")
    if skill_accuracy:
        print(f"{event_pokemon_skill['name']} hit!")
        character['Poke Ball'][user_pokemon]['currentHP'] -= damage
        print(f"{user_pokemon} took {damage} damage!")
    else:
        print(f"{event_pokemon_skill['name']} missed!")
    process_result = check_status(character, user_pokemon)
    return process_result


def event_occurred(character):
    event_type = set_event_type()
    process_result = True

    if event_type:
        event_pokemon_info = get_event_pokemon(character)
        if event_type == "wildPokemon":
            print(f"\nA wild {event_pokemon_info[0]} appeared!(HP: {event_pokemon_info[1]['currentHP']})\n")
        else:
            print(f"\nYou encountered a {event_type}!\n{event_type} sent out {event_pokemon_info[0]}!"
                  f"(HP: {event_pokemon_info[1]['currentHP']})\n")

        user_pokemon = take_out_pokemon(character)

        while process_result:
            print(f"{user_pokemon}(HP: {character['Poke Ball'][user_pokemon]['currentHP']})\n")

            user_choice = select_event_option(event_type)

            if user_choice == change_pokemon:
                user_pokemon = change_pokemon(character, user_pokemon)
            elif user_choice == use_potion:
                use_potion(character, user_pokemon)
            else:
                process_result = proceed_event_option(user_choice, user_pokemon, character, event_pokemon_info)

            if process_result:
                process_result = get_attacked(event_pokemon_info, event_type, character, user_pokemon)


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


def make_board(level):
    """
    Make a new game board.

    :param level: an integer (1, 2, or 3) representing character's current level
    :precondition: level is greater than 0
    :postcondition: returns board for the given level
    :return: board for the given level

    >>> make_board(1)
    {(0, 0): 'Empty room', (0, 1): 'Empty room', (0, 2): 'Empty room', (0, 3): 'Empty room', (0, 4): 'Empty room',
    (1, 1): 'Empty room', (1, 2): 'Empty room', (1, 3): 'Empty room', (1, 4): 'Empty room', (2, 1): 'Empty room',
    (2, 2): 'Empty room', (2, 3): 'Empty room', (2, 4): 'Empty room', (3, 1): 'Empty room', (3, 2): 'Empty room',
    (3, 3): 'Empty room', (3, 4): 'Empty room', (4, 1): 'Empty room', (4, 2): 'Empty room', (4, 3): 'Empty room',
    (4, 4): 'Empty room', (5, 1): 'Empty room', (5, 2): 'Empty room', (5, 3): 'Empty room', (5, 4): 'Empty room',
    (5, 5): 'Empty room'}
    """
    board = {}

    layout = []
    if level == 1:
        layout.append([True, True, True, True, True, False])
        layout.append([False, True, True, True, True, False])
        layout.append([False, True, True, True, True, False])
        layout.append([False, True, True, True, True, False])
        layout.append([False, True, True, True, True, False])
        layout.append([False, True, True, True, True, True])
    elif level == 2:
        layout.append([True, False, False, False, False])
        layout.append([True, True, True, True, True])
        layout.append([True, True, True, True, True])
        layout.append([True, True, True, True, True])
        layout.append([True, True, True, True, True])
        layout.append([True, True, True, True, True])
        layout.append([True, True, True, True, True])
        layout.append([False, False, False, False, True])
    elif level == 3:
        layout.append([False, False, False, False, True])
        layout.append([True, True, True, True, True])
        layout.append([True, True, True, True, True])
        layout.append([True, True, True, True, True])
        layout.append([True, True, True, True, True])
        layout.append([True, True, True, True, True])
        layout.append([True, True, True, True, True])
        layout.append([True, True, True, True, True])
        layout.append([True, True, True, True, True])
        layout.append([True, False, False, False, False])
    else:
        return board

    rows = len(layout)
    columns = len(layout[0])

    for i in range(rows):
        for j in range(columns):
            if layout[i][j]:
                board[(i, j)] = 'Empty room'

    return board


def display_current_location(board, character):
    """
    Display character's current location.

    :param board: a dictionary representing the game board
    :param character: a dictionary including character's current location and other related details
    :precondition: board is a dictionary where each key is a tuple representing coordinates (rows, columns),
                    and each value is a short string description of the coordinates
    :precondition: character is a dictionary including Current Location, Current Level, Current EXP, Money, and Balls
    :postcondition: prints the game board and character's current location with 'U'

    >>> test_board = {(0, 0): 'Empty room', (0, 1): 'Empty room', (0, 2): 'Empty room', (0, 3): 'Empty room',
    ... (0, 4): 'Empty room', (1, 1): 'Empty room', (1, 2): 'Empty room', (1, 3): 'Empty room', (1, 4): 'Empty room',
    ... (2, 1): 'Empty room', (2, 2): 'Empty room', (2, 3): 'Empty room', (2, 4): 'Empty room', (3, 1): 'Empty room',
    ... (3, 2): 'Empty room', (3, 3): 'Empty room', (3, 4): 'Empty room', (4, 1): 'Empty room', (4, 2): 'Empty room',
    ... (4, 3): 'Empty room', (4, 4): 'Empty room', (5, 1): 'Empty room', (5, 2): 'Empty room', (5, 3): 'Empty room',
    ... (5, 4): 'Empty room', (5, 5): 'Empty room'}
    >>> test_character = {
    ...     "Current Location": (1, 3),
    ...     "Current EXP": 20,
    ...     "Money": 10,
    ...     "Balls": {
    ...         'Charmander': {'Current HP': 20},
    ...         'Pikachu': {'Current HP': 20},
    ...         'Caterpie': {'Current HP': 20},
    ...         'Pidove': {'Current HP': 20},
    ...         'Slowpoke': {'Current HP': 20},
    ...         'Horsea': {'Current HP': 20}
    ...     }
    ... }
    >>> display_current_location(test_board, test_character)
    [ ][ ][ ][ ][ ]
       [ ][ ][U][ ]
       [ ][ ][ ][ ]
       [ ][ ][ ][ ]
       [ ][ ][ ][ ]
       [ ][ ][ ][ ][ ]
    """
    if board == {}:
        return

    rows = max(pos[0] for pos in board.keys()) + 1
    columns = max(pos[1] for pos in board.keys()) + 1

    for i in range(rows):
        row = ""
        for j in range(columns):
            if (i, j) in board:
                if (i, j) == character["Current Location"]:
                    row += "[U]"  # User's position
                else:
                    row += "[ ]"  # Empty room
            else:
                row += "   "  # No room
        print(row)


def buy_portion():
    """
    Calculate the change after a purchase.

    :postcondition: returns the change after a purchase, or 0 if the user skips
    :return: change after a purchase, or 0 if the user skips
    """
    price = 10
    print(f"Encountered a store! The portion costs ${price}.")
    while True:
        user_input = input(f"Enter {price} or more to buy, or 0 to skip: ")
        budget = int(user_input)
        if budget == 0:
            break
            # print("You chose not to proceed with the purchase.")
            # return budget

        change = budget - price
        if change < 0:
            print("Invalid input.")
            # or
            # print("Insufficient funds. You can't buy this item.")
        else:
            print(f"Purchase successful! Your change is ${change}.")
            return change


def battle_with_gym_leader(character):
    """
    Drive the battle with gym leader.

    Give character a gym badge if they win, else do not.

    :param character: a dictionary including character's current level and other related details
    :precondition: character is a dictionary including Current Location, Current Level, Current EXP, Money, and Balls
    :postcondition: return True if the battle wins else False
    :return: True if the battle wins else False
    """
    gym_badges = {'Level 1': False, 'Level 2': False, 'Level 3': False}
    is_gym_badge_earned = False
    user_input = input("Encountered a gym! Enter y to challenge, n to quit: ")
    if user_input == 'n':
        return False
    print("Gym Leader: Welcome to the gym! Here is one rule, you can't use potions to accurately assess your skills.")

    gym_leader_pokemons = {
        'Bulbasaur': {'type': 'grass', 'Current HP': 20},
        'Squirtle': {'type': 'water', 'Current HP': 20},
        'Pidgeotto': {'type': 'flying', 'Current HP': 20},
        'Growlithe': {'type': 'fire', 'Current HP': 20},
        'Raichu': {'type': 'electric', 'Current HP': 20}
    }

    pokemon_types = {
        'Charmander': 'fire',
        'Pikachu': 'electric',
        'Caterpie': 'grass',
        'Pidove': 'flying',
        'Slowpoke': 'water',
        'Horsea': 'water'
    }

    skills_of = {
        'water': [
            {'name': 'Tackle', 'damage': 3},
            {'name': 'Water Gun', 'damage': 5},
            {'name': 'Aqua Jet', 'damage': 7}
        ],
        'fire': [
            {'name': 'Tackle', 'damage': 3},
            {'name': 'Flamethrower', 'damage': 5},
            {'name': 'Fire Punch', 'damage': 7}
        ],
        'grass': [
            {'name': 'Tackle', 'damage': 3},
            {'name': 'Seed Bomb', 'damage': 5},
            {'name': 'Solar Beam', 'damage': 7}
        ],
        'electric': [
            {'name': 'Tackle', 'damage': 3},
            {'name': 'Thunderbolt', 'damage': 5},
            {'name': 'Electro Ball', 'damage': 7}
        ],
        'flying': [
            {'name': 'Pluck', 'damage': 3},
            {'name': 'Gust', 'damage': 5},
            {'name': 'Aerial Ace', 'damage': 7}
        ]
    }
    # TODO: decompose, function name: choose_pokemon_to_challenge()
    selected_pokemon = input(f"Choose a pokemon to challenge between {list(character['Balls'].keys())}: ").capitalize()

    if selected_pokemon not in pokemon_types:
        print("Invalid pokemon selection.")
        return False

    print(f"You have chosen {selected_pokemon}")

    gym_leader_pokemon_name = random.choice(list(gym_leader_pokemons.keys()))
    gym_leader_pokemon = gym_leader_pokemons[gym_leader_pokemon_name]
    print(f"The Gym Leader has chosen {gym_leader_pokemon_name}!")

    pokemon_type = pokemon_types[selected_pokemon]
    skills_of_selected_pokemon = skills_of[pokemon_type]
    skill_names = [skill['name'] for skill in skills_of_selected_pokemon]

    # TODO: decompose, function name: choose_skill_to_challenge()
    while character['Balls'][selected_pokemon]['Current HP'] > 0 and gym_leader_pokemon['Current HP'] > 0:
        user_input = input(f"Choose a skill between {skill_names}: ")

        selected_skill = next((skill for skill in skills_of_selected_pokemon if skill['name'] == user_input), None)

        if selected_skill:
            damage_to_gym_leader = selected_skill['damage']
            gym_leader_pokemon['Current HP'] -= damage_to_gym_leader
            print(f"You used {user_input}! It dealt {damage_to_gym_leader} damage.")
            print(f"Gym Leader's {gym_leader_pokemon_name} HP: {max(gym_leader_pokemon['Current HP'], 0)}")
        else:
            print("Invalid skill selection. Try again.")
            continue

        if gym_leader_pokemon['Current HP'] > 0:
            damage_from_gym_leader = random.choice([3, 5, 7])
            character['Balls'][selected_pokemon]['Current HP'] -= damage_from_gym_leader
            print(f"Gym Leader's {gym_leader_pokemon_name} attacked! You took {damage_from_gym_leader} damage.")
            print(f"Your {selected_pokemon}'s HP: {max(character['Balls'][selected_pokemon]['Current HP'], 0)}")

    # TODO: decompose, function name: result_of_battle()
    if character['Balls'][selected_pokemon]['Current HP'] <= 0:
        print(f"Your {selected_pokemon} fainted! You couldn't won the gym badge.")
    elif gym_leader_pokemon['Current HP'] <= 0:
        gym_badges[character['Current Level']] = True
        is_gym_badge_earned = True
        character['Current Level'] += 1
        print(f"Gym leader's {gym_leader_pokemon_name} fainted. You won the gym badge!")
    return is_gym_badge_earned


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
