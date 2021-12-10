from logica.src.obtener_documentos import obtener_documentos

def crear_markdown(coleccion, diccionario):
    
    lista_documentos = obtener_documentos(coleccion, diccionario)

    md = ''
        
    for documento in lista_documentos:
    
        # Añadimos el titulo/nombre 
        md += "# " + str(documento['NamePack']) + "\n\n"

        # Añadimos el contenido
        md += str(documento['ContentPack']) + "\n\n"

        # Añadimos el precio
        md += "El precio de este pack es: " + str(documento['PricePack']) + " €\n\n"
        
        # Añadimos si tiene cupon
        md += "_Cupon_ "
        if documento['HasCupon'] == False:
            md += "✅"
        else:
            md += "❌"
        md += "\n\n"

        # Añadimos si tiene parking
        md += "_Parking_ "
        if documento['HasParking'] == False:
            md += "✅"
        else:
            md += "❌"
        md += "\n\n"

        # Creamos el archivo con el nombre del pack como nombre del archivo
        archivo = open("./markdowns/" + documento["NamePack"] + ".md", 'w', encoding="utf-8")
        # Escribimos en el fichero todo lo añadido en la variable md
        archivo.write(md)
        # Cerramos el archivo
        archivo.close()