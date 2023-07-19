from Classi.Entity import Entity as newEntity
from Classi.Character import Character as newCharacter
from Classi.Wizard import Wizard as newWizard
import DB.CRUD as db

def loadCharacter(data):
    print(data["type"])
    if data["type"] == "Wizard":
        #Create a wizard object
        return newWizard(data["lineage"], data["name"], data["level"], data["weapon"], data["life"], data["basic_attack"],
                data["defence"], data["special_attack"], data["gender"], data["exp"], data["wallet"], data["inventory"])
        
    elif data["type"] == "Elf":
        pass



dataPlayer = db.getCharacter("Nitro")
#print(dataPlayer)
character = loadCharacter(dataPlayer)
print(character.name)



