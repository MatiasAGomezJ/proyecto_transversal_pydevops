import os   

# Crea archivos de extension markdown a partir de 2 strings, el primero define los que será escrito y el segundo en nombre del archivo
def crear_archivos_markdown(texto_para_markdown, nombre_archivo):

    # Guardamos la ruta donde se guardarán los archivos
    ruta = "./markdowns/"

    # Comprobamos que esa ruta existe y si no, la creamos
    if not os.path.isdir(ruta):
        os.mkdir(ruta)

    # Si 'nombre_archivo' esta vacio, ponemos un nombre por defecto
    if nombre_archivo == '':
        nombre_archivo = 'default'

    # Creamos el archivo en base a la ruta y el nombre
    archivo = open(ruta + nombre_archivo + ".md", 'w', encoding="utf-8")
    # Escribimos el texto dentro del archivo
    archivo.write(texto_para_markdown)
    # Cerramos el archivo
    archivo.close()
