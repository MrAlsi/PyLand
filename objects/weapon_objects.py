"""

File creato da Federico Piras in data 18.07.2023

Definizione delle armi.


Sword: Spada ------------------> Cavaliere
Bow: Arco.   ------------------> ELfo
Magic wand: Bacchetta magica --> Mago.
Shuriken: shuriken ------------> Ninja.

"""

from Classi.Weapons import Weapon


# canna da pesca disponibile per tutti i personaggi
fishing_pole = Weapon(name="fishing_pole", damage=1, price=20, level=0)

#armi dei mostri
sharp_fangs = Weapon(name="sharp fangs", damage=10, price=10, level=1)
rusty_sword = Weapon(name="rusty sword", damage=11, price=10, level=0)
broken_axe = Weapon(name="broken axe", damage=12, price=12, level=1)
sharp_claws = Weapon(name="sharp claws", damage= 13, price=13, level=2)
big_hammer = Weapon(name="big hammer", damage=14, price=14, level=2)
fangs = Weapon(name="fangs", damage=15, price=15, level=3)
claws = Weapon(name="claws", damage=16, price=16, level=3)
magic_wand = Weapon(name="magic wand", damage=12, price=12, level=1)
dust_bag = Weapon(name="dust bag", damage=10, price=10, level=1)
flower_crown = Weapon(name="flower crown", damage=8, price=8, level=0)
feather_fan = Weapon(name="feather fan", damage=9, price=9, level=0)
crystal_ball = Weapon(name="crystal ball", damage=14, price=14, level=2)
shell_necklace = Weapon(name="shell necklace", damage=7, price=7, level=0)
horn = Weapon(name="horn", damage=17, price=17, level=3)
wings = Weapon(name="wings", damage=18, price=18, level=4)

# Definire armi per Knight
wooden_sword = Weapon(name = "wooden_sword", damage=7, price=10, level=0)
iron_sword = Weapon(name = "iron sword", damage=11, price=40, level=0)
steel_sword = Weapon(name = "steel sword", damage=13, price=50, level=1)
silver_sword = Weapon(name = "silver sword", damage=15, price=60, level=2)
gold_sword = Weapon(name="gold sword", damage=17, price=140, level=3)
diamond_sword = Weapon(name="diamond sword", damage=19, price=160, level=4)
lance = Weapon(name="lance", damage=15, price=100, level=1)
mace = Weapon(name="mace", damage=13, price=80, level=1)
axe = Weapon(name="axe", damage=15, price=90, level=1)
halberd = Weapon(name="halberd", damage=16, price=130, level=1)
dagger = Weapon(name="dagger", damage=8, price=20, level=1)
              
# Definire armi per Elf
staff = Weapon(name="staff", damage=10, price=30, level=0)
elven_dagger = Weapon(name="elven_dagger", damage=8, price=20, level=1)
standard_bow = Weapon(name="standard_bow", damage=10, price=30, level=1)
shortbow = Weapon(name="shortbow", damage=11, price=40, level=0)
longbow = Weapon(name="longbow", damage=12, price=50, level=1)
recurve_bow = Weapon(name="recurve bow", damage=20, price=150, level=1)
composite_bow = Weapon(name="composite bow", damage=14, price=80, level=2)
crossbow = Weapon(name="crossbow", damage=18, price=120, level=2)
rapier = Weapon(name="rapier", damage=13, price=100, level=2)

# Definire armi per Wizard
wood_wand = Weapon(name="wood wand", damage=10, price=20, level=0)
iron_wand = Weapon(name="iron wand", damage=12, price=40, level=1)
silver_wand = Weapon(name="silver wand", damage=14, price=70, level=2)
gold_wand = Weapon(name="gold wand", damage=16, price=120, level=3)
diamond_wand = Weapon(name="diamond wand", damage=18, price=150, level=4)
wood_staff = Weapon(name="wood staff", damage=11, price=30, level=0)
iron_staff = Weapon(name="iron staff", damage=13, price=50, level=1)
silver_staff = Weapon(name="silver staff", damage=15, price=80, level=2)
gold_staff = Weapon(name="gold staff", damage=17, price=130, level=3)
diamond_staff = Weapon(name="diamond staff", damage=19, price=160, level=4)
orb = Weapon(name="orb", damage=17, price=90, level=1)
crystal = Weapon(name="crystal", damage=14, price=75, level=2)
scepter = Weapon(name="scepter", damage=16, price=100, level=3)

# Definire armi per Ninja

katana = Weapon(name="katana", damage=17, price=100, level=2)
kunai = Weapon(name="kunai", damage=12, price=40, level=1)
nunchaku = Weapon(name="nunchaku", damage=13, price=50, level=2)
sai = Weapon(name="sai", damage=14, price=14, level=2)
four_point_shuriken = Weapon(name="four point shuriken", damage=10, price=20, level=1)
six_point_shuriken = Weapon(name="six point shuriken", damage=13, price=40, level=1)
eight_point_shuriken = Weapon(name="eight point shuriken", damage=14, price=60, level=2)
circular_shuriken = Weapon(name="circular shuriken", damage=15, price=80, level=2)
spiked_shuriken = Weapon(name="spiked shuriken", damage=18, price=150, level=3)


# Fai un dizionario di tipo: {"Tipo di PG (quindi Knight, Elf....)": [lista di armi per quel pg]
# Esempio:  {"Knight": [sword, knife, alabarda],
#             "Ninja": [armi del ninja]  }

weapons_dict = {
                "Knight": [wooden_sword, iron_sword, steel_sword, silver_sword, gold_sword, diamond_sword, lance,
                           mace, axe, halberd, dagger, fishing_pole],
                "Elf": [staff, elven_dagger, standard_bow, shortbow, longbow, recurve_bow, composite_bow,
                        crossbow, rapier, fishing_pole],
                "Wizard": [wood_wand, iron_wand, silver_wand, gold_wand, diamond_wand, wood_staff,
                           iron_staff, silver_staff, gold_staff, diamond_staff, orb, crystal, scepter, fishing_pole],
                "Ninja": [katana, kunai, nunchaku, sai, four_point_shuriken, six_point_shuriken, 
                          eight_point_shuriken,circular_shuriken, spiked_shuriken, fishing_pole]
}
