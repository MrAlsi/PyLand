"""

File creato da Federico Piras in data 18.07.2023

Definizione della classe negozio e dei singoli negozi

"""
from Classi.Character import Character
from weapon_objects import weapons_dict


class Shop:

    def __init__(self, name):
        self.name = name


class Smith(Shop):

    def __init__(self, name):
        self.name = 'Mario'

    def show_available_weapons(self, character):
        """
        Function that shows the available weapons for the character playing
        :param character:
        :return:
        """
        character_type = type(character).__name__
        weapon_names = []
        weapon_prices = []
        for element in weapons_dict[character_type]:
            weapon_names.append(element.name)
            weapon_prices.append(element.price)

        print("Puoi comprare le seguenti armi:")
        for nome_arma, prezzo_arma in list(zip(weapon_names, weapon_prices)):
            print(f"Nome: {nome_arma}, prezzo: {prezzo_arma}")
        return weapon_names

    def buy_new_weapon(self, character):
        """
        Function that allows to buy the new weapon
        :param character:
        :param desired_weapon:
        :return:
        """

        if character.has_enough_room_in_inventory():

            # Facciamo vedere le armi disponibili
            list_of_available_weapons = self.show_available_weapons(character)

            # Chiedo l'arma
            desired_weapon = input("Che arma vuoi? ")
            while desired_weapon not in list_of_available_weapons:
                desired_weapon = input("Hai inserito un nome arma non valido. Che arma vuoi? ")

            character_type = type(character).__name__

            # Controllo per non comprare armi doppie
            weapons_names = []
            for element in character.inventory:
                weapons_names.append(element.name)

            if desired_weapon in weapons_names:
                print("Hai già questa arma")

            else:
                # Mi serve per l'indice
                weapon_names = []
                for element in weapons_dict[character_type]:
                    weapon_names.append(element.name)

                # Prendo l'indice dell'arma che voglio comprare
                weapon_index = weapon_names.index(desired_weapon)

                # Prendo l'arma che voglio comprare
                weapon = weapons_dict[character_type][weapon_index]
                price = weapon.price

                # Se ha abbastanza soldi
                if character.has_enough_money(price) and character.has_enough_room_in_inventory():
                    character.inventory.append(weapon)
                    print("Acquisto avvenuto con successo")
                    character.print_wallet_balance()

    def sell_weapon(self, character):
        """
        Funzione per vendere un'arma
        :param character:
        :return:
        """
        # Prendo inventario
        inventory = character.inventory

        # Se non hai armi...
        if len(inventory) == 0:
            print("Non hai armi da vendere. Torna un'altra volta")

        else:

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
            flag = int(input(f"Guadagnerai {price} dalla vendita. 1 per continuare, 0 per interrompere"))
            while flag not in [0, 1]:
                flag = int(input(f"Input errato. 1 per continuare, 0 per interrompere"))

            if flag:
                inventory.pop(idx_of_weapon_to_sell)
                print("Vendita avvenuta con successo")
                print(f"Balance precedente: {character.wallet}")
                # Aumento il wallet
                character.wallet += price
                print(f"Balance attuale: {character.wallet}")
            else:
                print("Vendita fallita")

    def upgrade_weapon(self, character):
        """
        Upgrades the weapon.
        :param character: must be an instance of Character
        :param price: int. Price of the upgrade
        :return:
        """

        # Prendo inventario
        inventory = character.inventory

        #  Se ho solo un'arma...
        if len(inventory) == 1:
            index_of_weapon = 0

        # Se ho più di una arma...
        elif len(inventory) > 1:
            # Ciclo sugli elementi dell'inventario e mi salvo i nomi delle armi
            weapon_names = []
            for element in inventory:
                weapon_names.append(element.name)

            # Mostro le armi disponibili e chiedo all'utente quale vuole upgradare
            print("Le armi disponibili sono: ")
            print(weapon_names)
            weapon_to_upgrade = input("Che arma vuoi upgradare?")

            # Finchè non mi dai un nome valido...
            while weapon_to_upgrade not in weapon_names:
                weapon_to_upgrade = input("Nome non valido! Che arma vuoi upgradare?")
                print(weapon_names)

            index_of_weapon = weapon_names.index(weapon_to_upgrade)

        # Adesso che ho l'indice dell'arma che voglio migliorare, calcolo il prezzo dell'upgrade
        weapon = inventory[index_of_weapon]
        base_price = weapon.price
        level = weapon.level
        const = 0.3
        upgrade_price = base_price + base_price * (level + 1) * const

        # Printiamo qualcosa:
        print(f"Arma scelta: {weapon.name}. Prezzo: {upgrade_price}.")
        flag = int(input("Digita 1 per continuare, 0 per interrompere"))
        while flag not in [0, 1]:
            flag = int(input("Carattere non valido. Digita 1 per continuare, 0 per interrompere"))

        previous_level = weapon.level
        if flag:
            # Se effettivamente è un pg che sta interagendo con il fabbro...
            if isinstance(character, Character):
                if character.has_enough_money(upgrade_price):
                    character.inventory[index_of_weapon].upgrade_level()
                    current_level = character.inventory[index_of_weapon].level
                    print(f"Upgrade avvenuto con successo da livello {previous_level} ---> {current_level}")
            else:
                print("Invalid INPUT. Character must be class Character")
        else:
            print("Nessun upgrade effettuato")



class Tavern(Shop):

    def __init__(self, name):
        self.name = name
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


