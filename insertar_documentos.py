from acceso_datos.src.obtener_cluster import obtener_cluster
from acceso_datos.src.obtener_bd import obtener_bd
from acceso_datos.src.obtener_coleccion import obtener_coleccion

def insertar_documentos(lista_diccionarios):
    
    cluster = obtener_cluster('mongodb+srv://m001-student:12345@sandbox.glkvp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    bd = obtener_bd(cluster, 'amenities')
    coleccion = obtener_coleccion(bd, 'packs2')

    for diccionario in lista_diccionarios:
        coleccion.insert_one(diccionario)

lista_diccionarios = [
    {
                            "PricePack":"100 €",
                            "NamePack":"Tier 6 Pack",
                            "ContentPack":"This pack is amazing",
                            "HasCupon":True,
                            "HasParking":True
                        },
                        {
                            "PricePack":"125 €",
                            "NamePack":"Tier 7 Pack",
                            "ContentPack":"The 7 tier pack offers as much as you can imagine",
                            "HasCupon":True,
                            "HasParking":True
                        }
]
insertar_documentos(lista_diccionarios)