import tkinter as tk
import DB.testDB as db

type_character = ""



# FUNCTION
def showElf():
    attack_var.set("1")
    defense_var.set("2")
    special_attack_var.set("9")
    global type_character
    type_character = "Elf"
    
def showKnight():
    attack_var.set("10")
    defense_var.set("12")
    special_attack_var.set("2")
    global type_character
    type_character = "Knight"

def showWizard(): 
    attack_var.set("15")
    defense_var.set("2")
    special_attack_var.set("19")
    global type_character
    type_character = "Wizard"

def showNinja():
    attack_var.set("7")
    defense_var.set("11")
    special_attack_var.set("4")
    global type_character
    type_character = "Ninja"

def createCharacter():
    name = name_entry.get()
    global type_character
    db.addCharacter(name, type_character)


# SET WINDOWS CONFIG
window = tk.Tk()
window.geometry("700x700")
window.title("PYLAND")
window.resizable(False, False)
window.configure(background="black")

name_entry = tk.Entry(window)
name_entry.pack()




# CHARACTER CHOISE
question_label = tk.Label(window, text="Cosa vuoi essere in questo mondo?")
ElfButton = tk.Button(text="Elfo", command=showElf)
KnightButton = tk.Button(text="Cavaliere", command=showKnight)
WizardButton = tk.Button(text="Mago", command=showWizard)
NinjaButton = tk.Button(text="Ninja", command=showNinja)

attack_var = tk.StringVar()
attack_var.set("-")
attack_label = tk.Label(window, textvariable = attack_var)
defense_var = tk.StringVar()
defense_var.set("-")
defense_label = tk.Label(window, textvariable = defense_var)
special_attack_var = tk.StringVar()
special_attack_var.set("-")
special_attack_label = tk.Label(window, textvariable = special_attack_var)

invio_button = tk.Button(window, text="Invia", command=createCharacter)


question_label.pack()
ElfButton.pack()
KnightButton.pack()
WizardButton.pack()
NinjaButton.pack()
attack_label.pack()
defense_label.pack()
special_attack_label.pack()
invio_button.pack()

    

#Run window
if __name__ == "__main__":
    window.mainloop()
