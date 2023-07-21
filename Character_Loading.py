
from Classi.Wizard import Wizard as newWizard
from Classi.Elf import Elf as newElf
from Classi.Knight import Knight as newKnight
from Classi.Ninja import Ninja as newNinja
from Classi.Weapons import Weapon as newWeapon
import DB.CRUD as db


def get_inventario(diz):
    weapons = []
    for weapon in diz:
        weapons.append(newWeapon(weapon["name"], weapon["damage"], weapon["price"], weapon["level"]))

    return weapons

def loadCharacter(data):
    '''
    In base al tipo di personaggio carica un oggetto diverso
    '''


    if data["type"] == "Wizard":
        return newWizard(data["lineage"], data["name"], data["level"], data["weapon"], data["life"], data["basic_attack"],
                data["defence"], data["special_attack"], data["gender"], data["exp"], data["wallet"], get_inventario(data["inventory"]))
    elif data["type"] == "Elf":
        return newElf(data["lineage"], data["name"], data["level"], data["weapon"], data["life"], data["basic_attack"],
                data["defence"], data["special_attack"], data["gender"], data["exp"], data["wallet"], get_inventario(data["inventory"]))
    elif data["type"] == "Ninja":
        return newNinja(data["lineage"], data["name"], data["level"], data["weapon"], data["life"], data["basic_attack"],
                data["defence"], data["special_attack"], data["gender"], data["exp"], data["wallet"], get_inventario(data["inventory"]))
    else:
        return newKnight(data["lineage"], data["name"], data["level"], data["weapon"], data["life"], data["basic_attack"],
                data["defence"], data["special_attack"], data["gender"], data["exp"], data["wallet"], get_inventario(data["inventory"]))

def getCharacter(name):
    '''
    Prende le informazioni del personaggio dal DB e le passa al metodo loadCharacter per caricare le infromazioni in oggetto che ritorna
    '''
    dataPlayer = db.getCharacter(name)
    return loadCharacter(dataPlayer)


#Function for create the object of character
def createWizard(name, lineage, gender):
    return newWizard(lineage, name, 0, None, 200, 10, 5, {'nome': 'Avadakedavra', 'danno': 20}, gender, 0, 50, [])

def createKnight(name, lineage, gender):
    return newKnight(lineage, name, 0, None, 200, 15, 10, {'nome': 'Charge', 'danno': 10}, gender, 0, 50, [])

def createElf(name, lineage, gender):
    return newElf(lineage, name, 0, None, 200, 10, 3, {'nome': 'Sharpshooter', 'danno': 25}, gender, 0, 50, [])

def createNinja(name, lineage, gender):
    return newNinja(lineage, name, 0, None, 200, 15, 15, {'nome': 'Shadow Clone', 'danno': 15}, gender, 0, 50, [])


