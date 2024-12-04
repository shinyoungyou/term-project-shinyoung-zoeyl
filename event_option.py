from common import check_input_is_digit
import random
from data import get_skill_of


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
    print(f"You got ${int(earn_money)}!\n")


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
        print(f"You defeated the {event_pokemon_info[0]}\n")
        if event_type != "Gym Leader":
            get_money(character, event_type)
        return False
    else:
        print(f"Event Pokémon status: {event_pokemon_info[0]}(HP: {event_pokemon_info[1]['currentHP']})\n")
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
    print(f"\nEvent Pokémon status: {event_pokemon_info[0]}(HP: {event_pokemon_info[1]['currentHP']})\n")
    skill_collection = get_skill_of(character_pokemon[1]['type'])
    character_pokemon_skill = choose_skill_to_challenge(skill_collection, character['Current Level'])
    if get_probability():
        return get_attack_result(character_pokemon_skill, event_pokemon_info, character, event_type)
    else:
        print(f"\n{character_pokemon_skill['name']} missed!\n"
              f"Event Pokémon status: {event_pokemon_info[0]}(HP: {event_pokemon_info[1]['currentHP']})\n")
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
        print("\nYou has no Pokémon to switch to\n")
    else:
        print("\nYour Pokémons' status...")
        for pokemon in pokeball.keys():
            if pokemon != character_pokemon[0]:
                print(f"{pokemon}(HP: {pokeball[pokemon]['currentHP']})")

        user_choice = input("\nWhich Pokémon would you like to switch to (Entering Pokémon name)? ").capitalize()
        while (user_choice not in pokeball.keys() or pokeball[user_choice]['currentHP'] == 0
               or user_choice == character_pokemon[0]):
            print(f"\n{user_choice} is not included in your Poké Balls or has 0HP")
            user_choice = input("Which Pokémon would you like (Entering Pokémon name)? ").capitalize()

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
    print("You can't choose the Starting Pokémon!")

    user_choice_pokemon = input("what Pokémon would you release (Entering Pokémon name)? ").capitalize()
    while (user_choice_pokemon not in character['Poke Ball'].keys() or user_choice_pokemon
           == character['Starting Pokemon']):
        print(f"\n{user_choice_pokemon} can't be chosen!")
        user_choice_pokemon = input(
            "Please choose a Pokémon that is in your Poké Ball except your Starting Pokémon "
            + "(Entering Pokémon name): ").capitalize()

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
        print("\nShoot! It was so close!\n")
        process_result = get_probability()
    return process_result
