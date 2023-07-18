"""

File creato da Federico Piras in data 18.07.2023

Definizione della classe negozio e dei singoli negozi

"""


class Shop:

    def __init__(self, attribute):
        self.attribute = attribute


class Smith(Shop):

    def __init__(self, attribute1):
        self.attribute1 = attribute1


class Tavern(Shop):

    def __init__(self, attribute2):
        self.attribute2 = attribute2