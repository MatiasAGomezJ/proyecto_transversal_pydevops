from acceso_datos.src.obtener_cluster import obtener_cluster
from acceso_datos.src.obtener_bd import obtener_bd
from acceso_datos.src.obtener_coleccion import obtener_coleccion

def insertar_documentos(lista_diccionarios):
    
    cluster = obtener_cluster('mongodb+srv://matias:12345@proyecto.bjagm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    bd = obtener_bd(cluster, 'prueba')
    coleccion = obtener_coleccion(bd, 'prueba')

    for diccionario in lista_diccionarios:
        coleccion.insert_one(diccionario)

lista_diccionarios = [
    {
        'r': 255,
        'g': 255,
        'b': 255
    }
]
insertar_documentos(lista_diccionarios)