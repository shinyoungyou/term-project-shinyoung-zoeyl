from typing import Any

from common import is_alive
from data import starting_pokemon_collection
from event_option import select_event_option, take_out_pokemon, get_event_pokemon, fight, change_pokemon, get_attacked


def check_badge_eligibility(character: dict[str, Any], current_win_count: int, gym_badge_earned: bool) -> bool:
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

    >>> test_character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 1, 'Potion': 0,
    ...             'Current Location': (5, 5),
    ...             'Starting Pokemon': 'Squirtle',
    ...             'Poke Ball': {
    ...                 'Squirtle': {'type': 'water', 'currentHP': 40},
    ...                 'Pichu': {'type': 'electric', 'currentHP': 30},
    ...                 'Shinx': {'type': 'electric', 'currentHP': 30},
    ...                 'Mareep': {'type': 'electric', 'currentHP': 30},
    ...                 'Caterpie': {'type': 'grass', 'currentHP': 30},
    ...                 'Weedle': {'type': 'grass', 'currentHP': 30},
    ...             }}
    >>> check_badge_eligibility(test_character, 1, False)
    <BLANKLINE>
    You need to win 1 more time(s) to earn the badge.
    <BLANKLINE>
    False
    >>> check_badge_eligibility(test_character, 2, False)
    True
    """
    current_level = character["Current Level"]

    win_count = {1: 2, 2: 3, 3: 4}.get(current_level)
    if win_count is None:
        print("Invalid level")
        return gym_badge_earned

    count_left_for_badge = win_count - current_win_count

    if count_left_for_badge > 0:
        print(f"\nYou need to win {count_left_for_badge} more time(s) to earn the badge.\n")
        return gym_badge_earned
    else:
        gym_badge_earned = True

    return gym_badge_earned


def has_six_pokemons(character: dict[str, Any]) -> bool:
    """
    Check if the character has six Pokèmons.

    :param character: a dictionary representing character's info, including their Pokèmons' info
    :precondition: character is a dictionary which has Pokèmons' info that the character has
    :postcondition: counts the number of Pokèmons needed to enter the gym
    :return: True if the character has six Pokèmons, otherwise False

    >>> test_character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 1, 'Potion': 0,
    ...             'Current Location': (5, 5),
    ...             'Starting Pokemon': 'Squirtle',
    ...             'Poke Ball': {
    ...                 'Squirtle': {'type': 'water', 'currentHP': 40},
    ...                 'Pichu': {'type': 'electric', 'currentHP': 30},
    ...                 'Shinx': {'type': 'electric', 'currentHP': 30},
    ...                 'Mareep': {'type': 'electric', 'currentHP': 30},
    ...                 'Caterpie': {'type': 'grass', 'currentHP': 30},
    ...                 'Weedle': {'type': 'grass', 'currentHP': 30},
    ...             }}
    >>> has_six_pokemons(test_character)
    True
    >>> test_character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 1, 'Potion': 0,
    ...             'Current Location': (5, 5),
    ...             'Starting Pokemon': 'Squirtle',
    ...             'Poke Ball': {
    ...                 'Squirtle': {'type': 'water', 'currentHP': 40},
    ...             }}
    >>> has_six_pokemons(test_character)
    You need to earn 5 more pokemon(s) to enter the gym.
    False
    """
    more = 6 - len(character['Poke Ball'])
    if more > 0:
        print(f"You need to earn {more} more pokemon(s) to enter the gym.")

    return not more


def encounter_gym(character: dict[str, Any]) -> bool:
    """
    Ask user to choose whether to challenge or quit.

    :param character: a dictionary representing character's info
    :precondition: character is a dictionary containing the character's details
    :postcondition: proceeds the gym battle if user chose to challenge
    :return: True if the user earned a gym badge as a result of the battle, otherwise False
    """
    gym_badge_earned = False

    while True:
        user_input = input("\nEncountered a gym! Enter y to challenge, n to quit: ")
        if user_input == 'y' or user_input == 'n':
            break
        print("Please Enter y or n.")

    if user_input == 'n':
        return gym_badge_earned

    print("\nGym Leader: Welcome to the gym! "
          "Here is one rule: you can't use potions to accurately assess your skills.\n")

    gym_badge_earned = battle_with_gym_leader(character, gym_badge_earned)
    return gym_badge_earned


def battle_with_gym_leader(character: dict[str, Any], gym_badge_earned: bool) -> bool:
    """
    Handle the gym battle between the user and the gym leader.

    :param character: a dictionary representing character's info
    :param gym_badge_earned: a boolean representing if the user earned a gym badge
    :precondition: character is a dictionary containing the character's details
    :precondition: gym_badge_earned is True if the user earned a gym badge, otherwise False
    :postcondition: checks if the user earned a gym badge as a result of the battle
    :return: True if the user earned a gym badge, otherwise False
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


