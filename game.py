import time
import os
from objects.shops_objects import smith, tavern
from objects.zone_objects import lago, montagna
from objects.missions_objects import mission_easy, mission_medium, mission_hard
from Classi.Enemy import easy_monsters, medium_monsters, strong_monsters
import random
import DB.CRUD as db
import sys


def clear_console():
    sys.stdout.write("\033[H\033[J")


def select_mission(player_level):
    """
    Seleziona una missione di livello facile medio o difficile in base al livello del giocatore
    :param player_level:
    :return:
    """
    if player_level < 3:
        return mission_easy, random.choice(easy_monsters)
    elif 3 <= player_level < 6:
        return mission_medium, random.choice(medium_monsters)
    else:
        return mission_hard, random.choice(strong_monsters)


missions_list = [mission_easy, mission_medium, mission_hard]


def main_loop(player):
    os.system('clear')
    print("Welcome to PyLand!")
    while not player.is_defeated():
        print("1. Esplora Locations")
        print("2. Esplora missioni")
        print("3. Fai una missione (combatti con un mostro)")
        print("4. Vai dal fabbro")
        print("5. Vai in locanda")
        print("6. Vai al lago")
        print("7. Vai in montagna")
        print("8. Visualizza stato giocatore")
        print("9. Esci\n")

        choice = input("Cosa vuoi fare?")


        if choice == '1':
            print("Ci sono quattro luoghi che puoi visitare! Su quale vorresti avere maggiori info?")
            print("1. Fabbro")
            print("2. Locanda")
            print("3. Lago")
            print("4. Montagna")
            print("5. Premi un tasto a caso per tornare in città")

            rimani = True
            while rimani:

                location_choice = int(input("Entra il numero della location che vuoi visitare: "))

                if location_choice == 1:
                    print(f"Ciao, sono il fabbro e mi chiamo {smith.name}")
                    smith.print_description()
                    print('\n')

                elif location_choice == 2:
                    print(f"Benvenuto da {tavern.name}")
                    tavern.print_description()
                    print('\n')

                elif location_choice == 3:
                    print(f"Benvenuto al lago {lago.name}")
                    lago.print_description()
                    print('\n')

                elif location_choice == 4:
                    print(f"Benvenuto alla montagna {montagna.name}")
                    montagna.print_description()
                    print('\n')

                else:
                    rimani = False

        elif choice == '2':
            for mission in missions_list:
                mission.print_description()

        elif choice == '3':
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
                time.sleep(2)

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

        elif choice == '4':
            print("Benvenuto dal FABBRO")
            print("Azioni disponibili: ")
            print("1. Acquista arma")
            print("2. Vendi arma")
            print("3. Upgrade Arma")
            print("4. Visualizza le armi che hai nell'inventario")
            print("5. Saluta il fabbro")

            rimani = True
            while rimani:
                print("Azioni disponibili: ")
                print("1. Acquista arma")
                print("2. Vendi arma")
                print("3. Upgrade Arma")
                print("4. Visualizza le armi che hai nell'inventario")
                print("5. Saluta il fabbro")

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

                elif choice_ == 5:
                    rimani = False

        elif choice == '5':
            print("Benvenuto Nella Locanda!")
            print("Azioni disponibili: ")
            print("1. Bevi una birra")
            print("2. Affitta una camera")
            print("3. Esci dalla locanda")

            rimani = True
            while rimani:
                choice_ = int(input("Cosa vuoi fare?: "))

                if choice_ == 1:
                    print("Goditi la tua birra fresca!")
                    tavern.drink_a_beer(player)

                elif choice_ == 2:
                    print("Ti vedo stanco, buon riposo!")
                    tavern.rent_a_room(player)

                elif choice_ == 3:
                    rimani = False

        elif choice == '6':
            rimani = True
            while rimani:
                print(f"Benvenuto al lago {lago.name.upper()}")
                print("1. Pesca")
                print("2. Riposa su un'amaca") # da implementare
                print("3. Torna in città")
                choice_ = int(input("Cosa vuoi fare? "))

                if choice_ == 1:
                    lago.pesca(player)

                elif choice_ == 2:
                    lago.sleep_on_hammock(player)

                elif choice_ == 3:
                    rimani = False

        elif choice == '7':
            print(f"Benvenuto alla montagna {montagna.name.upper()}")
            montagna.print_description()

            rimani = True
            while rimani:
                print("1. Riposa sotto le stelle")
                print("2. Scala la montagna")
                print("3. Torna in città")

                choice_ = int(input("Cosa vuoi fare? "))
                if choice_ == 1:
                    montagna.sleep_under_the_stars()

                elif choice_ == 2:
                    rimani = montagna.ask_entrance(player)

                elif choice_ == 3:
                    rimani = False

        elif choice == '8':
            player.print_lifepoints()
            player.print_wallet_balance()
            player.print_current_exp()
            player.print_current_weapons()

        elif choice == '9':
            db.updateCharacter(player)
            sys.exit()
            break

        else:
            print('Opzione invalida....')

        input("premi invio per continuare a giocare")
