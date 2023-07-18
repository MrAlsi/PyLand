def add_vita(life, life_to_add):
    vita_massima = 200
    if life == vita_massima:
        print("Vita piena")
    elif life + life_to_add > vita_massima:
        life = 200
    else:
        life += life_to_add

    return life


class Tavern:

    def __init__(self, name):
        self.name = name
        self.__price_per_night = 10

tavern = Tavern('Bella taverna')


def print_lifepoint(param):
    print(param)


def prova(variabile):
    return True if variabile > 200 else False



class Padre:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome


class Figlio(Padre):
    def __init__(self, age):
        super().__init__()
        self.age = age


import random

class Personaggio:

    def __init__(self, attacco, vita, difesa):
        self.attacco = attacco
        self.vita = vita
        self.difesa = difesa

    def get_life(self):
        print(f"Vita rimasta: {self.vita}")

    def attack(self):
        return self.attacco

    def combat(self, avversario):
        schivata = random.choice(range(1, 11))
        if schivata == 1:
            print("L'avversario ha schivato, che sfiga!")
        else:
            danno = int(self.attack()/avversario.difesa * 5)
            avversario.vita -= danno
            print(f"L'avversario ha subito il tuo danno e ha perso {danno} punti vita")
            avversario.get_life()



pg1 = Personaggio(attacco=10, vita=100, difesa=5)
pg2 = Personaggio(attacco=7, vita=80, difesa=3)

pg1.combat(pg2)

