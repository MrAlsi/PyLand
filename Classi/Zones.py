"""
File creato da Federico Piras in data 18.07.2023

Definizione di una classe zona

"""
import random
import sys
import os
import time
from Classi.ASCII_art import notte_stellata, vittoria
from Classi.Enemy import PyKing


def loading_animation(my_time, name):
    """
    Stampa l'animazione mentre aspetto che pesca
    :param my_time:
    :return:
    """
    animation = "|/-\\"
    for i in range(my_time):
        time.sleep(0.2)  # Aggiorna l'animazione ogni 0.1 secondo
        sys.stdout.write(f"\r {name} sta pescando... {animation[i % len(animation)]} ")
        sys.stdout.flush()


class Zone:

    def __init__(self, name, descrizione):
        self.name = name
        self.descrizione = descrizione

    def get_zone_name(self):
        return self.name

    def print_description(self):
        """
        Stampa la descrizione
        :return:
        """
        print(self.descrizione)



class Lake(Zone):

    def __init__(self, name, descrizione, pesci):
        super().__init__(name, descrizione)
        self.descrizione = descrizione
        self.pesci = pesci

    def print_pesci(self):
        """
        Stampa i pesci che hai nel lago
        :return:
        """
        print(f"I pesci che puoi pescare sono: {self.pesci}")


    def pesca(self, character):
        """
        Permette al giocatore di pescare un pesce dal lago con una probabilità del 10% di successo
        e aumenta la vita del giocatore se pesca con successo.
        :param character: Il giocatore che sta pescando
        :return: Il pesce pescato se ha avuto successo, None altrimenti
        """
        continua_pesca = 1
        # Controlliamo se ho una canna da pesca...
        if character.has_fishing_pole():

            while continua_pesca:
                # print(f"{character.name} sta pescando...")
                loading_animation(50, character.name)
                # time.sleep(10)  # Aspetta 10 secondi per simulare il tempo di pesca

                # Stampa della barretta di progresso

                if random.random() < 0.25:  # Probabilità del 10% di successo
                    pesce_pescato = self.pesci
                    print(f"\n{character.name} ha pescato un {pesce_pescato}!")
                    character.add_lifepoints(10)  # Aggiunge 10 punti vita al giocatore
                else:
                    print(f"\n{character.name}, purtroppo non hai pescato nulla.")

                continua_pesca = int(input("Vuoi continuare a pescare? 1 sì, 0 no"))
        else:
            print("Non hai la canna da pesca. Valla a comprare dal Fabbro")


class Mountain(Zone):

    def __init__(self, name, descrizione):
        super().__init__(name, descrizione)
        self.nome = name
        self.descrizione = descrizione
        self.tentativi = 3

    def ask_entrance(self, character):
        if self.tentativi != 0:
            print("Non puoi entrare")
            self.tentativi -= 1
            return True
        else:
            print("Compare PyKing! Combatti contro PyKing!")
            # Combatti
            while not character.is_defeated() and not PyKing.is_defeated():
                print('----------------------')
                character.fight(PyKing)
                if PyKing.life > 0:
                    PyKing.fight(character)
                elif PyKing <= 0:
                    #gestisci vittoria
                    win(character.name)
                elif character.life <= 0:
                    return False
                time.sleep(2)

    def sleep_under_the_stars(self):
        """
        Fa una bella dormita sotto le stelle
        :return:
        """

        for riga in notte_stellata:
            print(riga)
            time.sleep(1.1)


def win(name):
    os.system("cls")
    time.sleep(1.5)
    print("** squillo di trombre **")
    time.sleep(1.5)
    for line in vittoria:
        print(line)
        time.sleep(0.5)
    time.sleep(1.5)
    print(f"ORA PYLAND HA FINALMENTE UN NUOVO RE E SEI TU {name}!! CONGRATULAZIONI")
    sys.exit()
