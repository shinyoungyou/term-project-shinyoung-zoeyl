import random


def make_character():
    user_status = {'money': 30, 'user level': 1, 'potion': 0, 'X-coordinate': 0, 'Y-coordinate': 0}
    starting_pokemon = {'Squirtle': {'type': 'water', 'currentHP': 20},
                        'Charmander': {'type': 'fire', 'currentHP': 20},
                        'Bulbasaur': {'type': 'grass', 'currentHP': 20}}
    print("which poketmon would you like to go together?")
    print("Squirtle(Water) | Charmander(Fire) | Bulbasaur(Grass)")
    user_choice = input("Please type pokemon name: ").capitalize()
    while user_choice not in starting_pokemon:
        print("{} is not included in starting pokemon".format(user_choice))
        user_choice = input("what pokemon would you like? ")
    user_status['poke ball'] = {user_choice: starting_pokemon[user_choice]}
    return user_status