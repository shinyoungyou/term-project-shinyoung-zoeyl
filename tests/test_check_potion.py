from unittest import TestCase


from store import check_potion


class TestCheckPotion(TestCase):

    def test_check_potion_user_has_no_potion(self):
        expected = False
        number_of_potion = 0
        character_level = 1
        character_pokemon = ('Squirtle', {'type': 'water', 'currentHP': 10})
        actual = check_potion(number_of_potion, character_level, character_pokemon)
        self.assertEqual(expected, actual)

    def test_check_potion_character_pokemon_has_max_hp(self):
        expected = False
        number_of_potion = 1
        character_level = 1
        character_pokemon = ('Squirtle', {'type': 'water', 'currentHP': 40})
        actual = check_potion(number_of_potion, character_level, character_pokemon)
        self.assertEqual(expected, actual)

    def test_check_potion_user_has_potion_and_current_hp_is_less_than_max_hp_30(self):
        expected = True
        number_of_potion = 1
        character_level = 1
        character_pokemon = ('Squirtle', {'type': 'water', 'currentHP': 30})
        actual = check_potion(number_of_potion, character_level, character_pokemon)
        self.assertEqual(expected, actual)

    def test_check_potion_user_has_potion_and_current_hp_is_less_than_max_hp_20(self):
        expected = True
        number_of_potion = 1
        character_level = 1
        character_pokemon = ('Squirtle', {'type': 'water', 'currentHP': 20})
        actual = check_potion(number_of_potion, character_level, character_pokemon)
        self.assertEqual(expected, actual)

    def test_check_potion_user_has_potion_and_current_hp_is_less_than_max_hp_0(self):
        expected = True
        number_of_potion = 1
        character_level = 1
        character_pokemon = ('Squirtle', {'type': 'water', 'currentHP': 0})
        actual = check_potion(number_of_potion, character_level, character_pokemon)
        self.assertEqual(expected, actual)
