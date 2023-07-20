# creato da Gianluca 
# classe Entità con gli attributi. casata, livello, vita, attacco base, difesa, attacco speciale

import random


class Entity:
    # Ricordati che quando crei un nuovo PG livello default è 1 e exp default è 0
    def __init__(self, lineage, name, level, weapon, life, basic_attack, defence, special_attack):
        self.lineage = lineage
        self.name = name
        self.level = level
        self.weapon = weapon
        self.life = life
        self.basic_attack = basic_attack
        self.defence = defence
        self.special_attack = special_attack
        self.maxlife = 200

    def print_lifepoints(self):
        """
        Prints PG life points
        :return:
        """
        print(f"Current life is {self.life}/{self.maxlife}")

    def add_lifepoints(self, life_to_add):
        """
        Adds life points to PG
        :param life_to_add: int. Value of life to add to current life
        :return:
        """
        if self.life == self.maxlife:
            print("Life is already maxed out")
        elif self.life + life_to_add > self.maxlife:
            self.life = self.maxlife
        else:
            self.life += life_to_add
        self.print_lifepoints()

    def equip_with_weapon(self, weapon):
        self.weapon = weapon

    def is_equipped(self):
        """
        Checks if the PG is equipped with a weapon
        :return:
        """
        return True if self.weapon is not None else False

    def attack(self):
        """
        Returns total attack points of the PG
        :return:
        """
        return self.basic_attack + self.weapon.damage if self.is_equipped() else self.basic_attack

    def take_damage(self, damage):
        self.life -= damage




