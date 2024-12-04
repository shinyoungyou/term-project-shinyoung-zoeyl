import random
from data import get_skill_of
from event_option import get_probability


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
                 random.randrange(event_pokemon_skill['damage'][0], event_pokemon_skill['damage'][1] + 1))

    print(f"{event_pokemon_info[0]} used {event_pokemon_skill['name']}!\n")

    if get_probability():
        print(f"{event_pokemon_skill['name']} hit!")
        character_pokemon[1]['currentHP'] -= damage
        print(f"{character_pokemon[0]} took {damage} damage!")
    else:
        print(f"{event_pokemon_skill['name']} missed!")

    return check_status(character_pokemon)


def check_status(character_pokemon: tuple) -> bool:
    """
    Check if the user's Pokémon has fainted.

    :param character_pokemon: a tuple containing the user Pokémon's name and a dictionary with its type and current HP
    :precondition: character_pokemon represents the status of one of the user's Pokémon in battle
    :postcondition: check the status of user's Pokémon
    :return: a boolean value, false if the user's Pokémon has fainted, true otherwise

    >>> check_status(('Marshtomp', {'type': 'water', 'currentHP': 50}))
    True
    >>> check_status(('Totodile', {'type': 'water', 'currentHP': 0}))
    Totodile fainted!
    False
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

    >>> get_stronger_collection(1)
    (1, 1.3, 1.4, 1.5)
    >>> get_stronger_collection(3)
    (1.5, 1.7, 2, 2.5)
    """
    if character_level == 1:
        stronger_collection = (1, 1.3, 1.4, 1.5)
    elif character_level == 2:
        stronger_collection = (1.3, 1.5, 1.7, 2)
    else:
        stronger_collection = (1.5, 1.7, 2, 2.5)

    return stronger_collection