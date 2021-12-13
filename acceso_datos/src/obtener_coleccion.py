# Devuelve una colección de la base de datos
def obtener_coleccion(db, nombre_coleccion):

    # Guarda la colección especificada
    coleccion = db[nombre_coleccion]
    print("Se ha accesido a la coleccion: " + nombre_coleccion)
    print("--------")
    return coleccion
