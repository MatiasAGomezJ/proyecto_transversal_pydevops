from pymongo import MongoClient
from pprint import pprint
import certifi

def extraer_datos_mongo():
    sandbox = MongoClient('mongodb+srv://m001-student:12345@sandbox.glkvp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=certifi.where())
    db = sandbox.amenities
    return db