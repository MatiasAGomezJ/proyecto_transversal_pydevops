import os   

def crear_archivos_markdown(texto_para_markdown, nombre_archivo):
    ruta = "./markdowns/"

    if not os.path.isdir(ruta):
        os.mkdir(ruta)

    if nombre_archivo == '':
        nombre_archivo = 'default'

    archivo = open(ruta + nombre_archivo + ".md", 'w', encoding="utf-8")
    archivo.write(texto_para_markdown)
    archivo.close()
