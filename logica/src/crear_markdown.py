from logica.src.obtener_documentos import obtener_documentos
from logica.src.obtener_texto_para_markdown import obtener_texto_para_markdown
from logica.src.crear_nombre_archivo import crear_nombre_archivo
from logica.src.crear_archivos_markdown import crear_archivos_markdown

# Crea los archivos markdown desde cero
def crear_markdown(coleccion, filtro_diccionario):
    
    # Obtenemos una lista de documentos a partir de la colección especificada y del filtro elegido 
    lista_documentos = obtener_documentos(coleccion, filtro_diccionario)

    # Conseguimos la información que guardar en los ficheros markdown
    texto_para_markdown = obtener_texto_para_markdown(lista_documentos)

    # Guarda el nombre que le daremos al archivo markdown a partir del filtro que le hemos pasado
    nombre_archivo = crear_nombre_archivo(filtro_diccionario)
    
    # Creará los archivos markdown a partir del texto y el nombre del archivo
    crear_archivos_markdown(texto_para_markdown, nombre_archivo)
