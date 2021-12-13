from os import path, mkdir, listdir
from shutil import copyfile

# Mueve archivos desde la carpeta 'markdowns' hacia la carpeta de 'ruta_destino'
def mover_markdowns(ruta_destino):

    # Guardamos la ruta donde se guardarán los archivos
    ruta_origen = './markdowns/'

    # Comprobamos que esa ruta existe y si no, la creamos
    if not path.isdir(ruta_destino):
        mkdir(ruta_destino)

    # Crea una lista con el nombre de todos los archivos en la ruta especificada
    lista_archivos_markdown = listdir(ruta_origen)

    # Por cada archivo en la lista
    for archivo in lista_archivos_markdown:

        # Crea una ruta con el nombre de la carpeta y el nombre del archivo
        ruta_origen_completa    = path.join(ruta_origen, archivo)
        ruta_destino_completa   = path.join(ruta_destino, archivo)

        # Copiamos el archivo
        copyfile(ruta_origen_completa, ruta_destino_completa)

    print("Se han movido los archivos a la siguiente ruta: " + ruta_destino)