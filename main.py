import tkinter as tk
import DB.CRUD as db
from PIL import ImageTk, Image
from Classi.Wizard import Wizard as newWizard
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
    db.addCharacter(name, type_character, newWizard("B", name, 0, None, 100, 10, 5, 15, "Maschio", 0, 10, []))


# SET WINDOWS CONFIG
window = tk.Tk()
window.geometry("1000x1000")
window.title("PYLAND")
window.resizable(False, False)
window.configure(background="black")

name_entry = tk.Entry(window)
name_entry.pack()


image_path_elf = './images/Elf.jpg'  # Sostituisci con il percorso corretto dell'immagine
image_elf = Image.open(image_path_elf)
image_elf = image_elf.resize((150, 150))  # Regola le dimensioni dell'immagine se necessario
photo_elf = ImageTk.PhotoImage(image_elf)
ElfButton = tk.Button(image = photo_elf, command=showElf)
ElfButton.pack()

image_path_Kni = './images/Knight.jpg'  # Sostituisci con il percorso corretto dell'immagine
image_Kni = Image.open(image_path_Kni)
image_Kni = image_Kni.resize((150, 150))  # Regola le dimensioni dell'immagine se necessario
photo_Kni = ImageTk.PhotoImage(image_Kni)
KnightButton = tk.Button(image = photo_Kni, command=showKnight)
KnightButton.pack()

image_path_Wiz = './images/Wizard.jpg'  # Sostituisci con il percorso corretto dell'immagine
image_Wiz = Image.open(image_path_Wiz)
image_Wiz = image_Wiz.resize((150, 150))  # Regola le dimensioni dell'immagine se necessario
photo_Wiz = ImageTk.PhotoImage(image_Wiz)
WizardButton = tk.Button(image = photo_Wiz, command=showWizard)
WizardButton.pack()


image_path_Nin = './images/Ninja.png'  # Sostituisci con il percorso corretto dell'immagine
image_Nin = Image.open(image_path_Nin)
image_Nin = image_Nin.resize((150, 150))  # Regola le dimensioni dell'immagine se necessario
photo_Nin = ImageTk.PhotoImage(image_Nin)
NinjaButton = tk.Button(image = photo_Nin, command=showNinja)
NinjaButton.pack()



# CHARACTER CHOISE
question_label = tk.Label(window, text="Cosa vuoi essere in questo mondo?")


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

attack_label.pack()
defense_label.pack()
special_attack_label.pack()
invio_button.pack()

    

#Run window
if __name__ == "__main__":
    window.mainloop()
