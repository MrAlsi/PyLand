# creato da Gianluca 
# Sottoclasse di Entità chiamata Nemico con attributi: nome e dro

import Entity
from Character import Character


class Enemy(Entity):
    def __init__(self, lineage, name, level, weapon, life, basic_attack, defence, special_attack, drop):
        super().__init__(lineage, name, level, weapon, life, basic_attack, defence, special_attack)
        self.drop = drop

    def lose_lifepoints(self, attacker):
        if isinstance(attacker, Character):
            if attacker.is_equipped():
                damage = attacker.basic_damage + attacker.weapon.damage
            else:
                damage = attacker.basic_damage

        if self.life - damage > 0:
            self.life -= damage
        else:
            print("GAME OVER")

slime = Enemy("Oscuro","Slime", 1, None, 2, 1, 1, None, 5)
zombi = Enemy("Zombi",10)
lupo = Enemy("Lupo",15)
goblin = Enemy("Goblin",20)
orco = Enemy("Orco",30)
ghoul = Enemy("ghoul",35)
drago = Enemy("Orco",50)