# creato da Gianluca 
# Sottoclasse di Personaggio chiamata Ninja con attributi: 

import Character;


class Ninja(Character):
    def __init__(self, gender, exp, wallet, inventory):
        super().__init__(gender, exp, wallet, inventory)
        # self.valid_weapons = ['shuriken']
