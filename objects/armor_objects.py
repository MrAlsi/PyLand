"""

File creato da Gianluca

Definizione delle armature.


"""


from Classi.Armor import Armor


# Definire armatura per Knight
leather_chestplate = Armor(name="leather chestplate", armor_defense = 1, price = 10)
iron_chestplate = Armor(name = "iron chestplate", armor_defense = 6, price = 60)
steel_chestplate = Armor(name = "steel chestplate", armor_defense = 7, price = 70)
silver_chestplate = Armor(name = "silver chestplate", armor_defense = 8, price = 80)
gold_chestplate = Armor(name = "gold chestplate", armor_defense = 9, price = 90)
diamond_chestplate = Armor(name = "diamond chestplate", armor_defense = 15, price = 100)
helmet = Armor(name = "helmet", armor_defense = 2, price = 10)
shield = Armor(name = "shield", armor_defense = 3, price = 20)
chainmail = Armor(name = "chainmail", armor_defense = 5, price = 40)
plate_armor = Armor(name = "plate armor", armor_defense = 6, price = 50)

# Definire armatura per Elf
hood = Armor(name = "hood", armor_defense = 1, price = 5)
cloak = Armor(name = "cloak", armor_defense = 2, price = 10)
leather_armor = Armor(name = "leather armor", armor_defense = 3, price = 15)
elven_armor = Armor(name = "elven armor", armor_defense = 4, price = 20)
silk_robe = Armor(name = "silk robe", armor_defense = 5, price = 10)
enchanted_robe = Armor(name = "enchanted robe", armor_defense = 6, price = 40)


# Definire armatura per Wizard
hat = Armor(name = "hat", armor_defense = 1, price = 5)
cape = Armor(name = "cape", armor_defense = 2, price = 10)
robe = Armor(name = "robe", armor_defense = 3, price = 15)
magic_armor = Armor(name = "magic armor", armor_defense = 4, price = 20)
ring = Armor(name = "ring", armor_defense = 5, price = 5)
amulet = Armor(name = "amulet", armor_defense = 6, price = 10)


# Definire armatura per Ninja
mask = Armor(name = "mask", armor_defense = 1, price = 5)
ninja_suit = Armor(name = "ninja suit", armor_defense = 3, price = 15)
gloves = Armor(name = "gloves", armor_defense = 5, price = 5)
boots = Armor(name = "boots", armor_defense = 6, price = 5)
belt = Armor(name = "belt", armor_defense = 7, price = 5)
bandana = Armor(name = "bandana", armor_defense = 8, price = 100)
chainmail = Armor(name = "chainmail", armor_defense = 4, price = 20)
vest = Armor(name = "vest", armor_defense = 2, price = 10)
bracer = Armor(name = "bracer", armor_defense = 1, price = 5)
necklace = Armor(name = "necklace", armor_defense = 1, price = 5)


armor_dict = {"Knight": [leather_chestplate, iron_chestplate, steel_chestplate, silver_chestplate, gold_chestplate,
                          diamond_chestplate, helmet, shield, chainmail, plate_armor],
                "Elf": [hood, cloak, leather_armor, elven_armor, silk_robe, enchanted_robe],
                "Wizard": [hat, cape, robe, magic_armor, ring, amulet],
                "Ninja": [mask, ninja_suit, gloves, boots, belt, bandana, chainmail, vest, bracer, necklace]
                }