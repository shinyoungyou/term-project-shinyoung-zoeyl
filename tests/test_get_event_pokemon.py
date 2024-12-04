from unittest import TestCase
from prepare_event import get_event_pokemon
from unittest.mock import patch


class Test(TestCase):

    @patch('random.choices', return_value=[('Typhlosion', {'type': 'fire', 'currentHP': 80})])
    def test_get_event_pokemon_no_overlap_with_user_pokemon(self, _):
        character = {'Current Level': 3, 'Poke Ball': {'Venusaur': {'type': 'grass', 'currentHP': 100}}}

        result = get_event_pokemon(character)
        expected = ('Typhlosion', {'type': 'fire', 'currentHP': 80})

        self.assertEqual(result, expected)

    @patch('random.choices', side_effect=[[('Slowking', {'type': 'water', 'currentHP': 80})],
                                         [('Typhlosion', {'type': 'fire', 'currentHP': 80})]])
    def test_get_event_pokemon_overlap_with_user_pokemon(self, _):
        character = {'Current Level': 3, 'Poke Ball': {'Venusaur': {'type': 'grass', 'currentHP': 100},
                                                       'Slowking': {'type': 'water', 'currentHP': 80}}}

        result = get_event_pokemon(character)

        self.assertEqual(result, ('Typhlosion', {'type': 'fire', 'currentHP': 80}))