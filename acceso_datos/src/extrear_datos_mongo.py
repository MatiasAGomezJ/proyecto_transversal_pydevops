from pymongo import MongoClient
from pprint import pprint
import certifi

def extraer_datos_mongo(ruta):
    sandbox = MongoClient(ruta, tlsCAFile=certifi.where())
    db = sandbox.amenities
    return db

if __name__ == '__main__':
    print(extraer_datos_mongo())