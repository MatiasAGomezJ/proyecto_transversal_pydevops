from pymongo import MongoClient
from pprint import pprint
import certifi

def extraer_datos_mongo(ruta):
    sandbox = MongoClient(ruta, tlsCAFile=certifi.where())
    db = sandbox.amenities
    collection = db.packs2
    documentos = collection.find()
    lista_documentos = []
    for documento in documentos:
        lista_documentos.append(documento)
    return lista_documentos

if __name__ == '__main__':
    extraer_datos_mongo()
