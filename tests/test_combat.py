import unittest
from rpg.character import Character


class Test_combat(unittest.TestCase) : 

    def test_character_creation_defaults(self):
        # create a new charater
        char1 = Character()
        # test the character's name is "player"
        #print(char1.name == "player")
        self.assertEqual(char1.name, "player")

    def test_character_creation_from_file(self):
        # load a character from a file
        char2 = Character()
        char2.load_from_json('tests/data/dalinar.json')
        self.assertEqual("Dalinar", char2.name)

    def test_get_ac(self):
        """
        GIVEN a Character is the default instatiation
        WHEN the Character is instiantitated
        THEN the get_ac function to return a armor class that is dependent on its race
        """

        char = Character()
        self.assertEqual(char.get_ac(), 10)

        char.race = 'Kobold'
        self.assertEqual(char.get_ac(), 13)

        char.race = 'Human'
        self.assertEqual(char.get_ac(), 14)

        char.race = 'Dwarf'
        self.assertEqual(char.get_ac(), 15)

        char.race = 'Elf'
        self.assertEqual(char.get_ac(), 16)

        


