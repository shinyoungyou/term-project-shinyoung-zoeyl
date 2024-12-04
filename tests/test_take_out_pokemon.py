from unittest import TestCase
from prepare_event import take_out_pokemon
from unittest.mock import patch


class Test(TestCase):

    @patch('random.choices', return_value=[[('Typhlosion', {'type': 'fire', 'currentHP': 80})]])
    def test_take_out_pokemon_random_pokemon_has_hp_greater_than_0(self, _):
        character_pokemons = {'Typhlosion': {'type': 'fire', 'currentHP': 80},
                              'Pidgeot': {'type': 'flying', 'currentHP': 80}}

        result = take_out_pokemon(character_pokemons)

        self.assertEqual(result, ('Typhlosion', {'type': 'fire', 'currentHP': 80}))

    @patch('random.choices', side_effect=[[('Typhlosion', {'type': 'fire', 'currentHP': 0})],
                                          [('Pidgeot', {'type': 'flying', 'currentHP': 80})]])
    def test_take_out_pokemon_random_pokemon_has_0hp(self, _):
        character_pokemons = {'Typhlosion': {'type': 'fire', 'currentHP': 0},
                              'Pidgeot': {'type': 'flying', 'currentHP': 80}}

        result = take_out_pokemon(character_pokemons)

        self.assertEqual(result, ('Pidgeot', {'type': 'flying', 'currentHP': 80}))