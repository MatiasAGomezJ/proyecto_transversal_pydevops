from pymongo import MongoClient
import certifi

def obtener_cluster(ruta):
    
    # Devuelve un cluster a partir de la ruta pasada
    cluster = MongoClient(ruta, tlsCAFile=certifi.where())

    return cluster
    