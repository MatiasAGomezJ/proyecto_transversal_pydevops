from pymongo import MongoClient

def selector_datos_db(db):
    collection = db.packs2
    documentos = collection.find()
    lista_documentos = []
    for documento in documentos:
        lista_documentos.append(documento)

    return lista_documentos 