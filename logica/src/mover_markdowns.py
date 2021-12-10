import os
import shutil

rutaOrigen = 

rutaDestino =

if not os.path.isdir(rutaOrigen):
    print('la primera carpeta no existe')
elif not os.path.isdir(rutaDestino):
    print('la segunda carpeta no existe')

else:
    contenidos = os.listdir(rutaOrigen)

    for elemento in contenidos:
        try:
            src = os.path.join(rutaOrigen, elemento) # origen
            dst = os.path.join(rutaDestino, elemento) # destino
            shutil.copy(src, dst)
            print("Correcto")
        except:
            print("Falló")
            print("Error, no se pudo copia el archivo. Verifique los permisos de escritura")