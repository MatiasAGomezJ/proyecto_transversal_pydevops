# Devuelve una colección de la base de datos
def obtener_coleccion(db, nombre_collecion):

    # Guarda la colección especificada 
    coleccion = db[nombre_collecion]
    
    return coleccion
