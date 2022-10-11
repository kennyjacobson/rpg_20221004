import json
class Character():
    def __init__(self):
        self.name = "player"
        self.strength = 0
        self.intel = 0
        self.wisdom = 0
        self.dexterity = 0
        self.constitution = 0
        self.charisma = 0
        self.race = ""
        self.p_class = ""
        self.level = 1
        self.hit_p_max = 0
        self.movement = 0
        self.armors = []
        self.weapons = []
        self.xp = 0
        self.type = ""
        self.current_weapon = ""
        self.current_armor = ""

    def load_from_json(self, path):
        with open(path) as f:
            character = json.load(f)

        
        self.name = character.get("name")
        self.strength = character.get("strength")
        self.intel = character.get("intel")
        self.wisdom = character.get("wisdom")
        self.dexterity = character.get("dexterity")
        self.constitution = character.get("constitution")
        self.charisma = character.get("charisma")
        self.race = character.get("race")
        self.p_class = character.get("p_class")
        self.level = character.get("level")
        self.hit_p_max = character.get("hit_p_max")
        self.movement = character.get("movement")
        self.xp = character.get("xp")
        
    
    def set_current_weapon(self):
        pass
    
    def roll_to_hit(self):
        pass

    def roll_for_damage(self):
        pass

    def get_ac(self):
        pass

    def get_movement(self):
        pass

    def get_ability_bonuses(self):
        pass