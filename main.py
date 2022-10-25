from rpg.character import Character
from rpg.combat import Combat
from rpg.monster import Monster
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

def ply_function(result):
    #print("Hi, I'm the ply function")
    #value = input("Roll the dice.")

    if(result.get("hit")):
        print(f'{result.get("attacker_name")} scored a hit. {result.get("defender_name")} now has {result.get("defender_hp")}  hit points left.')
    else:
        print(f'{result.get("attacker_name")} missed.')

def end_game_function(winner):
    print(winner)
    print("Game OVer.")


dalinar = Character()
dalinar.load_from_json("characters/dalinar.json")
print(dalinar.name, dalinar.strength, dalinar.intel, dalinar.race)

monster = Monster()
monster.name = "Skeleton"
monster.hit_p_max = 8
monster.l_d = 1
monster.l_h = 4

for x in range(1000):
    game = Combat([dalinar], [monster], ply_function, end_game_function)

    game.start()


# j = Character()
# j.load_from_json("characters/jasnah.json")
# print(j.name, j.strength, j.intel, j.race)

# generator =  Generator()
# new_character = generator.character()
# print(new_character.hit_p_max, new_character.intel, new_character.race, new_character.p_class)