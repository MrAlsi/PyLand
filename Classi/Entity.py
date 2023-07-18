# creato da Gianluca 
# classe Entità con gli attributi. casata, livello, vita, attacco base, difesa, attacco speciale

class Entity:
    def __init__(self, lineage, name, level, weapon, life, besic_attack, defence, special_attack):
        self.lineage = lineage
        self.name = name
        self.level = level
        self. weapon = weapon
        self.life = life
        self.besic.attack = besic_attack
        self.defence = defence
        self.special_attack = special_attack
        self.maxlife=200

    # Controllo quando si aggiungono punti vita, affinche non superi il max vita
    def add_lifepoints(self, life_to_add):
        if self.life == self.maxlife:
            print("Life is already full")
        elif self.life + life_to_add > self.maxlife:
            self.life += self.maxlife
        else:
            self.life += life_to_add
        print_lifepoints()

    def print_lifepoints(self):
        print(f"Your current life is {self.life}/{self.maxlife}")

