from Classi.Knight import Knight as newKnight
from Classi.Wizard import Wizard as newWizard
from Classi.Elf import Elf as newElf
from Classi.Ninja import Ninja as newNinja

def createWizard(name, lineage, gender):
    return newWizard(lineage, name, 0, None, 200, 10, 5, {'nome': 'Avadakedavra', 'danno': 20}, gender, 0, 50, [])

def createKnight(name, lineage, gender):
    return newKnight(lineage, name, 0, None, 200, 15, 10, {'nome': 'Charge', 'danno': 10}, gender, 0, 50, [])

def createElf(name, lineage, gender):
    return newElf(lineage, name, 0, None, 200, 10, 3, {'nome': 'Sharpshooter', 'danno': 25}, gender, 0, 50, [])

def createNinja(name, lineage, gender):
    return newNinja(lineage, name, 0, None, 200, 15, 15, {'nome': 'Shadow Clone', 'danno': 15}, gender, 0, 50, [])
