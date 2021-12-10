def obtener_texto_para_markdown(lista_documentos):
    
    texto_para_markdown = ''
        
    for documento in lista_documentos:
        
        # Añadimos el titulo/nombre 
        texto_para_markdown += "# " + str(documento['NamePack']) + "\n\n"

        # Añadimos el contenido
        texto_para_markdown += str(documento['ContentPack']) + "\n\n"

        # Añadimos el precio
        texto_para_markdown += "El precio de este pack es: " + str(documento['PricePack']) + " €\n\n"
        
        # Añadimos si tiene cupon
        texto_para_markdown += "_Cupon_ "
        if documento['HasCupon'] == True:
            texto_para_markdown += "✅"
        else:
            texto_para_markdown += "❌"
        texto_para_markdown += "\n\n"

        # Añadimos si tiene parking
        texto_para_markdown += "_Parking_ "
        if documento['HasParking'] == True:
            texto_para_markdown += "✅"
        else:
            texto_para_markdown += "❌"
        texto_para_markdown += "\n\n"

    return texto_para_markdown