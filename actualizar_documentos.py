from acceso_datos.src.obtener_cluster import obtener_cluster
from acceso_datos.src.obtener_bd import obtener_bd
from acceso_datos.src.obtener_coleccion import obtener_coleccion


def actualizar_documentos(lista_diccionarios, datos_actualizacion):

    cluster = obtener_cluster(
        "mongodb+srv://m001-student:12345@sandbox.glkvp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    )
    bd = obtener_bd(cluster, "amenities")
    coleccion = obtener_coleccion(bd, "packs2")

    actualizacion = {"$set": datos_actualizacion}

    for diccionario in lista_diccionarios:
        coleccion.update_one(diccionario, actualizacion)


lista_diccionarios = [
    {
        "PricePack": "100 €",
        "NamePack": "Tier 6 Pack",
        "ContentPack": "This pack is amazing",
        "HasCupon": True,
        "HasParking": True,
    },
    {
        "PricePack": "125 €",
        "NamePack": "Tier 7 Pack",
        "ContentPack": "The 7 tier pack offers as much as you can imagine",
        "HasCupon": True,
        "HasParking": True,
    },
]

datos_actualizacion = {"HasParking": False}

actualizar_documentos(lista_diccionarios, datos_actualizacion)
