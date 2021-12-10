from pymongo import MongoClient
import certifi

def obtener_cluster(ruta):
    cluster = MongoClient(ruta, tlsCAFile=certifi.where())
    return cluster

    