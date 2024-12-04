from unittest import TestCase
from unittest.mock import patch
from event_option import fight
import io


class Test(TestCase):

    @patch('event_option.get_skill_of')
    @patch('event_option.choose_skill_to_challenge')
    @patch('event_option.get_probability')
    @patch('event_option.get_attack_result')
    def test_fight_when_skill_hit_and_defeated_pokemon(self, mock_get_attack_result, mock_get_probability,
                                                       mock_choose_skill_to_challenge, mock_get_skill_of):

        mock_get_attack_result.return_value = False
        mock_get_probability.return_value = True

        character_pokemon = ('Blastoise', {'type': 'water', 'currentHP': 100})
        event_pokemon_info = ('Beedrill', {'type': 'grass', 'currentHP': 80})
        character = {'Current Level': 3}
        result = fight(character_pokemon, event_pokemon_info, character, "Team Rocket")

        mock_get_skill_of.assert_called_once()
        mock_choose_skill_to_challenge.assert_called_once()
        mock_get_attack_result.assert_called_once()

        self.assertEqual(result, False)

    @patch('event_option.get_skill_of')
    @patch('event_option.choose_skill_to_challenge')
    @patch('event_option.get_probability')
    @patch('event_option.get_attack_result')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fight_when_skill_did_not_hit(self, mock_output, mock_get_attack_result, mock_get_probability,
                                          mock_choose_skill_to_challenge, mock_get_skill_of):

        mock_get_probability.return_value = False
        mock_choose_skill_to_challenge.return_value = {'name': 'Solar Beam', 'damage': (6, 7)}

        character_pokemon = ('Blastoise', {'type': 'water', 'currentHP': 100})
        event_pokemon_info = ('Beedrill', {'type': 'grass', 'currentHP': 80})
        character = {'Current Level': 3}
        fight(character_pokemon, event_pokemon_info, character, "Team Rocket")

        mock_get_attack_result.assert_not_called()
        mock_get_skill_of.assert_called_once()

        the_game_printed_this = mock_output.getvalue()
        expected = '\nSolar Beam missed!\nEvent Pokémon status: Beedrill(HP: 80)\n'

        self.assertIn(expected, the_game_printed_this)