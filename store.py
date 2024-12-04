from common import check_input_is_digit
from constants import POTION_PRICE
from event_option import level_maximum_hp


def encounter_store(character: dict) -> None:
    """
    Give user with options between buy or use potion, or quit the store.

    :param character: a dictionary representing the character
    :precondition: character is a dictionary containing the character's details, including 'Money', 'Poke Ball'
    :postcondition: executes selected option between buy potion, use potion, or quit
    """
    actions = {
        'buy': lambda: buy_potion(character),
        'use': lambda: use_potion(character, select_pokemon(character['Poke Ball'])),
    }

    while True:
        user_input = input("\nEnter 'buy' to buy a potion, 'use' to use a potion, or 'q' to quit: ").lower()
        if user_input in actions:
            actions[user_input]()
        elif user_input == 'q':
            break
        else:
            print("Invalid option. Please try again.")


def buy_potion(character: dict) -> None:
    """
    Calculate the change after a purchase.

    :param character: a dictionary representing character, including their money
    :precondition: character is a dictionary with a key "Money" representing the character's current budget
    :postcondition: updates the character's money if any potion is purchased
    """
    print(f"\nYour budget is ${character['Money']}, and each potion price is ${POTION_PRICE}.")
    while True:
        number_of_potions = check_input_is_digit("Enter the number of potions to purchase: ")
        if number_of_potions > 0:
            break
        print("You need to buy at least one potion.")

    total_price = POTION_PRICE * number_of_potions
    print(f"\nTotal price will be: ${total_price}")
    budget = character["Money"]
    change = budget - total_price

    if change >= 0:
        character["Potion"] += 1 * number_of_potions
        print(f"Purchase successful! Your remaining budget is ${change}")
        character["Money"] = change
    else:
        print("You can't buy with your current budget.")


def use_potion(character: dict, character_pokemon: tuple) -> None:
    """
    Restore the user's Pokémon's HP.

    :param character: a dictionary containing information about the character's status
    :param character_pokemon: a tuple containing the user Pokémon's name and a dictionary with its type and current HP
    :precondition: the user Pokémon must have an HP greater than 0 in the character_pokemon
    :precondition: character has a value about 'Current Level' key and 'Potion' key
    :precondition: check_potion returns a boolean value, true
    :postcondition: check whether the user wants to use a potion on the Pokémon
    :postcondition: add a certain amount to the Pokémon's HP
    """
    if check_potion(character['Potion'], character['Current Level'], character_pokemon):
        print(f"\nYou have {character['Potion']} potion(s)!\n{character_pokemon[0]} has "
              f"{character_pokemon[1]["currentHP"]} HP.")

        user_answer = input("\nWould you like to use a potion (y/n)? ").lower()
        while user_answer not in ('y', 'n'):
            print(f"\n{user_answer} is not a valid option")
            user_answer = input("Please choose a valid "
                                "option (y/n): ").lower()

        if user_answer == 'y':
            pokemon_maximum_hp = level_maximum_hp(character['Current Level'])
            if character_pokemon[1]["currentHP"] > pokemon_maximum_hp - 15:
                character_pokemon[1]["currentHP"] = pokemon_maximum_hp
            else:
                character_pokemon[1]["currentHP"] += 15
            character['Potion'] -= 1
            print(f"\n{character_pokemon[0]} restored HP!\n{character_pokemon[0]}"
                  f"(HP: {character_pokemon[1]["currentHP"]})\n{character['Potion']} potion(s) left!")


def check_potion(number_of_potion: int, character_level: int, character_pokemon: tuple) -> bool:
    """
    Check whether the user can use a potion.

    :param number_of_potion: an integer representing the number of potions the user has
    :param character_level: an integer that represents user's current level
    :param character_pokemon: a tuple containing the user Pokémon's name and a dictionary with its type and current HP
    :precondition: the user Pokémon must have an HP greater than 0 in the character_pokemon
    :precondition: character_level must be a number between 1 and 3
    :precondition: number_of_potion must be 0 or greater
    :postcondition: check if the user has no potion or the user's Pokémon has full HP
    :return: a boolean value, true if the user can use a potion on the Pokémon, false otherwise

    >>> test_character_pokemon = ('Squirtle', {'type': 'water', 'currentHP': 20})
    >>> test_validation = check_potion(0, 1, test_character_pokemon)
    <BLANKLINE>
    You don't have any potion!
    <BLANKLINE>
    >>> test_validation
    False
    >>> test_character_pokemon = ('Squirtle', {'type': 'water', 'currentHP': 30})
    >>> test_validation = check_potion(1, 1, test_character_pokemon)
    >>> test_validation
    True
    """
    validation = False
    if number_of_potion == 0:
        print("\nYou don't have any potion!\n")
    elif character_pokemon[1]["currentHP"] == level_maximum_hp(character_level):
        print(f"\n{character_pokemon[0]} has full HP!\n")
    else:
        validation = True
    return validation


def select_pokemon(pokeball: dict) -> (str, dict):
    """
    Ask user to select a Pokémon.

    :param pokeball: a dictionary representing collection of Pokémon(s)
    :precondition: pokeball is a dictionary representing collection of Pokémon(s)
    :postcondition: provides selected Pokémon name and the Pokémon's info
    :return: a tuple of a string representing selected Pokémon name,
             and a dictionary of the Pokémon's info
    """
    print("\nYour pokemons' status...")
    for pokemon in pokeball.keys():
        print(f"{pokemon}(HP: {pokeball[pokemon]['currentHP']})")

    while True:
        user_choice = input("\nSelect pokemon to proceed by entering the pokemon name: ").capitalize()
        if user_choice in pokeball.keys():
            break
        print("Invalid pokemon!\n")

    return user_choice, pokeball[user_choice]
