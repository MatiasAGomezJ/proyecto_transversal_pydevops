from ..src.crear_archivos_markdown import crear_archivos_markdown
from os import path
import pytest


@pytest.mark.crear_archivos_markdown
def test_funciona():
    texto = "texto1"
    nombre = "nombre1"
    crear_archivos_markdown(texto, nombre)

    ruta_archivo = "./markdowns/" + nombre + ".md"

    assert path.isfile(ruta_archivo)

    archivo = open(ruta_archivo, "r")

    acu = ""
    for linea in archivo.readlines():
        acu += linea

    assert texto == acu
    # ----
    texto = "a\nb\n\ncde"
    nombre = "ssd"
    crear_archivos_markdown(texto, nombre)

    ruta_archivo = "./markdowns/" + nombre + ".md"

    assert path.isfile(ruta_archivo)

    archivo = open(ruta_archivo, "r")

    acu = ""
    for linea in archivo.readlines():
        acu += linea

    assert texto == acu


def test_texto_vacio():
    texto = ""
    nombre = "nombre2"
    crear_archivos_markdown(texto, nombre)

    ruta_archivo = "./markdowns/" + nombre + ".md"

    assert path.isfile(ruta_archivo)

    archivo = open(ruta_archivo, "r")

    acu = ""
    for linea in archivo.readlines():
        acu += linea

    assert texto == acu
    assert path.getsize(ruta_archivo) == 0


def test_nombre_vacio():
    texto = "texto2"
    nombre = ""
    crear_archivos_markdown(texto, nombre)

    ruta_archivo = "./markdowns/" + "default" + ".md"

    assert path.isfile(ruta_archivo)

    archivo = open(ruta_archivo, "r")

    acu = ""
    for linea in archivo.readlines():
        acu += linea

    assert texto == acu
