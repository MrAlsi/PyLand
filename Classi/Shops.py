"""

File creato da Federico Piras in data 18.07.2023

Definizione della classe negozio e dei singoli negozi

"""
from Character import Character


class Shop:

    def __init__(self, name):
        self.name = name


class Smith(Shop):

    def __init__(self, attribute1):
        self.attribute1 = attribute1

    def buy_new_weapon(self):
        pass

    def upgrade_weapon(self, character, weapon, price):
        if type(weapon) == "Weapon" and type(character) == "Character":
            if character.has_enough_money(price):
                weapon.upgrade_level()
        else:
            if type(weapon) != "Weapon":
                print(f"Invalid input class. Weapon must be class class Weapon. Your input is of class {type(weapon)}")
            elif type(character) == "Character":
                print(f"Invalid input class. Character must be class class Character. Your input is of class {type(character)}")


class Tavern(Shop):

    def __init__(self):
        self.__price_per_night = 10

    def rent_a_room(self, character):
        if isinstance(character, Character):
            n_nights = int(input("How many nights do you want to stay?"))
            price = self.price_per_night * n_nights
            if character.has_enough_money(price):
                n_hours_per_night = 8
                n_lifepoints_per_hour = 3
                life_to_add = n_nights * n_hours_per_night * n_lifepoints_per_hour
                character.add_lifepoints(life_to_add)

        else:
            print(f"Invalid input class. Character must be class class Character. Your input is of class {type(character)}")

    def drink_a_beer(self, character):
        if isinstance(character, Character):
            beer_price = 3
            n_beers = int(input("How many beers do you want to drink?"))
            price = n_beers * beer_price
            if character.has_enough_money(price):
                n_lifepoints_per_beer = 2
                life_to_add = n_lifepoints_per_beer * n_beers
                character.add_lifepoints(life_to_add)
        else:
            print(f"Invalid input class. Character must be class class Character. Your input is of class {type(character)}")


