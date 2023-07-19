from Classi.Entity import Entity as newEntity
from Classi.Character import Character as newCharacter
from Classi.Wizard import Wizard as newWizard
from Classi.Elf import Elf as newElf
from Classi.Knight import Knigth as newKnigth
from Classi.Ninja import Ninja as newNinja
import DB.CRUD as db

def loadCharacter(data):
    print(data["type"])
    if data["type"] == "Wizard":
        #Create a wizard object
        return newWizard(data["lineage"], data["name"], data["level"], data["weapon"], data["life"], data["basic_attack"],
                data["defence"], data["special_attack"], data["gender"], data["exp"], data["wallet"], data["inventory"])
    elif data["type"] == "Elf":
        return newElf(data["lineage"], data["name"], data["level"], data["weapon"], data["life"], data["basic_attack"],
                data["defence"], data["special_attack"], data["gender"], data["exp"], data["wallet"], data["inventory"])
    elif data["type"] == "Ninja":
        return newNinja(data["lineage"], data["name"], data["level"], data["weapon"], data["life"], data["basic_attack"],
                data["defence"], data["special_attack"], data["gender"], data["exp"], data["wallet"], data["inventory"])
    else:
        return newKnigth(data["lineage"], data["name"], data["level"], data["weapon"], data["life"], data["basic_attack"],
                data["defence"], data["special_attack"], data["gender"], data["exp"], data["wallet"], data["inventory"])


dataPlayer = db.getCharacter("Strage")
#print(dataPlayer)
character = loadCharacter(dataPlayer)
print(type(character))



