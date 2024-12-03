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