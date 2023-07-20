# creato da Gianluca 
# Sottoclasse di Entità chiamata Nemico con attributi: nome e dro

from Classi.Entity import Entity
from Classi.Character import Character
import random


class Enemy(Entity):
    def __init__(self, lineage, name, level, weapon, life, basic_attack, defence, special_attack, drop):
        super().__init__(lineage, name, level, weapon, life, basic_attack, defence, special_attack)
        self.drop = drop

    # Guardaci in data 19.07

    def attack(self):
        return self.basic_attack

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"level: {self.level}")

    def is_defeated(self):
        return self.life <= 0

    # def lose_lifepoints(self, attacker):
    #     if isinstance(attacker, Character):
    #         if attacker.is_equipped():
    #             damage = attacker.basic_damage + attacker.weapon.damage
    #         else:
    #             damage = attacker.basic_damage
    #
    #     if self.life - damage > 0:
    #         self.life -= damage
    #     else:
    #         print("GAME OVER")

    def fight(self, opponent):
        """
        Implements a fight between two PG.
        :param opponent: The opponent to fight. Must be an instance of class Character
        :return:
        """
        if isinstance(opponent, Entity):
            dice_result = random.choice(range(1, 21))
            print(f"{self.name} STA ATTACCANDO {opponent.name}")
            if dice_result in list(range(1, 4)):
                print("L'avversario ha schivato, che sfiga!")
            elif dice_result in list(range(4, 18)):
                damage = int(self.attack()/opponent.defence * 5)
                opponent.life -= damage
                print(f"{opponent.name} ha subito il tuo danno e ha perso {damage} punti vita")
                opponent.print_lifepoints()
            elif dice_result in list(range(18, 21)):
                print(f"COLPO CRITICO! Parte l'attacco: {self.special_attack['name'].upper()}")
                damage = int((self.attack() + self.special_attack['attack'])/opponent.defence * 5)
                opponent.life -= damage
                print(f"{opponent.name} ha subito il tuo danno e ha perso {damage} punti vita")
                opponent.print_lifepoints()


slime = Enemy("Enemy","Slime", 1, None, 20, 10, 10, None, 5)
rat = Enemy("Enemy","Rat", 1, "Sharp fangs", 15, 10, 10, {"name": "Poisonous bite", "attack": 6}, 5)
goblin = Enemy("Enemy","Goblin", 2, "Rusty sword", 25, 15, 15, {"name": "Low blow", "attack": 6}, 10)
skeleton = Enemy("Enemy","Skeleton", 3, "Broken axe", 35, 20, 20, {"name": "Flying bones", "attack": 6}, 15)
ghost = Enemy("Enemy","Ghost", 4, None, 50, 25, 25, {"name": "Scary scream", "attack": 6}, 15)
wolf = Enemy("Enemy","Wolf", 5, "Sharp claws", 30, 15, 15, {"name": "Howl", "attack": 6}, 10)
zombie = Enemy("Enemy","Zombie", 6, "Rotten hands", 40, 20, 20, {"name": "Infection", "attack": 6}, 15)
orc = Enemy("Enemy","Orc", 7, "Big hammer", 50, 25, 25, {"name":  "Smash", "attack": 6}, 25)
vampire = Enemy("Enemy","Vampire", 8, "Fangs", 12, 5, 5, {"name": "Blood drain", "attack": 6}, 50)
dragon = Enemy("Enemy","Dragon", 10, "Claws", 75, 30, 30, {"name": "Fire breath", "attack": 6}, 75)
hydra = Enemy("Enemy","Hydra", 9, "Claws", 90, 35, 35, {"name": "Acid spit", "attack": 6}, 100)

easy_monsters = [slime, rat, goblin, wolf, vampire]
medium_monsters = [skeleton, ghost, zombie, orc]
strong_monsters = [dragon, hydra]

fairy = Enemy("Friendly","Fairy", 1, "Magic wand", 10, 5, 5, "Heal", 5)
pixie = Enemy("Friendly","Pixie", 2, "Dust bag", 15, 10, 10, "Invisibility", 10)
nymph = Enemy("Friendly","Nymph", 3, "Flower crown", 20, 15, 15, "Nature’s blessing", 15)
sylph = Enemy("Friendly","Sylph", 4, "Feather fan", 25, 20, 20, "Wind blast", 20)
sprite = Enemy("Friendly","Sprite", 5, "Crystal ball", 30, 25, 25, "Illusion", 25)
mermaid = Enemy("Friendly","Mermaid", 3, "Shell necklace", 20, 15, 15, "Water splash", 15)
unicorn = Enemy("Friendly","Unicorn", 4, "Horn", 25, 20, 20, "Rainbow beam", 20)
phoenix = Enemy("Friendly","Phoenix", 5, "Claws", 30, 25, 25, "Fire burst", 25)
angel = Enemy("Friendly","Angel", 6, "Wings", 35, 30, 30, "Light strike", 30)
