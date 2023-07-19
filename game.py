from Classi.Entity import Entity as newEntity
from Classi.Character import Character as newCharacter
from Classi.Wizard import Wizard as newWizard
import DB.CRUD as db

def loadCharacter(data):
    ent = newCharacter("Buono", data["nome"], 1, None, 5, 10, 5, 15, data["gender"], data["exp"], data["wallet"], data["inventory"] )
    if data["type"] == "Wizard":
        #Create a wizard object
        print(newWizard(ent, data["exp"], data["wallet"], data["inventory"], ))
        
    elif data["type"] == "Elf":
        pass


w = newWizard("B", "A", 1, "dcd", 10, 10, 5, 15, "M", 4, 10, [])
print(w)

dataPlayer = db.getCharacter("Alsi")
character = loadCharacter(dataPlayer)




