import time
import DB.CRUD as db
import CreatePlayer as cp
import os
import prova as game
import game as gc

menu = True

def dialog(text, pause=1):
    '''
    Method for make the text look like a dialogue
    '''
    delay = pause / len(text)
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(delay)
    print()


def selectName():
    '''
    Ask name of character
    '''
    finish = False
    dialog("Innanzitutto serve un nome, il nome deve essere unico in tutto il mondo quindi è possibile che non sia disponibile il nome che desideri, però possiamo provare\n", 2.5)
    while(not finish):
        name = input()
        account = db.getCharacter(name)
        if account == None:
            dialog("Ottimo, nel dubbio anche Porchetta68 era libero")
            return name
        else:
            print(account)
            dialog(f"Mi dispiace... C'è gia un vecchio {account['type']} che si chiama cosi, riprova")



def selectLineage(name):
    '''
    Ask the lineage of character
    '''
    dialog(f"Ok {name}, in questo regno ci sono due schieramenti:i Buoni, la Luce oppure i Cattivi, il Buio")

    time.sleep(0.5)
    dialog("tu cosa vuoi essere?")
    while(True):
        lineage = input("1) Buoni\n2) Cattivi\n")
        if lineage == "1":
            return "Good"
        elif lineage == "2":
            return "Evil"
        else:
            dialog("Simpatico...")
            time.sleep(1)
            dialog("Metterò coglione nel DB")
            return "Coglione"
        

def selectGender():
    '''
    Ask the gender of character, in 2023 is very difficult
    '''
    while(True):
        dialog("I programmatori vogliono sapere il sesso, non so a cosa serva per questo gioco però devi inserirlo", 2)
        gender = input("Cosa sei?\n1) Maschio\n2) Femmina\n3)Cavallo\n")
        dialog("Ovviamente noi ti crediamo, non è mai successo che in questo tipo di gioco gente menta su queste cose...", 2)
        if gender == 1:
            return "M"
        elif gender == 2:
            return "F"
        else:
            return "CAVALLO"


def selectCharacter():
    '''
    Ask the type of character
    '''
    finish = False
    dialog("Allora, qua puoi essere 4 tipi di personaggio: Cavaliere, Mago, Elfo o Ninja (si puoi essere un ninja)", 2)
    dialog("Queste sono le statistiche base dei tipi dei personaggi",1)
    #stampa statistiche
    while(not finish):
        tipo = input("Cosa vuoi essere?\n1) Cavaliere\n2) Mago\n3) Elfo\n4) Ninja\n")
        if tipo == "1":
            return "Knight"
        elif tipo == "2":
            return "Wizard"
        elif tipo == "3":
            return "Elf"
        elif tipo == "4":
            return "Ninja"
        else:
            dialog("Fammi indovinare...")
            time.sleep(1) 
            dialog("Sei quello simpatico alle feste te...")


#While for menu
while(menu):
    print("     ## BENVENUTO IN PYLAND! ## \nIL MONDO ONLINE DI CUI NON AVEVAMO BISOGNO\n")
    choice = input("Hai già un personaggio? Premi 1 per accedere\nAltrimenti premi 2 per creare un personaggio\n")
    if choice == "1": #LOGIN
        login = True
        while(login):
            name = input("\nCome si chiama il tuo personaggio?  ")
            #Search in DB
            player = db.getCharacter(name)
            if player != None:
                print("player",player)
                game.main_loop(gc.getCharacter(name))
            else:
                print("Personaggio non trovato")


    elif choice == "2": #CREATION OF CHARACTER
        name = selectName()
        lineage = selectLineage(name)
        gender = selectGender()
        tipo = selectCharacter()
        player = ""
        if tipo == "Knight":
            player = db.addCharacter(tipo, cp.createKnight(name, lineage, gender))
        elif tipo == "Wizard":
            player = db.addCharacter(tipo, cp.createWizard(name, lineage, gender))
        elif tipo == "Elf":
            player = db.addCharacter(tipo, cp.createElf(name, lineage, gender))
        elif tipo == "Ninja":
            player = db.addCharacter(tipo, cp.createNinja(name, lineage, gender))

        dialog("Super!! allora iniziamo a giocare")
        os.system('cls')
        game.main_loop(gc.getCharacter(name))

    else: #INVALID INPUT
        dialog("Bro...")
        time.sleep(1)
        dialog("partiamo già male")
        time.sleep(1)
        dialog("Riproviamo")
        time.sleep(1)
        