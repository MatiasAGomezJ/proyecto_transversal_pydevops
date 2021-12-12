from src.obtener_bd import obtener_bd
from pymongo import MongoClient
import pytest

@pytest.mark.obtener_bd

def test_funciona():
    ruta = 'mongodb+srv://m001-student:12345@sandbox.glkvp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
    cluster = MongoClient(ruta)
    db = cluster['amenities']

    assert 'packs2' in db.list_collection_names()