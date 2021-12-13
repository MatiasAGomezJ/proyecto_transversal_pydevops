from pymongo import MongoClient
import certifi

def obtener_cluster(ruta):
    
    try:
        # Devuelve un cluster a partir de la ruta pasada
        cluster = MongoClient(ruta, tlsCAFile=certifi.where())
    except:
        print("La conexion con el cluster ha fallado")
        exit()
    else:
        print("Se ha conectado correctamente con el cluster")

    return cluster
    