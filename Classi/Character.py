# creato da Gianluca 
# Sottoclasse Personaggio con attributi: nome, sesso, esperienza, portafoglio, inventario

import Entity;

class Character(Entity):
    def __init__(self, name, gender, exp, wallet, inventory):
        self.name = name
        self.gender = gender
        self.exp = exp
        self.wallet = wallet
        self.inventory = inventory

