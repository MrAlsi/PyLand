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
        self.experience_to_next_level = 100

    def ask_to_equip(self):
        """
        Chiede al giocatore se vuole equipaggiare l'arma
        :return:
        """

        # Chiede se vuoi equipaggiare
        choice = int(input("Non hai nessun arma equipaggiata, vuoi equipaggiare? 1 per sì, 0 per no: "))

        # Se mi dici sì...
        if choice == 1:
            # Se hai delle armi nell'inventario ti chiedo quale vuoi
            if len(self.inventory) > 0:
                # Fa vedere armi disponibili
                weapons_list = []
                print("Le armi disponibili sono: ")
                for element in self.inventory:
                    print(f"Arma: {element.name}, Danno: {element.damage}")
                    weapons_list.append(element.name)

                # Scegli l'arma
                weapon_name = input("Digita il nome dell'arma che vuoi equipaggiare nel combat")
                idx = weapons_list.index(weapon_name)
                weapon_to_equip = self.inventory[idx]

                # Equipaggia l'arma
                self.equip_with_weapon(weapon_to_equip)
                print(f"Arma {self.weapon.name} equipaggia con successo")

            else:
                print("Non hai armi da equipaggiare! Combatti a mani nude")
                input("premi invio per iniziare a combattere")

        else:
            print("Hai scelto di non equipaggiarti. Combatti a mani nude!")
            input("premi invio per iniziare a combattere")

    def disequip_weapon(self):
        """
        Disequipaggia l'arma dal giocatore
        :return:
        """
        self.weapon = None
        print("Arma disequipaggiata con successo")

    # funzione per controllare se il personaggio ha abbastanza soldi per comprare gli oggetti
    def has_enough_money(self, price):
        """
        Controlla se il giocatore ha abbastanza soldi per eseguire la tansazione.
        Se sì, aggiorno al wallet, se no avvisa che non ho abastanza soldi
        :param price:
        :return:
        """
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
        # Controllo se mi sto interfacciando con una entità affrontabile (esempio: no fabbro o locanda)
        if isinstance(opponent, Entity):

            # COMBATTIMENTO!

            # TIRIAMO UN DADO PER STABILIRE IL TIPO DI ATTACCO
            dice_result = random.choice(range(1, 21))
            print(f"{self.name} STA ATTACCANDO {opponent.name}")

            # SE IL DADO E' IN RANGE [1,3] ALLORA IL MIO COLPO VIENE MISSATO
            if dice_result in list(range(1, 4)):
                print("L'avversario ha schivato, che sfiga!")

            # SE IL DADO E' IN RANGE [4,17] ALLORA L'AVVERSARIO SUBISCE ATTACCO NORMALE
            elif dice_result in list(range(4, 18)):
                damage = int(self.attack()/opponent.defence * 5)
                opponent.life -= damage
                print(f"{opponent.name} ha subito il tuo danno e ha perso {damage} punti vita")
                opponent.print_lifepoints()

            # SE IL DADO E' IN RANGE [18,20] ALLORA L'AVVERSARIO SUBISCE ATTACCO NORMALE + ATTACCO SPECIALE
            elif dice_result in list(range(18, 21)):
                print(f"COLPO CRITICO! Parte l'attacco: {self.special_attack['nome'].upper()}")
                damage = int((self.attack() + self.special_attack['danno'])/opponent.defence * 5)
                opponent.life -= damage
                print(f"{opponent.name} ha subito il tuo danno e ha perso {damage} punti vita")
                opponent.print_lifepoints()

        # Se l'input non è un oggetto con cui posso combattere...
        else:
            print("Invalid INPUT. Opponent must be class Character")

    def is_defeated(self):
        """
        Tells if the player is defeated
        :return:
        """
        return self.life <= 0

    def has_enough_room_in_inventory(self):
        """
        Controlla se il giocatore ha abbastanza spazio nell'inventario
        :return:
        """
        if len(self.inventory) < self.max_inventory_len:
            return True
        else:
            print("Spazio inventario pieno")
            return False

    def print_current_exp(self):
        """
        Mi stampa l'exp attuale
        :return:
        """
        print(f"Exp attuale: {self.exp}/{self.experience_to_next_level}")

    def print_wallet_balance(self):
        """
        Mi stampoa il bilancio delle mie finanze
        :return:
        """
        print(f"Your Current balance is: {self.wallet}")

    def print_current_weapons(self):
        """
        Mi stampo il nome delle armi che ho attualmente nell'inventario
        :return:
        """
        weapon_names = []
        for element in self.inventory:
            weapon_names.append(element.name)
        print("Le tue armi sono")
        print(weapon_names)

        return weapon_names

    def gain_experience(self, experience):
        """
        Aggiunge esperienza a un giocatore
        :param experience: int. esperienza da aggiungere
        :return:
        """
        self.exp += experience
        print(f"{self.name} gained {experience} experience points!")

        if self.exp >= self.experience_to_next_level:
            self.level_up()

    def level_up(self):
        """
        Fa il level up del giocatore
        :return:
        """
        self.level += 1
        self.life += 10
        self.basic_attack += 5
        self.defence += 3
        self.exp -= self.experience_to_next_level
        self.experience_to_next_level *= 2
        print(f"Congratulations! {self.name} leveled up to level {self.level}!")
