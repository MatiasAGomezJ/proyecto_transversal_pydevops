from pprint import pprint
from acceso_datos.src.extrear_datos_mongo import extraer_datos_mongo
from logica.src.dicts_a_markdown import dicts_a_markdown
from logica.src.separar_grupos import selector_datos_db


def de_mongo_a_hugo():
    bbdd = extraer_datos_mongo()
    dicts_a_markdown(bbdd)

de_mongo_a_hugo()
