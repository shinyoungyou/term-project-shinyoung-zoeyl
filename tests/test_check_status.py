from unittest import TestCase
from event_pokemon_attack import check_status


class Test(TestCase):
    def test_check_status_pokemon_hp_is_less_than_1(self):
        character_pokemon = ('Beedrill', {'type': 'grass', 'currentHP': -3})
        result = check_status(character_pokemon)

        self.assertFalse(result)

    def test_check_status_pokemon_hp_is_greater_than_0(self):
        character_pokemon = ('Beedrill', {'type': 'grass', 'currentHP': 7})
        result = check_status(character_pokemon)

        self.assertTrue(result)
