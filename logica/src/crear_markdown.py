from logica.src.obtener_documentos import obtener_documentos
from logica.src.obtener_texto_para_markdown import obtener_texto_para_markdown
from logica.src.crear_nombre_archivo import crear_nombre_archivo
from logica.src.crear_archivos_markdown import crear_archivos_markdown

def crear_markdown(coleccion, filtro_diccionario):
    
    lista_documentos = obtener_documentos(coleccion, filtro_diccionario)

    texto_para_mardown = obtener_texto_para_markdown(lista_documentos)

    nombre_archivo = crear_nombre_archivo(filtro_diccionario)

    crear_archivos_markdown(texto_para_mardown, nombre_archivo)
