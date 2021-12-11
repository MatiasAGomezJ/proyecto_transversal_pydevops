def crear_archivos_markdown(texto_para_mardown, nombre_archivo):
    archivo = open("./markdowns/" + nombre_archivo + ".md", 'w', encoding="utf-8")
    archivo.write(texto_para_mardown)
    archivo.close()