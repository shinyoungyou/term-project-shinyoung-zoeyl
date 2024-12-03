from unittest import TestCase


from game import is_alive


class TestIsAlive(TestCase):

    def test_is_alive_all_pokemon_hps_are_zero(self):
        expected = False
        character = {"Poke Ball": {
                     'Squirtle': {'type': 'water', 'currentHP': 0},
                     'Pichu': {'type': 'electric', 'currentHP': 0},
                     'Shinx': {'type': 'electric', 'currentHP': 0},
                     'Mareep': {'type': 'electric', 'currentHP': 0},
                     'Caterpie': {'type': 'grass', 'currentHP': 0},
                     'Weedle': {'type': 'grass', 'currentHP': 0}}}
        actual = is_alive(character)
        self.assertEqual(expected, actual)

    def test_is_alive_five_pokemon_hps_are_zero(self):
        expected = True
        character = {"Poke Ball": {
                     'Squirtle': {'type': 'water', 'currentHP': 10},
                     'Pichu': {'type': 'electric', 'currentHP': 0},
                     'Shinx': {'type': 'electric', 'currentHP': 0},
                     'Mareep': {'type': 'electric', 'currentHP': 0},
                     'Caterpie': {'type': 'grass', 'currentHP': 0},
                     'Weedle': {'type': 'grass', 'currentHP': 0}}}
        actual = is_alive(character)
        self.assertEqual(expected, actual)

    def test_is_alive_three_pokemon_hps_are_zero(self):
        expected = True
        character = {"Poke Ball": {
                     'Squirtle': {'type': 'water', 'currentHP': 10},
                     'Pichu': {'type': 'electric', 'currentHP': 10},
                     'Shinx': {'type': 'electric', 'currentHP': 10},
                     'Mareep': {'type': 'electric', 'currentHP': 0},
                     'Caterpie': {'type': 'grass', 'currentHP': 0},
                     'Weedle': {'type': 'grass', 'currentHP': 0}}}
        actual = is_alive(character)
        self.assertEqual(expected, actual)

    def test_is_alive_one_pokemon_hp_is_zero(self):
        expected = True
        character = {"Poke Ball": {
                     'Squirtle': {'type': 'water', 'currentHP': 10},
                     'Pichu': {'type': 'electric', 'currentHP': 10},
                     'Shinx': {'type': 'electric', 'currentHP': 10},
                     'Mareep': {'type': 'electric', 'currentHP': 10},
                     'Caterpie': {'type': 'grass', 'currentHP': 10},
                     'Weedle': {'type': 'grass', 'currentHP': 0}}}
        actual = is_alive(character)
        self.assertEqual(expected, actual)

    def test_is_alive_all_pokemon_hps_are_greater_than_zero(self):
        expected = True
        character = {"Poke Ball": {
                     'Squirtle': {'type': 'water', 'currentHP': 10},
                     'Pichu': {'type': 'electric', 'currentHP': 10},
                     'Shinx': {'type': 'electric', 'currentHP': 10},
                     'Mareep': {'type': 'electric', 'currentHP': 10},
                     'Caterpie': {'type': 'grass', 'currentHP': 10},
                     'Weedle': {'type': 'grass', 'currentHP': 10}}}
        actual = is_alive(character)
        self.assertEqual(expected, actual)

