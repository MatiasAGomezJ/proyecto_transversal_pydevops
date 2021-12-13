# Devuelve una base de datos del cluster
def obtener_bd(cluster, nombre_bd):
    
    # Obtenemos la base de datos específicada
    bd = cluster[nombre_bd]

    return bd

