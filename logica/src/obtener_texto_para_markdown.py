# Devuelve una string a partir una lista de diccionarios
def obtener_texto_para_markdown(lista_documentos):

    # Creammos una acumulador
    texto_para_markdown = ""

    # Por cada documento en la lista ->
    for documento in lista_documentos:

        # Añadimos su titulo/nombre
        texto_para_markdown += "# " + str(documento["NamePack"]) + "\n\n"

        # Añadimos su contenido
        texto_para_markdown += str(documento["ContentPack"]) + "\n\n"

        # Añadimos su precio
        texto_para_markdown += (
            "El precio de este pack es: " + str(documento["PricePack"]) + "\n\n"
        )

        # Añadimos si tiene cupon
        texto_para_markdown += "_Cupon_ "
        if documento["HasCupon"] == True:
            texto_para_markdown += "✅"
        else:
            texto_para_markdown += "❌"
        texto_para_markdown += "\n\n"

        # Añadimos si tiene parking
        texto_para_markdown += "_Parking_ "
        if documento["HasParking"] == True:
            texto_para_markdown += "✅"
        else:
            texto_para_markdown += "❌"
        texto_para_markdown += "\n\n"

    return texto_para_markdown
