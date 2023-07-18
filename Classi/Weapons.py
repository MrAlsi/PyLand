"""
File creato da Federico Piras in data 18.07.2023

Definizione di una classe Weapon

"""


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
        self.level += 1

