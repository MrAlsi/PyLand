# creato da Gianluca 
# Sottoclasse Personaggio con attributi: nome, sesso, esperienza, portafoglio, inventario

from Classi.Entity import Entity
import random


class Character(Entity):

    def __init__(self, lineage, name, level, weapon, life, basic_attack, defence, special_attack, gender, exp, wallet, inventory):
        super().__init__(lineage, name, level, weapon, life, basic_attack, defence, special_attack)
        self.gender = gender
        self.exp = exp
        self.wallet = wallet
        self.inventory = inventory
        self.max_inventory_len = 3

    # funzione per controllare se il personaggio ha abbastanza soldi per comprare gli oggetti
    def has_enough_money(self, price):
        flag = False
        if self.wallet - price >= 0:
            self.wallet -= price
            flag = True
        else:
            print(f"Your credit is not sufficient. The action costs {price}. your current balance is: {self.wallet}")
        return flag

    def fight(self, opponent):
        """
        Implements a fight between two PG.
        :param opponent: The opponent to fight. Must be an instance of class Character
        :return:
        """
        if isinstance(opponent, Character):
            dice_result = random.choice(range(1, 21))
            print(f" {self.name} STA ATTACCANDO {opponent.name}")
            if dice_result in list(range(1, 4)):
                print("L'avversario ha schivato, che sfiga!")
            elif dice_result in list(range(4, 18)):
                damage = int(self.attack()/opponent.defence * 5)
                opponent.life -= damage
                print(f"{opponent.name} ha subito il tuo danno e ha perso {damage} punti vita")
                opponent.print_lifepoints()
            elif dice_result in list(range(18, 21)):
                print(f"COLPO CRITICO! Parte l'attacco: {self.special_attack['nome'].capitalize()}")
                damage = int((self.attack() + self.special_attack['danno'])/opponent.defence * 5)
                opponent.life -= damage
                print(f"{opponent.name} ha subito il tuo danno e ha perso {damage} punti vita")
                opponent.print_lifepoints()

        else:
            print("Invalid INPUT. Opponent must be class Character")

    def has_enough_room_in_inventory(self):
        if len(self.inventory) < self.max_inventory_len:
            return True
        else:
            print("Spazio inventario pieno")
            return False

    def print_wallet_balance(self):
        print(f"Your Current balance is: {self.wallet}")

    def print_current_weapons(self):
        weapon_names = []
        for element in self.inventory:
            weapon_names.append(element.name)
        print("Le tue armi sono")
        print(weapon_names)