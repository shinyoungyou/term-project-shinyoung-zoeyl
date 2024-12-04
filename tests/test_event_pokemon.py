from unittest import TestCase
from unittest.mock import patch
from data import event_pokemon


class Test(TestCase):

    @patch('data.current_pokemon_collection')
    def test_event_pokemon_user_level_is_1(self, mock_current_pokemon_collection):
        mock_current_pokemon_collection.return_value = {'Pichu': {'type': 'electric', 'currentHP': 30},
                                                        'Shinx': {'type': 'electric', 'currentHP': 30},
                                                        'Mareep': {'type': 'electric', 'currentHP': 30},
                                                        'Caterpie': {'type': 'grass', 'currentHP': 30},
                                                        'Weedle': {'type': 'grass', 'currentHP': 30},
                                                        'Treecko': {'type': 'grass', 'currentHP': 30},
                                                        'Pidgey': {'type': 'flying', 'currentHP': 30},
                                                        'Pidove': {'type': 'flying', 'currentHP': 30},
                                                        'Slowpoke': {'type': 'water', 'currentHP': 30},
                                                        'Horsea': {'type': 'water', 'currentHP': 30},
                                                        'Mudkip': {'type': 'water', 'currentHP': 30},
                                                        'Cyndaquil': {'type': 'fire', 'currentHP': 30},
                                                        'Totodile': {'type': 'fire', 'currentHP': 30},
                                                        'Magby': {'type': 'fire', 'currentHP': 30},
                                                        'Swinub': {'type': 'ice', 'currentHP': 30},
                                                        'Spheal': {'type': 'ice', 'currentHP': 30},
                                                        'Vanillite': {'type': 'ice', 'currentHP': 30},
                                                        'Geodude': {'type': 'rock', 'currentHP': 30},
                                                        'Aron': {'type': 'rock', 'currentHP': 30},
                                                        'Roggenrola': {'type': 'rock', 'currentHP': 30}}

        result = event_pokemon(1)
        expected = {'Pichu': {'type': 'electric', 'currentHP': 30},
                    'Shinx': {'type': 'electric', 'currentHP': 30},
                    'Mareep': {'type': 'electric', 'currentHP': 30},
                    'Caterpie': {'type': 'grass', 'currentHP': 30},
                    'Weedle': {'type': 'grass', 'currentHP': 30},
                    'Treecko': {'type': 'grass', 'currentHP': 30},
                    'Pidgey': {'type': 'flying', 'currentHP': 30},
                    'Pidove': {'type': 'flying', 'currentHP': 30},
                    'Slowpoke': {'type': 'water', 'currentHP': 30},
                    'Horsea': {'type': 'water', 'currentHP': 30},
                    'Mudkip': {'type': 'water', 'currentHP': 30},
                    'Cyndaquil': {'type': 'fire', 'currentHP': 30},
                    'Totodile': {'type': 'fire', 'currentHP': 30},
                    'Magby': {'type': 'fire', 'currentHP': 30},
                    'Swinub': {'type': 'ice', 'currentHP': 30},
                    'Spheal': {'type': 'ice', 'currentHP': 30},
                    'Vanillite': {'type': 'ice', 'currentHP': 30},
                    'Geodude': {'type': 'rock', 'currentHP': 30},
                    'Aron': {'type': 'rock', 'currentHP': 30},
                    'Roggenrola': {'type': 'rock', 'currentHP': 30}}

        self.assertEqual(result, expected)

    @patch('data.current_pokemon_collection')
    def test_event_pokemon_user_level_is_2(self, mock_current_pokemon_collection):
        mock_current_pokemon_collection.return_value = {'Pikachu': {'type': 'electric', 'currentHP': 50},
                                                        'Luxio': {'type': 'electric', 'currentHP': 50},
                                                        'Flaaffy': {'type': 'electric', 'currentHP': 50},
                                                        'Metapod': {'type': 'grass', 'currentHP': 50},
                                                        'Kakuna': {'type': 'grass', 'currentHP': 50},
                                                        'Grovyle': {'type': 'grass', 'currentHP': 50},
                                                        'Pidgeotto': {'type': 'flying', 'currentHP': 50},
                                                        'Tranquill': {'type': 'flying', 'currentHP': 50},
                                                        'Slowbro': {'type': 'water', 'currentHP': 50},
                                                        'Seadra': {'type': 'water', 'currentHP': 50},
                                                        'Marshtomp': {'type': 'water', 'currentHP': 50},
                                                        'Quilava': {'type': 'fire', 'currentHP': 50},
                                                        'Croconaq': {'type': 'fire', 'currentHP': 50},
                                                        'Magmar': {'type': 'fire', 'currentHP': 50},
                                                        'Piloswine': {'type': 'ice', 'currentHP': 50},
                                                        'Sealeo': {'type': 'ice', 'currentHP': 50},
                                                        'Vanillish': {'type': 'ice', 'currentHP': 50},
                                                        'Graveler': {'type': 'rock', 'currentHP': 50},
                                                        'Lairon': {'type': 'rock', 'currentHP': 50},
                                                        'Boldore': {'type': 'rock', 'currentHP': 50}}

        result = event_pokemon(2)
        expected = {'Pikachu': {'type': 'electric', 'currentHP': 50},
                    'Luxio': {'type': 'electric', 'currentHP': 50},
                    'Flaaffy': {'type': 'electric', 'currentHP': 50},
                    'Metapod': {'type': 'grass', 'currentHP': 50},
                    'Kakuna': {'type': 'grass', 'currentHP': 50},
                    'Grovyle': {'type': 'grass', 'currentHP': 50},
                    'Pidgeotto': {'type': 'flying', 'currentHP': 50},
                    'Tranquill': {'type': 'flying', 'currentHP': 50},
                    'Slowbro': {'type': 'water', 'currentHP': 50},
                    'Seadra': {'type': 'water', 'currentHP': 50},
                    'Marshtomp': {'type': 'water', 'currentHP': 50},
                    'Quilava': {'type': 'fire', 'currentHP': 50},
                    'Croconaq': {'type': 'fire', 'currentHP': 50},
                    'Magmar': {'type': 'fire', 'currentHP': 50},
                    'Piloswine': {'type': 'ice', 'currentHP': 50},
                    'Sealeo': {'type': 'ice', 'currentHP': 50},
                    'Vanillish': {'type': 'ice', 'currentHP': 50},
                    'Graveler': {'type': 'rock', 'currentHP': 50},
                    'Lairon': {'type': 'rock', 'currentHP': 50},
                    'Boldore': {'type': 'rock', 'currentHP': 50}}

        self.assertEqual(result, expected)

    @patch('data.current_pokemon_collection')
    def test_event_pokemon_user_level_is_3(self, mock_current_pokemon_collection):
        mock_current_pokemon_collection.return_value = {'Raichu': {'type': 'electric', 'currentHP': 80},
                                                        'Luxray': {'type': 'electric', 'currentHP': 80},
                                                        'Ampharos': {'type': 'electric', 'currentHP': 80},
                                                        'Butterfree': {'type': 'grass', 'currentHP': 80},
                                                        'Beedrill': {'type': 'grass', 'currentHP': 80},
                                                        'Sceptile': {'type': 'grass', 'currentHP': 80},
                                                        'Pidgeot': {'type': 'flying', 'currentHP': 80},
                                                        'Pidove': {'type': 'flying', 'currentHP': 80},
                                                        'Slowking': {'type': 'water', 'currentHP': 80},
                                                        'Kingdra': {'type': 'water', 'currentHP': 80},
                                                        'Swampert': {'type': 'water', 'currentHP': 80},
                                                        'Typhlosion': {'type': 'fire', 'currentHP': 80},
                                                        'Reraligatr': {'type': 'fire', 'currentHP': 80},
                                                        'Magmortar': {'type': 'fire', 'currentHP': 80},
                                                        'Mamoswine': {'type': 'ice', 'currentHP': 80},
                                                        'Walrein': {'type': 'ice', 'currentHP': 80},
                                                        'Vanilluxe': {'type': 'ice', 'currentHP': 80},
                                                        'Golem': {'type': 'rock', 'currentHP': 80},
                                                        'Aggron': {'type': 'rock', 'currentHP': 80},
                                                        'Gigalith': {'type': 'rock', 'currentHP': 80}}

        result = event_pokemon(3)
        expected = {'Raichu': {'type': 'electric', 'currentHP': 80},
                    'Luxray': {'type': 'electric', 'currentHP': 80},
                    'Ampharos': {'type': 'electric', 'currentHP': 80},
                    'Butterfree': {'type': 'grass', 'currentHP': 80},
                    'Beedrill': {'type': 'grass', 'currentHP': 80},
                    'Sceptile': {'type': 'grass', 'currentHP': 80},
                    'Pidgeot': {'type': 'flying', 'currentHP': 80},
                    'Pidove': {'type': 'flying', 'currentHP': 80},
                    'Slowking': {'type': 'water', 'currentHP': 80},
                    'Kingdra': {'type': 'water', 'currentHP': 80},
                    'Swampert': {'type': 'water', 'currentHP': 80},
                    'Typhlosion': {'type': 'fire', 'currentHP': 80},
                    'Reraligatr': {'type': 'fire', 'currentHP': 80},
                    'Magmortar': {'type': 'fire', 'currentHP': 80},
                    'Mamoswine': {'type': 'ice', 'currentHP': 80},
                    'Walrein': {'type': 'ice', 'currentHP': 80},
                    'Vanilluxe': {'type': 'ice', 'currentHP': 80},
                    'Golem': {'type': 'rock', 'currentHP': 80},
                    'Aggron': {'type': 'rock', 'currentHP': 80},
                    'Gigalith': {'type': 'rock', 'currentHP': 80}}

        self.assertEqual(result, expected)
