import io
from unittest import TestCase
from unittest.mock import patch


from game import print_instructions


class TestPrintInstructions(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_instructions(self, mock_output):
        expected = ("\nWelcome to the world of Pokèmon! Embark on an exciting journey to become a Pokèmon Champion.\n"
                    "\nImportant notes to know before you begin:"
                    "\n- Stores are represented by S on the map."
                    "\n- Gyms are represented by G on the map."
                    "\n- You can catch wild pokèmons by throwing pokeball when their HP is less than 11."
                    "\n- If all six of your Pokémon lose their HP, the game is over."
                    "\n- You can only challenge a Gym Leader once you have a full team of six Pokémon."
                    "\n- After defeating a Gym Leader, you will earn a Badge, unlocking the next level."
                    "\n- Badge Requirements by Level:"
                    "\n  - Level 1: Defeat the gym leader twice to earn a badge."
                    "\n  - Level 2: Defeat the gym leader three times to earn a badge."
                    "\n  - Level 3: Defeat the gym leader four times to earn a badge and complete the mission."
                    "\n- The mission is complete when you defeat the final Gym Leader at Level 3.\n")
        print_instructions()
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
