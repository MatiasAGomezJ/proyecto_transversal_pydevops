


from acceso_datos.src.obtener_cluster import obtener_cluster
from acceso_datos.src.obtener_coleccion import obtener_coleccion
from acceso_datos.src.obtener_bd import obtener_bd
from logica.src.dicts_a_markdown import dicts_a_markdown


def mongo_a_hugo():


    cluster = obtener_cluster('mongodb+srv://m001-student:12345@sandbox.glkvp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    bd = obtener_bd(cluster)
    coleccion = obtener_coleccion(bd)
    dicts_a_markdown(bd)
    