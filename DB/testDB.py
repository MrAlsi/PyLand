# Get the database using the method we defined in pymongo_test_insert file
from pymongo_get_database import get_database

dbname = get_database()
collection_name = dbname["Giocatori"]



#collection_name.insert_one(item_3)

print("WE")