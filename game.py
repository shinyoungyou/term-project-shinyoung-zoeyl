import random


def make_character():
    user_status = {'money': 30, 'user level': 1, 'potion': 0, 'X-coordinate': 0, 'Y-coordinate': 0}
    starting_pokemon = {'Squirtle': {'type': 'water', 'currentHP': 20},
                        'Charmander': {'type': 'fire', 'currentHP': 20},
                        'Bulbasaur': {'type': 'grass', 'currentHP': 20}}
    print("which pokemon would you like to go together?")
    print("Squirtle(Water) | Charmander(Fire) | Bulbasaur(Grass)")
    user_choice = input("Please type pokemon name: ").capitalize()
    while user_choice not in starting_pokemon:
        print("{} is not included in starting pokemon".format(user_choice))
        user_choice = input("what pokemon would you like? ").capitalize()
    user_status['poke ball'] = {user_choice: starting_pokemon[user_choice]}
    return user_status


def fight(user_status, skills_of, player_pokemon, event_pokemon_info, event_pokemon):
    possible_cases = ('hit', 'missed')
    skill_result = random.choice(possible_cases)
    pokemon_type = user_status['poke ball'][player_pokemon]['type']
    skills_of_selected_pokemon = skills_of[pokemon_type]
    number = 1
    for skill in skills_of_selected_pokemon:
        print("{}. {}(damage range: {} ~ {})".format(number, skill['name'], skill['damage'][0], skill['damage'][1]))
        number += 1
    user_choice = int(input("Which skill would you like to use (Entering number)? "))
    while user_choice not in range(1, 4):
        print("{} is not a valid skill choice".format(user_choice))
        user_choice = int(input("Please choose a valid skill (Entering number): "))
    if skill_result == 'hit':
        print("{} hit!".format(skills_of_selected_pokemon[user_choice - 1]['name']))
        damage = random.randrange(skills_of_selected_pokemon[user_choice - 1]['damage'][0], skills_of_selected_pokemon[user_choice - 1]['damage'][1] + 1)
        event_pokemon_info['currentHP'] -= damage
    else:
        print("{} missed!".format(skills_of_selected_pokemon[user_choice - 1]['name']))
        return True

    if event_pokemon_info['currentHP'] <= 0:
        event_pokemon_info['currentHP'] = 20
        print("You defeated the %s" % event_pokemon)
        return False
    else:
        print("{}(HP: {})".format(event_pokemon, event_pokemon_info['currentHP']))
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
            print("A wild {} appeared!(HP: {})".format(event_pokemon, event_pokemon_info['currentHP']))
        else:
            print("You encountered a %s!" % event_type)
            print("{} sent out {}!(HP: {})".format(event_type, event_pokemon, event_pokemon_info['currentHP']))

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
        print("{}(HP: {})".format(player_pokemon, user_status['poke ball'][player_pokemon]['currentHP']))

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
                print("That is not option you can choose!")
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
                print("{} used {}!".format(event_pokemon, event_pokemon_skill['name']))
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
                    print("{}(HP: {})".format(player_pokemon, user_status['poke ball'][player_pokemon]['currentHP']))


def game():
    user_status = make_character()
    event_happened(user_status)


def main():
    game()


if __name__ == "__main__":
    main()