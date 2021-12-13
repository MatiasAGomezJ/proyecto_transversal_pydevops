from ..src.crear_nombre_archivo import crear_nombre_archivo
import pytest


@pytest.mark.crear_nombre_archivo
def test_funciona():
    filtro = {"a": 1}
    assert crear_nombre_archivo(filtro) == "a1"
    filtro = {"a": 1, "b": "alohomora"}
    assert crear_nombre_archivo(filtro) == "a1balohomora"
    filtro = {"a": 1, "b": "alohomora", "c": [1, 2, 3]}
    assert crear_nombre_archivo(filtro) == "a1balohomorac[1, 2, 3]"


def test_filtro_vacio():
    filtro = {}
    assert crear_nombre_archivo(filtro) == "todos"
