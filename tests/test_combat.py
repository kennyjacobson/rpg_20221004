import unittest
from rpg.character import Character

class Test_combat(unittest.TestCase):

    def test_character_creation(self):
        """
        GIVEN a Character institation with no parameters
        WHEN a Character is instantiated
        THEN the new object should have certain default
        """
        char1 = Character()
        self.assertEqual(char1.name, "player")

        #Load Character from file
        char2 = Character()
        char2.load_from_json("tests/data/test_char.json")
        self.assertEqual(char2.name, "Test Guy")