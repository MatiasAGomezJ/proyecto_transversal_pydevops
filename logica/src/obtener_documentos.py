# Devuelve una lista de documentos a partir de una colección de documentos y de un diccionario
def obtener_documentos(coleccion, filtro_diccionario):

    # Utilizando la función find(), conseguimos una lista de documentos a partir de un filtro
    # En python los items de esta lista no se pueden leer, por lo tanto crearemos una lista de python
    documentos = coleccion.find(filtro_diccionario)

    # Creamos una lista vacia para poder guardar los documentos
    lista_documentos = []

    # Por cada documento en la lista de mongo, añadiremos este a la lista vacía
    for documento in documentos:
        lista_documentos.append(documento)

    print("Se han extraido los documentos de la coleccion")

    return lista_documentos 