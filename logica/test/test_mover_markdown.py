from ..src.mover_markdowns import mover_markdowns
from os import listdir
import pytest

@pytest.mark.mover_markdowns

def test_funciona():
    ruta_origen = './markdowns'
    ruta_destino = './logica/test/carpeta_de_prueba/'

    mover_markdowns(ruta_destino)

    assert len(listdir(ruta_origen)) == len(listdir(ruta_destino))

