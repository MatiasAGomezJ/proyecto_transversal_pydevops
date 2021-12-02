from pprint import pprint
from acceso_datos.src.extrear_datos_mongo import extraer_datos_mongo
from logica.src.dicts_a_markdown import dicts_a_markdown
from separacion_de_datos.src.separar_grupos import selector_datos_db


def de_mongo_a_hugo(pathDB):
    bbdd = extraer_datos_mongo(pathDB)
    lista_documentos = selector_datos_db(bbdd)
    dicts_a_markdown(lista_documentos)



path = 'mongodb+srv://m001-student:12345@sandbox.glkvp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

de_mongo_a_hugo(path)
