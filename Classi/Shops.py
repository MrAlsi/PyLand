"""

File creato da Federico Piras in data 18.07.2023

Definizione della classe negozio e dei singoli negozi

"""
from Character import Character
from weapon_objects import weapons_dict

class Shop:

    def __init__(self, name):
        self.name = name


class Smith(Shop):

    def __init__(self, name):
        self.name = name

    def show_available_weapons(self, character):
        """
        Function that shows the available weapons for the character playing
        :param character:
        :return:
        """
        character_type = type(character).__name__
        ## Gabriel fa grafica
        return weapons_dict[character_type]

    def buy_new_weapon(self, character, desired_weapon):
        """
        Function that allows to buy the new weapon
        :param character:
        :param desired_weapon:
        :return:
        """
        price = desired_weapon.price

        # Controllo per non comprare armi doppie
        weapons_names = []
        for element in character.inventory:
            weapons_names.append(element.name)

        # Se ha abbastanza soldi
        if character.has_enough_money(price) and (desired_weapon.name not in weapons_names):
            character.inventory.append(desired_weapon)
            # Se ha spazio nell'inventario:
            if character.has_enough_room_in_inventory():
                character.inventory.append(desired_weapon)
            else:
                print("Inventory is full or you already own the weapon")
                print(f"Your inventory: {weapons_names}")

    def sell_weapon(self, character):
        # Prendo inventario
        inventory = character.inventory

        # Ciclo sugli elementi dell'inventario e mi salvo i nomi delle armi
        weapon_names = []
        for element in inventory:
            weapon_names.append(element.name)

         # Chiedo all'utente quale arma vuole eliminare
        print("You have the following weapons in your inventory: which one would you like to sell?")
        print(f"Your weapons: {weapon_names}")
        weapon_to_sell = input("Write the weapon name: ")
        while weapon_to_sell not in weapon_names:
            weapon_to_sell = input("Write the weapon name: ")

        # Prendo l'indice dell'arma che mi ha detto l'utente
        idx_of_weapon_to_sell = weapon_names.index(weapon_to_sell)

        # Seleziono l'arma a quell'indice
        weapon_to_sell = inventory[idx_of_weapon_to_sell]
        price = weapon_to_sell.price

        # Il fabbro mi da il 30% del valore dell'arma quando gliela vendo
        price = 0.3 * price

        # Rimuovo l'arma dall'inventario
        inventory.pop(idx_of_weapon_to_sell)

        # Aumento il wallet
        character.wallet += price



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
        Allows a character to rent a room to restore some energies
        :param character: instance of character object
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


