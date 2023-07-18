"""
File creato da Federico Piras in data 18.07.2023

Definizione di una classe Weapon

"""

#Devo upgradare il damage
class Weapon:

    def __init__(self, name, damage, price, level):
        self.name = name
        self.damage = damage
        self.price = price
        self.level = level
        self.max_level = 10

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_price(self):
        print(f"This weapon costs {self.price}")
        return self.price

    # def upgrade_level(self):
    #     if self.level < self.max_level:
    #         self.level += 1
    #     else:
    #         print(f"Cannot upgrade weapon level. Weapon is already at maximum level")
    #
    # def upgrade_damage(self):
    #     self

