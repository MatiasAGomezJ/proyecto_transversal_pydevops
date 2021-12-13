# Devuelve una base de datos del cluster
def obtener_bd(cluster, nombre_bd):

    # Obtenemos la base de datos específicada
    bd = cluster[nombre_bd]
    print("Se ha accesido a la base de datos: " + nombre_bd)
    return bd
