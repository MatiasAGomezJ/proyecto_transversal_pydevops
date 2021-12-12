from ..src.obtener_texto_para_markdown import obtener_texto_para_markdown
import pytest

@pytest.mark.obtener_texto_para_markdown

def test_funciona():
    lista_documentos = [
                        {
                            "_id":{"$oid":"619a9b91a2b4bbbb8e69bc60"},
                            "PricePack":"Free",
                            "NamePack":"Free Pack",
                            "ContentPack":"This pack includes a bag full of sweets",
                            "HasCupon":False,
                            "HasParking":False
                        },
                        {
                            "_id":{"$oid":"619a9b92a2b4bbbb8e69bc61"},
                            "PricePack":"5€",
                            "NamePack":"Tier 1 Pack",
                            "ContentPack":"this low-priced pack includes a bag of sweets plus an organized hotel welcome ",
                            "HasCupon":False,
                            "HasParking":False
                        }
                        ]
    texto_resultante = '# Free Pack\n\nThis pack includes a bag full of sweets\n\nEl precio de este pack es: Free\n\n_Cupon_ ❌\n\n_Parking_ ❌\n\n# Tier 1 Pack\n\nthis low-priced pack includes a bag of sweets plus an organized hotel welcome \n\nEl precio de este pack es: 5€\n\n_Cupon_ ❌\n\n_Parking_ ❌\n\n'

    assert obtener_texto_para_markdown(lista_documentos) == texto_resultante