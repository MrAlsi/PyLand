# creato da Gianluca 
# Sottoclasse di Personaggio chiamata Ninja con attributi: 

from Classi.Character import Character


class Ninja(Character):
    def __init__(self, lineage, name, level, weapon, life, basic_attack, defence, special_attack, gender, exp, wallet, inventory):
        super().__init__(lineage, name, level, weapon, life, basic_attack, defence, 
                         {'nome': 'Shadow Clone', 'danno':special_attack}, gender, exp, wallet, inventory)
        # self.valid_weapons = ['shuriken']
