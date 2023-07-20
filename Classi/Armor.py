"""
File creato da Gianluca

Definizione di una classe Armor

"""

class Armor:

    def __init__(self, name, armor_defence, price):
        self.name = name
        self.armor_defence = armor_defence
        self.price = price
    

    #funzione per prendere il nome dell'armatura
    def get_name_armor(self):
        return self.name
    
    #funzione per avere il costo dell'armatura
    def get_price_armor(self):
        print(f"This armor costs {self.price}")
        return self.price


        
