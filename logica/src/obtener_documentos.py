def obtener_documentos(coleccion, filtro_diccionario):
    documentos = coleccion.find(filtro_diccionario)
    lista_documentos = []
    for documento in documentos:
        lista_documentos.append(documento)

    return lista_documentos 