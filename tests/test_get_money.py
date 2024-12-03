from unittest import TestCase
from unittest.mock import patch
from event_option import get_money


class Test(TestCase):

    @patch('event_option.make_stronger')
    @patch('random.randrange', return_value=5)
    def test_get_money_event_type_is_wild_pokemon(self, _, mock_make_stronger):
        mock_make_stronger.return_value = 1.3

        character = {'Money': 20, 'Current Level': 2}
        get_money(character, 'wildPokemon')
        result = character['Money']

        self.assertEqual(result, 26)

    @patch('event_option.make_stronger')
    @patch('random.randrange', return_value=27)
    def test_get_money_event_type_is_team_rocket(self, _, mock_make_stronger):
        mock_make_stronger.return_value = 1.3

        character = {'Money': 20, 'Current Level': 2}
        get_money(character, 'Team Rocket')
        result = character['Money']

        self.assertEqual(result, 55)

    @patch('event_option.make_stronger')
    @patch('random.randrange', return_value=16)
    def test_get_money_event_type_is_strange_trainer(self, _, mock_make_stronger):
        mock_make_stronger.return_value = 1.3

        character = {'Money': 20, 'Current Level': 2}
        get_money(character, 'Team Rocket')
        result = character['Money']

        self.assertEqual(result, 40)
