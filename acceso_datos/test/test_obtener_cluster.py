from src.obtener_cluster import obtener_cluster
from pymongo import MongoClient
import pytest


@pytest.mark.obtener_cluster
def test_funciona():
    ruta = "mongodb+srv://m001-student:12345@sandbox.glkvp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    cluster = obtener_cluster(ruta)
    assert "amenities" in cluster.list_database_names()
