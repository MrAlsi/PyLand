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
        if self.level < self.max_level:
            self.level += 1
            self.damage = int(self.damage * 0.05 + self.damage)
        else:
            print("Weapon is already maxed out")

