"""

File creato da Federico Piras in data 18.07.2023

Definizione della classe negozio e dei singoli negozi

"""
from Character import Character


class Shop:

    def __init__(self, name):
        self.name = name


class Smith(Shop):

    def __init__(self, name):
        self.name = name

    def buy_new_weapon(self):
        pass

    def upgrade_weapon(self, character, price):
        """
        Upgrades the weapon.
        :param character: must be an instance of Character
        :param price: int. Price of the upgrade
        :return:
        """
        if isinstance(character, Character):
            if character.has_enough_money(price):
                character.weapon.upgrade_level()
        else:
            print("Invalid INPUT. Character must be class Character")


class Tavern(Shop):

    def __init__(self):
        self.__price_per_night = 10

    def rent_a_room(self, character):
        """
        Allows
        :param character:
        :return:
        """
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


