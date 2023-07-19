import game
import tkinter as tk
from Classi.Shops import Tavern
from Classi.Shops import Smith


def fattiNaPera():
    player.life -= 30
    print("Dose")
    print(player.life)
    life.set(player.life)

def sleep():
    bar.rent_a_room(player)
    print("Dormi")
    print(player.life)
    life.set(player.life)

def populate_inventary():
    for weapon in player.inventory:
        inventario.insert(tk.END, weapon.name)

def populate_shop():
    available_weapons = fabbro.show_available_weapons(player)
    for weapon in available_weapons:
        available_weapons_listBox.insert(tk.END, weapon)

def buy_weapon(event):
    selected_item = available_weapons_listBox.get(available_weapons_listBox.curselection())
    fabbro.buy_new_weapon(player, selected_item)
    populate_inventary()
    print("mie armi", player.inventory)

    
nome = "Mammastomale"
player = game.getCharacter(nome)

# SET WINDOWS CONFIG
window = tk.Tk()
window.geometry("1000x1000")
window.title("PYLAND")
window.resizable(False, False)
window.configure(background="black")

#Carica immagine del giocatore
#Nome utente
name_label = tk.Label(window, text=player.name)
name_label.pack()

#Life
life = tk.StringVar()
life.set(player.life)
life_label = tk.Label(window, textvariable=life)
life_label.pack()

#Exp
exp = tk.StringVar()
exp.set(player.exp)
exp_label = tk.Label(window, textvariable=exp)
exp_label.pack()

#Statistiche
att_bs = "Attacco:   " + str(player.basic_attack)
stats_att_bs = tk.Label(window, text=att_bs)
stats_att_bs.pack()

#Invetario
inventario = tk.Listbox(window)
populate_inventary()
inventario.pack()

##Prova
#pera
prova = tk.Button(window, text="Fatti una pera", command=fattiNaPera)
prova.pack()

#Locanda
bar = Tavern("Da Boe")
locanda_button = tk.Button(window, text=bar.name, command=sleep)
locanda_button.pack()

#Fabbro
fabbro = Smith("Fabbro")
available_weapons_listBox = tk.Listbox(window)
populate_shop()

# Associazione dell'azione all'evento di clic su un elemento
available_weapons_listBox.bind('<<ListboxSelect>>', buy_weapon)

# Aggiunta del available_weapons_listBox alla finestra
available_weapons_listBox.pack()



#Run window
if __name__ == "__main__":
    window.mainloop()
