from unittest import TestCase
from data import get_skill_of


class Test(TestCase):

    def test_get_skill_of_pokemon_type_is_fire(self):
        result = get_skill_of('fire')

        expected = [{'name': 'Tackle', 'damage': (1, 3)}, {'name': 'Flamethrower', 'damage': (4, 5)},
                    {'name': 'Fire Punch', 'damage': (6, 7)}]
        self.assertEqual(result, expected)

    def test_get_skill_of_pokemon_type_is_ice(self):
        result = get_skill_of('ice')

        expected = [{'name': 'Tackle', 'damage': (1, 3)}, {'name': 'Blizzard', 'damage': (4, 5)},
                    {'name': 'Ice Fang', 'damage': (6, 7)}]
        self.assertEqual(result, expected)

    def test_get_skill_of_pokemon_type_is_flying(self):
        result = get_skill_of('flying')

        expected = [{'name': 'Pluck', 'damage': (1, 3)}, {'name': 'Gust', 'damage': (4, 5)},
                    {'name': 'Aerial Ace', 'damage': (6, 7)}]
        self.assertEqual(result, expected)