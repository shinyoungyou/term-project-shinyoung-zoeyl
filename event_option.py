import copy

from common import check_input_is_digit
import random

from data import get_skill_of, event_pokemon


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

    >>> level_maximum_hp(3)
    100
    >>> level_maximum_hp(1)
    40
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

    >>> make_stronger(3)
    1.8
    >>> make_stronger(2)
    1.3
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
