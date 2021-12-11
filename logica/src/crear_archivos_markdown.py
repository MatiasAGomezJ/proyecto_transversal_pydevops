import os

def crear_archivos_markdown(texto_para_mardown, nombre_archivo):
    ruta = "./markdowns/"

    if not os.path.isdir(ruta):
        os.mkdir(ruta)

    archivo = open(ruta + nombre_archivo + ".md", 'w', encoding="utf-8")
    archivo.write(texto_para_mardown)
    archivo.close()
