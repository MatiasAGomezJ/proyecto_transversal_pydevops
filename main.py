from pprint import pprint
from src.extrear_datos_mongo import extraer_datos_mongo


def de_mongo_a_hugo(pathDB):
    lista_diccionarios = extraer_datos_mongo(pathDB)
    pprint(lista_diccionarios)


path = 'mongodb+srv://m001-student:12345@sandbox.glkvp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'




de_mongo_a_hugo(path)
