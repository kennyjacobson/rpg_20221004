from rpg.character import Character
import random

class Generator():
    def __init__(self):
        pass

    def character(self):
        char = Character()
        char.hit_p_max = 6
        char.strength = random.randint(3,19)
        char.intel = random.randint(3,19)
        char.wisdom = random.randint(3,19)
        char.dexterity = random.randint(3,19)
        char.constitution = random.randint(3,19)
        char.charisma = random.randint(3,19)

        char.race = random.choice(["Human", "Dwarf", "Elf"])
        char.p_class = random.choice(["Fighter", "Thief", "Cleric"])

        return char