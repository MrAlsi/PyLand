"""
File creato da Federico Piras in data 18.07.2023

Definizione di una classe Weapon

"""

from math import ceil


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

    def upgrade_level(self):
        if self.level < self.max_level:
            self.level += 1
            self.damage = ceil(self.damage * 0.05 + self.damage)
        else:
            print("Weapon is already maxed out")

    def to_dict(self):
        return {
            "name" : self.name,
            "damage" : self.damage,
            "price" : self.price,
            "level" : self.level,
            "max_level" : self.max_level
        }

