# creato da Gianluca 
# Sottoclasse di Personaggio chiamata Mago con attributi: 

from Classi.Character import Character


class Wizard(Character):
    def __init__(self, lineage, name, level, weapon, life, basic_attack, defence, special_attack, gender, exp, wallet, inventory):
        super().__init__(lineage, name, level, weapon, life, basic_attack, defence, special_attack, gender, exp, wallet, inventory)
