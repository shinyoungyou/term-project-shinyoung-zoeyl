from typing import Any


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


def is_alive(character: dict[str, Any]) -> bool:
    """
    Check if the character is alive

    :param character: a dictionary representing character, including their Pokémon
    :precondition: character is a dictionary with a key "Balls" including Pokémon's HP
    :postcondition: returns True if at least one Pokémon has HP greater than 0, else False
    :return: True if the character is alive, else False

    >>> test_character = {"Poke Ball": {"Pikachu": {"currentHP": 10}, "Bulbasaur": {"currentHP": 10}}}
    >>> is_alive(test_character)
    True
    >>> test_character = {"Poke Ball": {"Pikachu": {"currentHP": 10}, "Bulbasaur": {"currentHP": 0}}}
    >>> is_alive(test_character)
    True
    >>> test_character = {"Poke Ball": {"Pikachu": {"currentHP": 0}, "Bulbasaur": {"currentHP": 0}}}
    >>> is_alive(test_character)
    False
    """
    alive = True

    if not any(pokemon['currentHP'] > 0 for pokemon in character["Poke Ball"].values()):
        alive = False

    return alive
