# Get the database using the method we defined in pymongo_test_insert file
from pymongo import MongoClient

def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb+srv://Admin:Password1@cluster0.bmwnxll.mongodb.net/?retryWrites=true&w=majority"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING, tls=True, tlsAllowInvalidCertificates=True)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['PyLand']
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
   # Get the database
   dbname = get_database()

   
dbname = get_database()
collection_name = dbname["Giocatori"]


#collection_name.insert_one(item_3)

def addCharacter(nome, type, obj):
  """
   Method for Add new player in DB
  """
  collection_name = dbname["Giocatori"]
  character = {
      "lineage": obj.lineage,
      "name": obj.name,
      "level": obj.level,
      "type": type,
      "weapon": obj.weapon,
      "life": obj.life,
      "basic_attack": obj.basic_attack,
      "defence": obj.defence,
      "special_attack": obj.special_attack,
      "gender": obj.gender, 
      "exp": obj.exp,
      "wallet": obj.wallet,
      "inventory": obj.inventory

  }

  collection_name.insert_one(character)



def getCharacter(nome):
   '''
   get character from DB select by name
   '''
   giocatori = dbname["Giocatori"]
   return giocatori.find_one({"name": nome})
   

def updateCharacter(player):
   pass


def delete_character(player):
   giocatori = dbname["Giocatori"]
   giocatori.delete_one({"name":player.name})
   print("Giocatore eliminato")



print("WE")
