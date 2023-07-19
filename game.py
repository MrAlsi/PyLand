
from Classi.Wizard import Wizard as newWizard
from Classi.Elf import Elf as newElf
from Classi.Knight import Knigth as newKnigth
from Classi.Ninja import Ninja as newNinja
import DB.CRUD as db


def loadCharacter(data):
    '''
    In base al tipo di personaggio carica un oggetto diverso
    '''
    if data["type"] == "Wizard":
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

def getCharacter(name):
    '''
    Prende le informazioni del personaggio dal DB e le passa al metodo loadCharacter per caricare le infromazioni in oggetto che ritorna
    '''
    dataPlayer = db.getCharacter(name)
    return loadCharacter(dataPlayer)


#print(type(character))
#print(character.life)




