def crear_nombre_archivo(filtro_diccionario):

    nombre_archivo = ''

    if filtro_diccionario == {}: 
        return 'todos'

    lista = list(filtro_diccionario.keys()) 

    for item in lista:
        nombre_archivo += item + str(filtro_diccionario[item])
    
    nombre_archivo = nombre_archivo.lower()

    return nombre_archivo