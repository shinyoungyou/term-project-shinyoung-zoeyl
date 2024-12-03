from unittest import TestCase
from unittest.mock import patch


from gym import evolve_pokemon


class TestEvolvePokemon(TestCase):

    @patch('gym.starting_pokemon_collection', return_value={'Wartortle': {'type': 'water', 'currentHP': 65}})
    def test_evolve_pokemon_squirtle_has_evolved_into_wartortle_in_level_2(self, _):
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 2, 'Potion': 0,
                     'Current Location': (5, 5),
                     'Starting Pokemon': 'Squirtle',
                     'Poke Ball': {
                         'Squirtle': {'type': 'water', 'currentHP': 40},
                         'Pichu': {'type': 'electric', 'currentHP': 30},
                         'Shinx': {'type': 'electric', 'currentHP': 30},
                         'Mareep': {'type': 'electric', 'currentHP': 30},
                         'Caterpie': {'type': 'grass', 'currentHP': 30},
                         'Weedle': {'type': 'grass', 'currentHP': 30},
                     }}
        expected_evolved_pokemon_name = 'Wartortle'
        evolve_pokemon(character)
        actual_evolved_pokemon_name = character['Starting Pokemon']
        self.assertEqual(expected_evolved_pokemon_name, actual_evolved_pokemon_name)

    @patch('gym.starting_pokemon_collection', return_value={'Charmeleon': {'type': 'fire', 'currentHP': 65}})
    def test_evolve_pokemon_charmander_has_evolved_into_charmeleon_in_level_2(self, _):
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 2, 'Potion': 0,
                     'Current Location': (5, 5),
                     'Starting Pokemon': 'Charmander',
                     'Poke Ball': {
                         'Charmander': {'type': 'fire', 'currentHP': 40},
                         'Luxio': {'type': 'electric', 'currentHP': 50},
                         'Flaaffy': {'type': 'electric', 'currentHP': 50},
                         'Metapod': {'type': 'grass', 'currentHP': 50},
                         'Kakuna': {'type': 'grass', 'currentHP': 50},
                         'Grovyle': {'type': 'grass', 'currentHP': 50}
                     }}
        expected_evolved_pokemon_name = 'Charmeleon'
        evolve_pokemon(character)
        actual_evolved_pokemon_name = character['Starting Pokemon']
        self.assertEqual(expected_evolved_pokemon_name, actual_evolved_pokemon_name)

    @patch('gym.starting_pokemon_collection', return_value={'Ivysaur': {'type': 'grass', 'currentHP': 65}})
    def test_evolve_pokemon_bulbasaur_has_evolved_into_ivysaur_in_level_2(self, _):
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 2, 'Potion': 0,
                     'Current Location': (5, 5),
                     'Starting Pokemon': 'Bulbasaur',
                     'Poke Ball': {
                         'Bulbasaur': {'type': 'grass', 'currentHP': 40},
                         'Luxio': {'type': 'electric', 'currentHP': 50},
                         'Flaaffy': {'type': 'electric', 'currentHP': 50},
                         'Metapod': {'type': 'grass', 'currentHP': 50},
                         'Kakuna': {'type': 'grass', 'currentHP': 50},
                         'Grovyle': {'type': 'grass', 'currentHP': 50}
                     }}
        expected_evolved_pokemon_name = 'Ivysaur'
        evolve_pokemon(character)
        actual_evolved_pokemon_name = character['Starting Pokemon']
        self.assertEqual(expected_evolved_pokemon_name, actual_evolved_pokemon_name)

    @patch('gym.starting_pokemon_collection', return_value={'Blastoise': {'type': 'water', 'currentHP': 100}})
    def test_evolve_pokemon_wartortle_has_evolved_into_blastoise_in_level_3(self, _):
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 3, 'Potion': 0,
                     'Current Location': (7, 4),
                     'Starting Pokemon': 'Wartortle',
                     'Poke Ball': {
                         'Wartortle': {'type': 'water', 'currentHP': 65},
                         'Luxray': {'type': 'electric', 'currentHP': 80},
                         'Ampharos': {'type': 'electric', 'currentHP': 80},
                         'Butterfree': {'type': 'grass', 'currentHP': 80},
                         'Beedrill': {'type': 'grass', 'currentHP': 80},
                         'Sceptile': {'type': 'grass', 'currentHP': 80},
                     }}
        expected_evolved_pokemon_name = 'Blastoise'
        evolve_pokemon(character)
        actual_evolved_pokemon_name = character['Starting Pokemon']
        self.assertEqual(expected_evolved_pokemon_name, actual_evolved_pokemon_name)

    @patch('gym.starting_pokemon_collection', return_value={'Charizard': {'type': 'fire', 'currentHP': 100}})
    def test_evolve_pokemon_charmeleon_has_evolved_into_charizard_in_level_3(self, _):
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 3, 'Potion': 0,
                     'Current Location': (7, 4),
                     'Starting Pokemon': 'Charmeleon',
                     'Poke Ball': {
                         'Charmeleon': {'type': 'fire', 'currentHP': 65},
                         'Luxray': {'type': 'electric', 'currentHP': 80},
                         'Ampharos': {'type': 'electric', 'currentHP': 80},
                         'Butterfree': {'type': 'grass', 'currentHP': 80},
                         'Beedrill': {'type': 'grass', 'currentHP': 80},
                         'Sceptile': {'type': 'grass', 'currentHP': 80},
                     }}
        expected_evolved_pokemon_name = 'Charizard'
        evolve_pokemon(character)
        actual_evolved_pokemon_name = character['Starting Pokemon']
        self.assertEqual(expected_evolved_pokemon_name, actual_evolved_pokemon_name)

    @patch('gym.starting_pokemon_collection', return_value={'Venusaur': {'type': 'grass', 'currentHP': 100}})
    def test_evolve_pokemon_ivysaur_has_evolved_into_venusaur_in_level_3(self, _):
        character = {'Character Name': 'user1', 'Money': 30, 'Current Level': 3, 'Potion': 0,
                     'Current Location': (7, 4),
                     'Starting Pokemon': 'Ivysaur',
                     'Poke Ball': {
                         'Bulbasaur': {'type': 'grass', 'currentHP': 40},
                         'Luxray': {'type': 'electric', 'currentHP': 80},
                         'Ampharos': {'type': 'electric', 'currentHP': 80},
                         'Butterfree': {'type': 'grass', 'currentHP': 80},
                         'Beedrill': {'type': 'grass', 'currentHP': 80},
                         'Sceptile': {'type': 'grass', 'currentHP': 80},
                     }}
        expected_evolved_pokemon_name = 'Venusaur'
        evolve_pokemon(character)
        actual_evolved_pokemon_name = character['Starting Pokemon']
        self.assertEqual(expected_evolved_pokemon_name, actual_evolved_pokemon_name)
