"""

File creato da Federico Piras in data 18.07.2023

Definizione delle armi.


Sword: Spada ------------------> Cavaliere
Bow: Arco.   ------------------> ELfo
Magic wand: Bacchetta magica --> Mago.
Shuriken: shuriken ------------> Ninja.

"""

from Weapons import Weapon

# Definire armi per Knight
sword = Weapon(name="sward", damage=11, price=10, level=0)
lance = Weapon(name="lance", damage=15, price=15, level=1)
mace = Weapon(name="mace", damage=13, price=13, level=1)
axe = Weapon(name="axe", damage=12, price=12, level=1)
bow = Weapon(name="bow", damage=10, price=10, level=1)
dagger = Weapon(name="dagger", damage=8, price=8, level=1)

# Definire armi per Elf
bow = Weapon(name="bow", damage=5, price=5, level=0)

# Definire armi per Wizard
magic_wand = Weapon(name="magic_wand", damage=12, price=7, level=0)

# Definire armi per Ninja
shuriken = Weapon(name="shuriken", damage=9, price=8, level=0)


# Fai un dizionario di tipo: {"Tipo di PG (quindi Knight, Elf....)": [lista di armi per quel pg]
# Esempio:  {"Knight": [sword, knife, alabarda],
#             "Ninja": [armi del ninja]  }

weapons_dict = {}

