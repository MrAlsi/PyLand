import game
import tkinter as tk
from Classi.Shops import Tavern

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

##Prova
#pera
prova = tk.Button(window, text="Fatti una pera", command=fattiNaPera)
prova.pack()
#Locanda
bar = Tavern("Da Boe")
locanda_button = tk.Button(window, text=bar.name, command=sleep)
locanda_button.pack()

#Fabbro




#Run window
if __name__ == "__main__":
    window.mainloop()
