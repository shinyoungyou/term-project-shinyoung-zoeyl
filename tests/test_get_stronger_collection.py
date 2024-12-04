from unittest import TestCase
from event_pokemon_attack import get_stronger_collection


class Test(TestCase):

    def test_get_stronger_collection_user_level_is_1(self):
        result = get_stronger_collection(1)
        expected = (1, 1.3, 1.4, 1.5)

        self.assertEqual(result, expected)

    def test_get_stronger_collection_user_level_is_2(self):
        result = get_stronger_collection(2)
        expected = (1.3, 1.5, 1.7, 2)

        self.assertEqual(result, expected)

    def test_get_stronger_collection_user_level_is_3(self):
        result = get_stronger_collection(3)
        expected = (1.5, 1.7, 2, 2.5)

        self.assertEqual(result, expected)
