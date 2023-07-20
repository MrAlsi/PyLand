from Classi.Wizard import Wizard
from Classi.shops_objects import smith, tavern
from Classi.weapon_objects import weapons_dict
from Classi.missions_objects import mission_easy, mission_medium, mission_hard
from Classi.Enemy import easy_monsters, medium_monsters, strong_monsters
import random


def select_mission(player_level):
    if player_level < 3:
        return mission_easy, random.choice(easy_monsters)
    elif 3 <= player_level < 6:
        return mission_medium, random.choice(medium_monsters)
    else:
        return mission_hard, random.choice(strong_monsters)
#
# def combat(player, monster):
#     while not player.is_defeated() and not monster.is_defeated():
#         player_damage = player.attack()
#         monster_damage = monster.attack()
#
#         monster.take_damage(player_damage)
#         player.take_damage(monster_damage)
#
#         print(f"{player.name} attacks {monster.name} and deals {player_damage} damage.")
#         print(f"{monster.name} attacks {player.name} and deals {monster_damage} damage.")
#
#     if player.is_defeated():
#         print("You have been defeated. Game Over!")
#         return 0  # Il giocatore non guadagna esperienza se viene sconfitto
#     elif monster.is_defeated():
#         print(f"You have defeated {monster.name}! You win!")
#         return 1

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
             life=2000,
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
#
# while pg1.life > 0 and pg2.life > 0:
#     print("--------------------------------------")
#     pg1.fight(pg2)
#     if pg2.life > 0:
#         pg2.fight(pg1)

missions_list = [mission_easy, mission_medium, mission_hard]


def main_loop(player):
    print("Welcome to PyLand!")
    while not player.is_defeated():
        print("1. Esplora Locations")
        print("2. Esplora missioni")
        print("3. Fai una missione (combatti con un mostro)")
        print("4. Vai dal fabbro")
        print("5. Vai in locanda")
        print("6. Visualizza stato giocatore")
        print("7. Esci")

        choice = int(input("Cosa vuoi fare?"))

        if choice == 1:
            print("Ci sono due luoghi che puoi visitare! Su quale vorresti avere maggiori info?")
            print("1. Fabbro")
            print("2. Locanda")

            location_choice = int(input("Entra il numero della location che vuoi visitare: "))

            if location_choice == 1:
                print(f"Ciao, sono il fabbro e mi chiamo {smith.name}")
                smith.print_description()

            elif location_choice == 2:
                print(f"Benvenuto da {tavern.name}")
                tavern.print_description()

        elif choice == 2:
            for mission in missions_list:
                mission.print_description()

        elif choice == 3:
            mission, monster = select_mission(player.level)
            mission.print_description()
            monster.print_info()

            # Chiedi di equipaggiare
            player.ask_to_equip()

            m = monster
            # Combatti
            while not player.is_defeated() and not m.is_defeated():
                print('----------------------')
                player.fight(m)
                if m.life > 0:
                    m.fight(player)

            # result = combat(player, monster)
            if m.is_defeated():
                m.life = m.vita_iniziale
                player.gain_experience(mission.exp_reward)
                player.wallet += mission.money_reward
                print(f"You have defeated {m.name}! You win!")

                # Disequipaggia l'arma
                player.disequip_weapon()
            else:
                print("You have been defeated. Game Over!")

        elif choice == 4:
            print("Benvenuto dal FABBRO")
            print("Azioni disponibili: ")
            print("1. Acquista arma")
            print("2. Vendi arma")
            print("3. Upgrade Arma")
            print("4. Visualizza le armi che hai nell'inventario")

            choice_ = int(input("Cosa vuoi fare? "))

            if choice_ == 1:
                print("Hai scelto di comprare un'arma")
                smith.buy_new_weapon(player)

            elif choice_ == 2:
                print("Hai scelto di vendere un'arma")
                smith.sell_weapon(player)

            elif choice_ == 3:
                print("Hai scelto di fare upgrade di un'arma")
                smith.upgrade_weapon(player)

            elif choice_ == 4:
                print("Hai scelto di visualizzare le armi che hai nell'inventario")
                player.print_current_weapons()

        elif choice == 5:
            print("Benvenuto Nella Locanda!")
            print("Azioni disponibili: ")
            print("1. Bevi una birra")
            print("2. Affitta una camera")

            choice_ = int(input("Cosa vuoi fare?: "))

            if choice_ == 1:
                print("Goditi la tua birra fresca!")
                tavern.drink_a_beer(player)

            elif choice_ == 2:
                print("Ti vedo stanco, buon riposo!")
                tavern.rent_a_room(player)

        elif choice == 6:
            player.print_lifepoints()
            player.print_wallet_balance()
            player.print_current_exp()

        elif choice == 7:
            break

        input("premi invio per continuare a giocare")


# Esegui il main loop del gioco
#main_loop(pg1)