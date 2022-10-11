from rpg.character import Character
from rpg.weapon import Weapon
from rpg.armor import Armor
from utils.generator import Generator

# print("Hello World!")

# sword = Weapon()
# print(sword.name)
# sword.load('weapons/sword.json')
# print(sword.name)

# chainmail = Armor()
# chainmail.load('armor/chainmail.json')
# print(chainmail.name)


# dalinar = Character()
# dalinar.load_from_json("characters/dalinar.json")
# print(dalinar.name, dalinar.strength)

generator =  Generator()
new_character = generator.character()
print(new_character.hit_p_max, new_character.intel)