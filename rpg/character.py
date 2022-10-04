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
        self.p_class = 0
        self.level = 0
        self.hit_p_max = 0
        self.movement = 0
        self.armor = 0
        self.xp = 0
        self.type = ""
        self.current_weapon = ""
        self.current_armor = ""

    
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