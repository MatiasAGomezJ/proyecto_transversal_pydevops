from ..src.obtener_documentos import obtener_documentos
from ...acceso_datos.src.obtener_cluster import obtener_cluster
from ...acceso_datos.src.obtener_bd import obtener_bd
from ...acceso_datos.src.obtener_coleccion import obtener_coleccion
import pytest


@pytest.mark.obtener_documentos
def test_funciona():
    # coleccion = [
    #                 {'r': 1,    'g': 50,    'b': 0},
    #                 {'r': 125,  'g': 150,   'b': 25},
    #                 {'r': 255,  'g': 50,    'b': 50},
    #                 {'r': 1,    'g': 150,   'b': 75},
    #                 {'r': 125,  'g': 50,    'b': 100},
    #                 {'r': 255,  'g': 150,   'b': 125},
    #                 {'r': 1,    'g': 50,    'b': 150},
    #                 {'r': 125,  'g': 150,   'b': 175},
    #                 {'r': 255,  'g': 50,    'b': 200},
    #             ]

    cluster = obtener_cluster(
        "mongodb+srv://matias:12345@proyecto.bjagm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    )
    db = obtener_bd(cluster, "prueba")
    coleccion = obtener_coleccion(db, "prueba")

    clave_filtro = "r"
    valor_filtro = 125

    filtro = {clave_filtro: valor_filtro}

    lista_docs = obtener_documentos(coleccion, filtro)

    for doc in lista_docs:
        assert doc[clave_filtro] == valor_filtro


def test_filtro_vacio():
    # coleccion = [
    #                 {'r': 1,    'g': 50,    'b': 0},
    #                 {'r': 125,  'g': 150,   'b': 25},
    #                 {'r': 255,  'g': 50,    'b': 50},
    #                 {'r': 1,    'g': 150,   'b': 75},
    #                 {'r': 125,  'g': 50,    'b': 100},
    #                 {'r': 255,  'g': 150,   'b': 125},
    #                 {'r': 1,    'g': 50,    'b': 150},
    #                 {'r': 125,  'g': 150,   'b': 175},
    #                 {'r': 255,  'g': 50,    'b': 200},
    #             ]

    cluster = obtener_cluster(
        "mongodb+srv://matias:12345@proyecto.bjagm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    )
    db = obtener_bd(cluster, "prueba")
    coleccion = obtener_coleccion(db, "prueba")

    numero_documentos = coleccion.count_documents({})

    filtro = {}

    lista_docs = obtener_documentos(coleccion, filtro)

    assert numero_documentos == len(lista_docs)