def initialize_battle(character: dict) -> tuple:
    """
    Initiate the gym battle.

    :param character: a dictionary including character's details such as their pokèmons
    :precondition: character is a dictionary which has 'Poke Ball' key, and other character's details
    :postcondition: sets up the initial state for a gym battle
    :return: a tuple representing the initial state for a gym battle
    """
    current_win_count = 0
    prev_round = 0
    gym_round = 1
    selected_pokemon = take_out_pokemon(character['Poke Ball'])
    gym_leader_pokemon = get_event_pokemon(character)
    return current_win_count, prev_round, gym_round, selected_pokemon, gym_leader_pokemon


def display_round_intro(gym_round: int, gym_leader_pokemon: (str, dict[str, Any]),
                        selected_pokemon: (str, dict[str, Any]), character: dict[str, Any]):
    """
    Display the status of gym leader pokèmon and selected pokèmon.

    :param gym_round: a positive integer representing the current gym round
    :param gym_leader_pokemon: a tuple including gym leader pokèmon's name, and their details
    :param selected_pokemon: a tuple including the name of randomly selected pokèmon for character, and their details
    :param character: a dictionary representing character's details such as their name and their poke ball
    :precondition: gym_round is an integer greater than 0
    :precondition: gym_leader_pokemon is a tuple including a string and a dictionary
    :precondition: selected_pokemon is a tuple including a string and a dictionary
    :precondition: character is a dictionary which has 'Character Name', 'Poke Ball' keys and other character's details
    :postcondition: prints the gym round and the status of gym leader pokèmon and selected pokèmon
    """
    print(f"\n❗️Round {gym_round} ❗\n")
    print(f"Event pokemon status: {gym_leader_pokemon[0]}(HP: {gym_leader_pokemon[1]['currentHP']})\n")
    print(f"{character['Character Name']}'s pokemon status: {selected_pokemon[0]}"
          f"(HP: {character['Poke Ball'][selected_pokemon[0]]['currentHP']})\n")


