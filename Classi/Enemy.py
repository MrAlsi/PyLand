# creato da Gianluca 
# Sottoclasse di Entità chiamata Nemico con attributi: nome e dro

import Entity
from Character import Character


class Enemy(Entity):
    def __init__(self, lineage, name, level, weapon, life, basic_attack, defence, special_attack, drop):
        super().__init__(lineage, name, level, weapon, life, basic_attack, defence, special_attack)
        self.drop = drop

    # Guardaci in data 19.07

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

slime = Enemy("Enemy","Slime", 1, None, 20, 10, 10, None, 5)
rat = Enemy("Enemy","Rat", 1, "Sharp fangs", 15, 10, 10, "Poisonous bite", 5)
goblin = Enemy("Enemy","Goblin", 2, "Rusty sword", 25, 15, 15, "Low blow", 10)
skeleton = Enemy("Enemy","Skeleton", 3, "Broken axe", 35, 20, 20, "Flying bones", 15)
ghost = Enemy("Enemy","Ghost", 4, None, 50, 25, 25, "Scary scream", 15)
wolf = Enemy("Enemy","Wolf", 5, "Sharp claws", 30, 15, 15, "Howl", 10)
zombie = Enemy("Enemy","Zombie", 6, "Rotten hands", 40, 20, 20, "Infection", 15)
orc = Enemy("Enemy","Orc", 7, "Big hammer", 50, 25, 25, "Smash", 25)
vampire = Enemy("Enemy","Vampire", 8, "Fangs", 12, 5, 5, "Blood drain", 50)
dragon = Enemy("Enemy","Dragon", 10, "Claws", 75, 30, 30, "Fire breath", 75)
hydra = Enemy("Enemy","Hydra", 9, "Claws", 90, 35, 35, "Acid spit", 100)

fairy = Enemy("Friendly","Fairy", 1, "Magic wand", 10, 5, 5, "Heal", 5)
pixie = Enemy("Friendly","Pixie", 2, "Dust bag", 15, 10, 10, "Invisibility", 10)
nymph = Enemy("Friendly","Nymph", 3, "Flower crown", 20, 15, 15, "Nature’s blessing", 15)
sylph = Enemy("Friendly","Sylph", 4, "Feather fan", 25, 20, 20, "Wind blast", 20)
sprite = Enemy("Friendly","Sprite", 5, "Crystal ball", 30, 25, 25, "Illusion", 25)
mermaid = Enemy("Friendly","Mermaid", 3, "Shell necklace", 20, 15, 15, "Water splash", 15)
unicorn = Enemy("Friendly","Unicorn", 4, "Horn", 25, 20, 20, "Rainbow beam", 20)
phoenix = Enemy("Friendly","Phoenix", 5, "Claws", 30, 25, 25, "Fire burst", 25)
angel = Enemy("Friendly","Angel", 6, "Wings", 35, 30, 30, "Light strike", 30)
