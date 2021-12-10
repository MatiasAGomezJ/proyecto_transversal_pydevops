from logica.src.obtener_documentos import obtener_documentos
from logica.src.obtener_texto_para_markdown import obtener_texto_para_markdown

def crear_markdown(coleccion, diccionario):
    
    lista_documentos = obtener_documentos(coleccion, diccionario)

    texto_para_mardown = obtener_texto_para_markdown(lista_documentos)

    # Creamos el archivo con el nombre del pack como nombre del archivo
    archivo = open("./markdowns/" + "name" + ".md", 'w', encoding="utf-8")
    # Escribimos en el fichero todo lo añadido en la variable md
    archivo.write(texto_para_mardown)
    # Cerramos el archivo
    archivo.close()