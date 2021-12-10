def obtener_documentos(coleccion, diccionario):
    documentos = coleccion.find(diccionario)
    lista_documentos = []
    for documento in documentos:
        lista_documentos.append(documento)

    return lista_documentos 