from os import path, mkdir, listdir
from shutil import copyfile

def mover_markdowns(ruta_destino):
    ruta_origen = './markdowns/'

    if not path.isdir(ruta_destino):
        mkdir(ruta_destino)

    lista_archivos_markdown = listdir(ruta_origen)

    for archivo in lista_archivos_markdown:

        ruta_origen_completa    = path.join(ruta_origen, archivo)
        ruta_destino_completa   = path.join(ruta_destino, archivo)

        copyfile(ruta_origen_completa, ruta_destino_completa)
