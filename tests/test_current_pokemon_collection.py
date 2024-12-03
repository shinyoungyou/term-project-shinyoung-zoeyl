from unittest import TestCase
from data import current_pokemon_collection


class Test(TestCase):

    def test_current_pokemon_collection_user_level_1(self):
        level1 = {'Aron': {'type': 'rock', 'currentHP': 30}}
        level2 = {'Lairon': {'type': 'rock', 'currentHP': 50}}
        level3 = {'Aggron': {'type': 'rock', 'currentHP': 80}}

        result = current_pokemon_collection(1, level1, level2, level3)
        expected = {'Aron': {'type': 'rock', 'currentHP': 30}}

        self.assertEqual(result, expected)

    def test_current_pokemon_collection_user_level_2(self):
        level1 = {'Aron': {'type': 'rock', 'currentHP': 30}}
        level2 = {'Lairon': {'type': 'rock', 'currentHP': 50}}
        level3 = {'Aggron': {'type': 'rock', 'currentHP': 80}}

        result = current_pokemon_collection(2, level1, level2, level3)
        expected = {'Lairon': {'type': 'rock', 'currentHP': 50}}

        self.assertEqual(result, expected)

    def test_current_pokemon_collection_user_level_3(self):
        level1 = {'Aron': {'type': 'rock', 'currentHP': 30}}
        level2 = {'Lairon': {'type': 'rock', 'currentHP': 50}}
        level3 = {'Aggron': {'type': 'rock', 'currentHP': 80}}

        result = current_pokemon_collection(3, level1, level2, level3)
        expected = {'Aggron': {'type': 'rock', 'currentHP': 80}}

        self.assertEqual(result, expected)