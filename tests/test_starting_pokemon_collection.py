from unittest import TestCase
from unittest.mock import patch
from data import starting_pokemon_collection


class Test(TestCase):

    @patch('data.current_pokemon_collection')
    def test_starting_pokemon_collection_user_level_is_1(self, mock_current_pokemon_collection):
        mock_current_pokemon_collection.return_value = {'Squirtle': {'type': 'water', 'currentHP': 40},
                                                        'Charmander': {'type': 'fire', 'currentHP': 40},
                                                        'Bulbasaur': {'type': 'grass', 'currentHP': 40}}

        result = starting_pokemon_collection(1)
        expected = {'Squirtle': {'type': 'water', 'currentHP': 40},
                    'Charmander': {'type': 'fire', 'currentHP': 40},
                    'Bulbasaur': {'type': 'grass', 'currentHP': 40}}

        self.assertEqual(result, expected)

    @patch('data.current_pokemon_collection')
    def test_starting_pokemon_collection_user_level_is_2(self, mock_current_pokemon_collection):
        mock_current_pokemon_collection.return_value = {'Wartortle': {'type': 'water', 'currentHP': 65},
                                                        'Charmeleon': {'type': 'fire', 'currentHP': 65},
                                                        'Ivysaur': {'type': 'grass', 'currentHP': 65}}

        result = starting_pokemon_collection(1)
        expected = {'Wartortle': {'type': 'water', 'currentHP': 65},
                    'Charmeleon': {'type': 'fire', 'currentHP': 65},
                    'Ivysaur': {'type': 'grass', 'currentHP': 65}}

        self.assertEqual(result, expected)

    @patch('data.current_pokemon_collection')
    def test_starting_pokemon_collection_user_level_is_3(self, mock_current_pokemon_collection):
        mock_current_pokemon_collection.return_value = {'Blastoise': {'type': 'water', 'currentHP': 100},
                                                        'Charizard': {'type': 'fire', 'currentHP': 100},
                                                        'Venusaur': {'type': 'grass', 'currentHP': 100}}

        result = starting_pokemon_collection(1)
        expected = {'Blastoise': {'type': 'water', 'currentHP': 100},
                    'Charizard': {'type': 'fire', 'currentHP': 100},
                    'Venusaur': {'type': 'grass', 'currentHP': 100}}

        self.assertEqual(result, expected)