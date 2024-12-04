from common import check_input_is_digit
from data import event_pokemon
import random
import copy
from event_option import fight, throw_poke_ball


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

    >>> customize_user_options("wildPokemon")
    ['Fight', 'Change Pokemon', 'Use Potion', 'Throw Poke Ball', 'Run Away']
    >>> customize_user_options("Gym Leader", 3)
    ['Fight', 'Change Pokemon', 'Run Away']
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


def set_event_type() -> str or bool:
    """
    Determine what kind of event has occurred.

    :postcondition: choose a random event type
    :return: a string representing the type of event if an event has occurred
    :return: a boolean value, false if no event has occurred
    """
    event_collection = ("wildPokemon", "Team Rocket", "Strange trainer", False)
    return random.choices(event_collection, weights=[18, 5, 7, 3], k=1)[0]


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

    >>> d_user_choice = "Run Away"
    >>> d_character_pokemon = ("Squirtle", {'type': 'water', 'currentHP': 40})
    >>> d_character = {'Character Name': "zoey", 'Poke Ball': {'Squirtle': {'type': 'water', 'currentHP': 40}}}
    >>> d_event_pokemon_info = ("Pichu", {'type': 'electric', 'currentHP': 30})
    >>> d_event_type = "wildPokemon"
    >>> proceed_event_option(d_user_choice, d_character_pokemon, d_character, d_event_pokemon_info, d_event_type)
    <BLANKLINE>
    You escaped from Pichu!
    <BLANKLINE>
    False
    """
    if user_choice == "Fight":
        process_result = fight(character_pokemon, event_pokemon_info, character, event_type)
    elif user_choice == "Throw Poke Ball":
        process_result = throw_poke_ball(event_pokemon_info, character)
    else:
        print(f"\nYou escaped from {event_pokemon_info[0]}!\n")
        process_result = False
    return process_result


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
        print(f"\nA wild {event_pokemon_info[0]} appeared!")
    else:
        print(f"\nYou encountered a {event_type}!\n{event_type} sent out {event_pokemon_info[0]}!\n")
    print(f"Event pokemon status: {event_pokemon_info[0]}(HP: {event_pokemon_info[1]['currentHP']})\n")
    return event_pokemon_info