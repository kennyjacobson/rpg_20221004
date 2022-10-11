from operator import truediv


class Combat():

    def __init__(self, player_characters, npcs, player_ply_function, endgame_function):
        #no idea if im doing this right but im trying!!!
        self.player_characters = player_characters
        self.npcs = npcs
        self.interactive_mode = True
        self.party_xp = 0
        self.party_success = False
        self.ordered_combatants = []
        self.player_ply_function = player_ply_function
        self.endgame_function = endgame_function

    def characters_dead(self):
        pass

    def combat_over(self):
        pass
        
    
    def end_combat(self):
        pass

    def ply(self):
        pass
        
    def print_stats(self):
        pass
    
    def turn(self):
        pass

    def start(self):
        pass