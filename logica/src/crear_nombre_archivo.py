# Devuelve un string a partir de un diccionario
def crear_nombre_archivo(filtro_diccionario):

    # Primero creamos la variable en la cual se guardará el nombre
    nombre_archivo = ""

    # Si el filtro está vacio entonces devolvera un nombre por defecto
    if filtro_diccionario == {}:
        return "todos"

    # Guardamos en una lista todas las keys del filtro
    lista = list(filtro_diccionario.keys())

    # Por cada item de la lista añadimos al nombre su clave y su valor
    for item in lista:
        nombre_archivo += item + str(filtro_diccionario[item])

    # Luego lo transformamos en minuscula
    nombre_archivo = nombre_archivo.lower()

    return nombre_archivo
