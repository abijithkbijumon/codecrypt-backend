
from pymongo import MongoClient


uri = "mongodb+srv://abhijithkbijumon:bijumon1234@cluster0.hjiup31.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client["code_crypt"]
collection = db["cost_of_living_index"]

def connectionn(location):
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        query = {'City': location}
        result = collection.find_one(query)
        print (result)
        
        return result
    except Exception as e:
        print('Error connecting to MongoDB:', e)
        return "error"


