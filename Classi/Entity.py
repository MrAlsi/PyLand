# creato da Gianluca 
# classe Entità con gli attributi. casata, livello, vita, attacco base, difesa, attacco speciale

from Character import Character
import random


class Entity:

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

        :param life_to_add:
        :return:
        """
        if self.life == self.maxlife:
            print("Life is already maxed out")
        elif self.life + life_to_add > self.maxlife:
            self.life = self.maxlife
        else:
            self.life += life_to_add
        self.print_lifepoints()

    def is_equipped(self):
        return True if self.weapon is not None else False

    def attack(self):
        return self.basic_damage + self.weapon.damage if self.is_equipped() else self.basic_damage

    def combat(self, opponent):
        if isinstance(opponent, Character):
            dodge_chance = random.choice(range(1, 11))
            if dodge_chance == 1:
                print("L'avversario ha schivato, che sfiga!")
            else:
                damage = int(self.attack()/opponent.defence * 5)
                opponent.life -= damage
                print(f"L'avversario ha subito il tuo danno e ha perso {damage} punti vita")
                opponent.print_lifepoints()
        else:
            print("Invalid INPUT. Opponent must be class Character")

