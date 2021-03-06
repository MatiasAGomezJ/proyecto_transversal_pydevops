from acceso_datos.src.obtener_cluster import obtener_cluster
from acceso_datos.src.obtener_bd import obtener_bd
from acceso_datos.src.obtener_coleccion import obtener_coleccion

from logica.src.crear_markdown import crear_markdown
from logica.src.mover_markdowns import mover_markdowns


def main():

    # Acceder a la base de datos ----
    cluster = obtener_cluster(
        "mongodb+srv://m001-student:12345@sandbox.glkvp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    )
    bd = obtener_bd(cluster, "amenities")
    coleccion = obtener_coleccion(bd, "packs2")
    # ----

    # Logica ----
    crear_markdown(coleccion, {})
    crear_markdown(coleccion, {"HasParking": True})
    crear_markdown(coleccion, {"HasCupon": True})
    crear_markdown(coleccion, {"HasCupon": False, "HasParking": False})

    mover_markdowns("./servicio/web/content/posts/")
    # ----


main()
