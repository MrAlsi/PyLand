from Classi.Wizard import Wizard
from Classi.Shops import Tavern, Smith
from Classi.weapon_objects import weapons_dict
#
#
# wiz = Wizard(lineage="Buoni",
#              name="Wiz",
#              level=0,
#              weapon=None,
#              life=200,
#              basic_attack=10,
#              defence=5,
#              special_attack=15,
#              gender='m',
#              exp=0,
#              wallet=2000,
#              inventory=[])
#
# wiz.print_wallet_balance()
#
# tavern = Tavern(name="Taverna da Boe")
# smith = Smith(name="Mario")
#
# # # Compro arma
# # list_of_available_weapons = smith.show_available_weapons(wiz)
# #
# # # Chiedo l'arma
# # arma_name = input("Che arma vuoi? ")
# # while arma_name not in list_of_available_weapons:
# #     arma_name = input("Che arma vuoi? ")
# #
# # smith.buy_new_weapon(wiz, arma_name)
#
# # Compro arma
# # smith.buy_new_weapon(wiz)


pg1 = Wizard(lineage="Buoni",
             name="Silente",
             level=0,
             weapon=None,
             life=200,
             basic_attack=10,
             defence=5,
             special_attack=15,
             gender='m',
             exp=0,
             wallet=2000,
             inventory=[])

pg2 = Wizard(lineage="Buoni",
             name="Wizzzzzard",
             level=0,
             weapon=None,
             life=200,
             basic_attack=10,
             defence=5,
             special_attack=15,
             gender='m',
             exp=0,
             wallet=2000,
             inventory=[])

while pg1.life > 0 and pg2.life > 0:
    print("--------------------------------------")
    pg1.fight(pg2)
    if pg2.life > 0:
        pg2.fight(pg1)