def handle_user_choice(user_choice: str, process_result: bool, selected_pokemon: (str, dict[str, Any]),
                       gym_leader_pokemon: (str, dict[str, Any]), character: dict[str, Any])\
                    -> tuple:
    """
    Ask user to fight, change their pokèmon, or run away.

    :param user_choice: a string representing the user choice
    :param process_result: a boolean indicating whether the target won or lost the round
    :param selected_pokemon: a tuple including the name of randomly selected pokèmon for character, and their details
    :param gym_leader_pokemon: a tuple including gym leader pokèmon's name, and their details
    :param character: a dictionary representing character's details such as their name and their poke ball
    :precondition: user_choice is a function or a string
    :precondition: process_result is True if the target won, or False if they lost the round
    :precondition: selected_pokemon is a tuple including a string and a dictionary
    :precondition: gym_leader_pokemon is a tuple including a string and a dictionary
    :precondition: character is a dictionary which has 'Poke Ball' key and other character's details
    :postcondition: updates gym battle state according to the user choice
    :return: a tuple representing updated gym battle state according to the user choice

    >>> test_user_choice = "Run Away"
    >>> test_process_result = False
    >>> test_selected_pokemon = ('Squirtle', {'type': 'water', 'currentHP': 40})
    >>> test_gym_leader_pokemon = ('Weedle', {'type': 'grass', 'currentHP': 30})
    >>> test_character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 1, 'Potion': 0,
    ...             'Current Location': (5, 5),
    ...             'Starting Pokemon': 'Squirtle',
    ...             'Poke Ball': {
    ...                 'Squirtle': {'type': 'water', 'currentHP': 40},
    ...                 'Pichu': {'type': 'electric', 'currentHP': 30},
    ...                 'Shinx': {'type': 'electric', 'currentHP': 30},
    ...                 'Mareep': {'type': 'electric', 'currentHP': 30},
    ...                 'Caterpie': {'type': 'grass', 'currentHP': 30},
    ...                 'Weedle': {'type': 'grass', 'currentHP': 30},
    ...             }}
    >>> updated_state = handle_user_choice(test_user_choice, test_process_result, test_selected_pokemon,
    ... test_gym_leader_pokemon, test_character)
    <BLANKLINE>
    Gym Leader: Running away, huh? I guess today's not your day. Come back when you're ready to battle!
    >>> stop_process = updated_state[2]
    >>> stop_process
    True
    """
    stop_process = False
    if user_choice == "Fight":
        process_result = fight(selected_pokemon, gym_leader_pokemon, character, "Gym Leader")
    elif user_choice == "Change Pokemon":
        selected_pokemon = change_pokemon(character['Poke Ball'], selected_pokemon)
    elif user_choice == "Run Away":
        print("\nGym Leader: Running away, huh? I guess today's not your day. "
              "Come back when you're ready to battle!")
        stop_process = True
    return process_result, selected_pokemon, stop_process


def check_if_alive_when_lost_the_round(gym_leader_pokemon: (str, dict[str, Any]), character: dict[str, Any],
                                       selected_pokemon: (str, dict[str, Any]), gym_round: int)\
                                    -> tuple:
    """
    Check if character is still alive when they lost the round.

    :param gym_leader_pokemon: a tuple including gym leader pokèmon's name, and their details
    :param character: a dictionary representing character's details such as their name and their poke ball
    :param selected_pokemon: a tuple including the name of randomly selected pokèmon for character, and their details
    :param gym_round: a positive integer representing the current gym round
    :precondition: gym_leader_pokemon is a tuple including a string and a dictionary
    :precondition: character is a dictionary which has 'Poke Ball' key and other character's details
    :precondition: selected_pokemon is a tuple including a string and a dictionary
    :precondition: gym_round is an integer greater than 0
    :postcondition: updates the gym battle state reflecting whether the user lost the round
             and whether their pokèmon is still alive
    :return: a tuple representing updated the gym battle state
    """
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


def win_the_round(current_win_count: int, character: dict[str, Any], gym_badge_earned: bool, gym_round: int)\
              -> tuple:
    """
    Make changes to the gym battle state as the outcome when the user wins.

    :param current_win_count: a positive integer representing the current winning count
    :param character: a dictionary including character's details
    :param gym_badge_earned: a boolean representing if the gym badge earned
    :param gym_round: a positive integer representing the current gym round
    :postcondition: updates the gym battle state as the outcome when the user wins
    :return: a tuple representing updated the gym battle state
    """
    current_win_count += 1
    gym_badge_earned = check_badge_eligibility(character, current_win_count, gym_badge_earned)
    gym_round += 1
    gym_leader_pokemon = get_event_pokemon(character)
    return current_win_count, gym_badge_earned, gym_round, gym_leader_pokemon


def evolve_pokemon(character: dict[str, Any]):
    """
    Evolve character's starting pokèmon based on the character's level.

    :param character: a dictionary including character's info such as their poke ball and starting pokèmon
    :precondition: character is a dictionary including 'Poke Ball', 'Starting Pokemon' keys, and other details for them
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


def level_up(character: dict[str, Any]):
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
