import random


def make_character():
    user_status = {'money': 30, 'user level': 1, 'potion': 0, 'X-coordinate': 0, 'Y-coordinate': 0}
    starting_pokemon = {'Squirtle': {'type': 'water', 'currentHP': 20},
                        'Charmander': {'type': 'fire', 'currentHP': 20},
                        'Bulbasaur': {'type': 'grass', 'currentHP': 20}}
    print("which pokemon would you like to go together?\n")
    print("Squirtle(Water) | Charmander(Fire) | Bulbasaur(Grass)")
    user_choice = input("Please type pokemon name: ").capitalize()
    while user_choice not in starting_pokemon:
        print("\n{} is not included in starting pokemon".format(user_choice))
        user_choice = input("what pokemon would you like? ").capitalize()
    user_status['poke ball'] = {user_choice: starting_pokemon[user_choice]}
    return user_status


def fight(user_status, skills_of, player_pokemon, event_pokemon_info, event_pokemon):
    possible_cases = ('hit', 'missed')
    skill_result = random.choice(possible_cases)
    pokemon_type = user_status['poke ball'][player_pokemon]['type']
    skills_of_selected_pokemon = skills_of[pokemon_type]
    number = 1
    print("")
    for skill in skills_of_selected_pokemon:
        print("{}. {}(damage range: {} ~ {})".format(number, skill['name'], skill['damage'][0], skill['damage'][1]))
        number += 1
    user_choice = int(input("Which skill would you like to use (Entering number)? "))
    while user_choice not in range(1, 4):
        print("{} is not a valid skill choice".format(user_choice))
        user_choice = int(input("Please choose a valid skill (Entering number): "))
    if skill_result == 'hit':
        print("\n{} hit!".format(skills_of_selected_pokemon[user_choice - 1]['name']))
        damage = random.randrange(skills_of_selected_pokemon[user_choice - 1]['damage'][0], skills_of_selected_pokemon[user_choice - 1]['damage'][1] + 1)
        event_pokemon_info['currentHP'] -= damage
    else:
        print("\n{} missed!".format(skills_of_selected_pokemon[user_choice - 1]['name']))

    if event_pokemon_info['currentHP'] <= 0:
        event_pokemon_info['currentHP'] = 20
        print("You defeated the %s" % event_pokemon)
        return False
    else:
        print("{}(HP: {})\n".format(event_pokemon, event_pokemon_info['currentHP']))
        return True


def change_pokemon():
    pass


def use_potion():
    pass


def throw_poke_ball():
    pass


def event_happened(user_status):
    event_collection = ("wildPokemon", "Team Rocket", "Strange trainer", False)
    event_type = random.choice(event_collection)
    event_pokemon_collection = {'Pichu': {'type': 'electric', 'currentHP': 20},
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

    event_pokemon = random.choice(list(event_pokemon_collection.keys()))
    event_pokemon_info = event_pokemon_collection[event_pokemon]
    if event_type:
        if event_type == "wildPokemon":
            print("\nA wild {} appeared!(HP: {})\n".format(event_pokemon, event_pokemon_info['currentHP']))
        else:
            print("\nYou encountered a %s!" % event_type)
            print("{} sent out {}!(HP: {})\n".format(event_type, event_pokemon, event_pokemon_info['currentHP']))

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
        player_pokemon = random.choice(list(user_status['poke ball'].keys()))
        while user_status['poke ball'][player_pokemon]['currentHP'] == 0:
            player_pokemon = random.choice(list(user_status['poke ball'].keys()))
        print("Go, %s!" % player_pokemon)
        print("{}(HP: {})\n".format(player_pokemon, user_status['poke ball'][player_pokemon]['currentHP']))

        process_result = True
        while process_result:
            user_option = [fight, change_pokemon, use_potion]
            if event_type == "wildPokemon":
                user_option.append(throw_poke_ball)
                user_option.append("Run")

            for print_option in range(len(user_option)):
                if print_option == 4:
                    print("{}. {}".format(print_option + 1, user_option[print_option]))
                else:
                    print("{}. {}".format(print_option + 1, user_option[print_option].__name__.replace("_", " ").title()))

            user_choice = int(input("What do you want to do (Entering number)? "))
            while user_choice == 0 or user_choice > len(user_option):
                print("\nThat is not option you can choose!")
                user_choice = input("Please choose valid option(Entering number): ")

            if user_choice == 1:
                process_result = user_option[user_choice - 1](user_status, skills_of, player_pokemon, event_pokemon_info, event_pokemon)

            if process_result:
                event_pokemon_skill = random.choice(skills_of[event_pokemon_info['type']])
                possible_cases = ('hit', 'missed')
                skill_result = random.choice(possible_cases)
                damage = 1
                if event_type == "Team Rocket":
                    damage = 1.5
                elif event_type == "Strange trainer":
                    damage = 1.3
                player_damage = (random.choice(
                    range(event_pokemon_skill['damage'][0], event_pokemon_skill['damage'][1] + 1)) * damage)
                print("{} used {}!\n".format(event_pokemon, event_pokemon_skill['name']))
                if skill_result == 'hit':
                    print("{} hit!".format(event_pokemon_skill['name']))
                    user_status['poke ball'][player_pokemon]['currentHP'] -= player_damage
                    print("{} took {} damage!".format(player_pokemon, player_damage))
                else:
                    print("{} missed!".format(event_pokemon_skill['name']))

                if user_status['poke ball'][player_pokemon]['currentHP'] <= 0:
                    user_status['poke ball'][player_pokemon]['currentHP'] = 0
                    print("{} fainted!".format(player_pokemon))
                    process_result = False
                else:
                    print("{}(HP: {})\n".format(player_pokemon, user_status['poke ball'][player_pokemon]['currentHP']))


def game():
    user_status = make_character()
    event_happened(user_status)


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
    # game()
    character = {
        "Current Location": (5, 5),
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
    board = make_board(character["Current Level"])
    display_current_location(board, character)
    battle_with_gym_leader(character)


if __name__ == "__main__":
    main()
