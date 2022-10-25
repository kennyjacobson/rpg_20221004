import random

class Monster():
    def __init__(self):
        #l_d = low damage
        #h_d = high damage
        self.name = ""
        self.type = ""
        self.ac = 11
        self.hit_p_max = 0
        self.l_d = 0
        self.h_d = 0
        self.morale = ""
        self.movement = 0
        self.xp = 0

    def roll_to_hit(self):
        return random.randint(3,18)

    def roll_for_damage(self):
        return random.randint(1,4)

    def get_ac(self):
        return 12

    def get_movement(self):
        pass