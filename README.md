# **PROYECTO_TRANSVERSAL_PYDEVOPS**

1. **Introducción**
2. **Metodología** 
    - Carácteristicas escenciales
3. **Análisis**
    - Primer diagrama general
    - Partes interesadas
    - Requisitos funcionales
    - Requisitos no funcionales
    - Diagrama de casos de uso (UML)
    - Requisitos/Tecnologías
4. **Diseño**
    - Mapa conceptual
    - Estructura
    - Esquema
5. **Implementación**
6. **Pruebas**
    - Acceso a datos
    - Lógica 
7. **Comparación temporal**
    - Estimación inicial
    - Estimación real
    - Comparación temporal
8. **Dificultades**
9. **Futuras mejoras**

# ***1. Introducción***
El presente trabajo consiste en crear una aplicación mediante el lenguaje de programación **Python**. Esta ha de ser capaz de extraer la información necesaria que estará ubicada en una base de datos en la nube. El servicio que usaremos para esta acción será **MongoAtlas**.

Es necesario diseñar una especificación del esquema de los documentos **JSON**, ya que trabajaremos en conjunto con un compañero del segundo curso de DAW.

Los documentos JSON que obtengamos deberemos de transformarlos en ficheros **Markdown**. Para que seguido a esto, podamos situarlos en una estructura de datos que establezca **HUGO**, que és un generador de sitios estáticos, y que nos ayudará en la tarea de crear los sitios web a partir de los markdowns que le pasemos. 

Para que ésto funcione, deberemos de saber y comprender como funciona HUGO y personalizar los estilos CSS para dotar la página de una presentación adecuada.

# ***2. Metodología de software***
En este proyecto hacemos uso del ***modelo incremental***, que tiene como objetivo un crecimiento progresivo de la funcionalidad. Es decir, el producto va evolucionando con cada una de las entregas previstas hasta que se amolda a lo requerido por el cliente o destinatario. 

La tareas se dividen en iteraciones, para conseguir objetivos específicos. Para esto hicimos uso de herramientas como el apartado *"proyectos"* de Github. Que nos permitía poder organizar el trabajo en diferentes *"sprints"*. En cada sprint o cada ciclo de trabajo lo que se aspiraba a  conseguir es lo que se denomina un entregable o incremento del producto, que aporte valor al cliente.

## **Carácteristicas esenciales**

- Incrementos pequeños.
- Permite una fácil administración de las tareas en cada iteración.
- Modelo propicio a cambios o modificaciones.
- Adaptable a las necesidades que surjan.

El modelo de gestión incremental no es un modelo necesariamente rígido, es decir, que puede adaptarse a las características de cualquier tipo de proyecto, existen al menos 7 fases que debemos tener en cuenta a la hora de implementarlo.

![](https://i.imgur.com/urvQApI.jpg)

- **Requerimientos.** son los objetivos centrales y específicos que persigue el proyecto.

- **Definición de las tareas y las iteraciones.** teniendo en cuenta lo que se busca, el siguiente paso es hacer una lista de tareas y agruparlas en las iteraciones que tendrá el proyecto. Esta agrupación no puede ser aleatoria. Cada una debe perseguir objetivos específicos que la definan como tal.

- **Diseño de los incrementos.** establecidas las iteraciones, es preciso definir cuál será la evolución del producto en cada una de ellas. Cada iteración debe superar a la que le ha precedido. Esto es lo que se denomina incremento.

- **Desarrollo del incremento.** posteriormente se realizan las tareas previstas y se desarrollan los incrementos establecidos en la etapa anterior.

- **Validación de incrementos.** al término de cada iteración, los responsables de la gestión del proyecto deben dar por buenos los incrementos que cada una de ellas ha arrojado. Si no son los esperados o si ha habido algún retroceso, es necesario volver la vista atrás y buscar las causas de ello.

- **Integración de incrementos.** una vez son validados, los incrementos dan forma a lo que se denomina línea incremental o evolución del proyecto en su conjunto. Cada incremento ha contribuido al resultado final.

- **Entrega del producto.** cuando el producto en su conjunto ha sido validado y se confirma su correspondencia con los objetivos iniciales, se procede a su entrega final.


### **Ventajas** 
- Los clientes no tienen que esperar hasta que el sistema se entregue completamente para comenzar a hacer uso de él. 
- Los clientes pueden usar los incrementos iniciales como prototipo para precisar los requerimientos posteriores del sistema. 
- Minimización del riesgo de falla en el proyecto porque los errores se van corrigiendo progresivamente. 

### **Desventajas**
- Difícil de aplicar a sistemas transaccionales que tienden ser integrados y a operar como un todo. 
- Riesgos largos y complejos. 
- Pueden aumentar el coste debido a las pruebas. 
- Los errores en los requisitos se detectan tarde.

# ***3. Analisis***
## **Primer diagrama general**

Al iniciar el proyecto, decidimos hacer un esquema en papel del programa, para poder tener una mejor idea de como podíamos ir trabajando para tratar de conseguir todo lo que se nos pedían en la práctica.  

![](https://i.imgur.com/YuGvQ0r.png)

## **Partes interesadas**
En este proyecto el usuario será la única parte interesada, ya que no hay ninguna otra entidad que manipule la aplicación. 

*RF_usuario_xx*

## **Requisitos funcionales**

|  Requisitos funcionales | Descripción |
|-------------------|-------------|
| RF_Usuario_01: Conectar con la BBDD    | La aplicación debe permitir conectarse a la base de datos |
| RF_Usuario_02: Obtener documentos de la colección    | La aplicación tiene que extraer los documentos requeridos de la colección que le hayamos pasado |
| RF_Usuario_03: Crear archivos markdowns | La aplicación debe crear los archivos md a partir de los documentos de la colección |
| RF_Usuario_04: Añadir contenido a los archivos markdown  | La aplicación tiene que añadir el contenido de los documentos de la colección dentro de los archivos md respectivamente |
| RF_Usuario_05: Crear nombre a los archivos markdown  | La aplicación tiene que darle un nombre diferente a todos los archivos que se creen |
| RF_Usuario_06: Mover markdowns a la carpeta de Hugo  | La aplicación tiene que ser capaz de mover los archivos creados a la carpeta de contenido del generador de sitios estáticos |
| RF_Usuario_07: Crear nuevos documentos   | La aplicación tiene que permitir crear nuevos documentos en la coleccion de la base de datos |
| RF_Usuario_08: Leer los documentos  | La aplicación tiene que permitir leer los documentos que se encuentren en la colección |
| RF_Usuario_09: Actualizar los documentos   | La aplicación tiene que permitir actualizar documentos en la coleccion de la base de datos|
| RF_Usuario_10: Borrar los documentos  | La aplicación tiene que permitir borrar documentos de la colección|

## **Requisitos no funcionales**

| Requisitos no funcionales |
| ------------------------------------------------|
| La aplicación tiene que ser programada en Python |
| Se tiene que trabajar sobre un sistema workflow  |
| El diseño de los módulos de la aplicación ha de ser SOLID |

## **Diagrama de casos de uso (ULM)**

![](https://i.imgur.com/nY3d5jX.png)

## **Requisitos/tecnologías**

| **Tecnologías\Requisitos** | Acceder a la base de datos | Descargar documentos de la base de datos y convertirlos a markdown | Mover markdowns a la carpeta de hugo | Poder ver los markdown en una página web | Actualizar documentos | Borrar documentos | Insertar documentos | Programar código | Control de versiones |
|-----------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|
| Hugo | | | | X |
| MongoAtlas | X | X |
| Python | X | X | X | | X | X | X |
| Módulo - Pymongo | X | X | | | | | | | 
| Módulo - Certifi | X | X | | | | | | | 
| Módulo - OS | | | X | | | | | | 
| Módulo - Shutil | | | X | | | | | X | 
| Vscode | | | | | | | | X | 
| Git | | | | | | | | | X |

# ***4. Diseño***

## **Mapa conceptual** 

La arquitectura que decidimos implementar para nuestra aplicación es la denominada ***"arquitectura de multiples niveles (N-tier)"***. Esta nos permite desglosar la app en diferentes capas, y que las diferentes funciones estén separadas. 

Gracias a esto nuestra aplicación será flexible y reutilizable y adquirimos la opción de modificar o agregar una capa específica en lugar de reelaborar toda la aplicación.


![](https://i.imgur.com/PP7ZsGu.png)

## **Estructura**

La estructura del programa empieza en un modulo principal nombrado "main" el cual contiende diversos submodulos en una agrupacion especifica a la tarea que realiza. 

![](https://i.imgur.com/R859gmF.png)

El modulo principal se encarga de llamar a las otras funciones, en este modulo hay dos grupos de modulos que utiliza.

Los primeros se encargan de acceder a la base de datos de Mongo y devolver lo que le pedimos:
1. La funcion `obtener_cluster(uri)` se encarga de devolver el cluster en base a la URI que le pasamos
2. El modulo de `obtener_bd(cluster, bd)` devuelve a partir de un cluster la base de datos con el nombre que tambien le pasamos.
3. Por ultimo, la funcion `obtener_coleccion(bd, coleccion)` devuelve, de la base de datos pasada, la coleccion que ha sido pasada como parametro.

Lo otros modulos se encargan de la lógica del programa, estos estan siendo llamados desde la funcion `crear_markdown(coleccion, filtro)` :
1. La primera funcion es `obtener_documentos(coleccion, filtro)` la cual a partir de una coleccion y un diccionario, devuelve todos los documentos que haya dentro de la coleccion en los cuales esté filtro.
2. La siguiente es `obtener_texto_para_markdown(lista_documentos)` que crea el texto a partir de una lista de diccionarios
3. El modulo de `crear_nombre_archivo(filtro)` crea a partir de un diccionario un string
4. Para finalizar está la funcion `crear_archivos_markdown(texto, nombre)` crea archivos markdown de nombre el nombre pasado, y de contenido el texto pasado.

Luego está la funcion `mover_markdowns(ruta_destino)` la cual simplemente copia los archivos en la carpeta creada dentro del programa, y la mueve a la carpeta que se especifique como parametro. 

Despues estan separadas del resto las demás funciones CRUD.
1. La función `insertar_documentos(lista_diccionarios)` nos permite añadir uno o varios documentos a la base de datos que se especifique en el código, los documentos que añadirá serán los que estén en la lista que hemos pasado como parámetro
2.  Luego está la función `actualizar_documentos(lista_diccionarios, datos_acutalizacion)`, la cual busca en la base de datos los documentos dentro de la lista que hemos pasado como argumento y por cada uno de ellos actualiza lo que le pasemos en `datos_actualizacion`
3. Para acabar esta la función `borrar_documentos(lista_diccionarios)` que borra todos los documentos que esten en la lista.

## **Esquema**
```python
{
	'_id': ObjectID(90823649081326749082136492304),
	'PricePack': String,
	'NamePack': String,
	'ContenPack': String,
	'HasCupon': Boolean,
	'HasParking': Boolean
}

$jsonSchema: {
            bsonType: "object",
            required: ["PricePack","NamePack","ContentPack","HasCupon","HasParking"],
            properties: {
                "_id":{},
                "PricePack":{
                    bsonType: "string",
                    description: "The price of the Pack"
                    //debe ser 0 (Free) o x (buy)
                },
                "NamePack":{
                    bsonType: "string",
                    description: "The name of the Pack"
                },
                "ContentPack":{
                    bsonType: "array",
                    items: {
                        bsonType:"object",
                        required: ["name"],
                        properties:{
                            name:{
                                bsonType:"string",
                                description: "este es el nombre del elemento del pack"
                            },
                            description:{
                                bsonType:"string",
                                description: "esta es la descrición del elemento"
                            }
                        }
                    }
                },
                "HasCupon":{
                    type:"boolean",
                    description:"Para saber si tiene o no descuento el pack"
                },
                "HasParking":{
                    bsonType:"bool",
                    description:"Para saber si el pack es solo para los que tienen parking"
                }
            }
        }
```
# ***Implementacion***
Aqui explicaremos las diferentes herramientas que se han utilizado para la creación del software, separa en BackEnd, FrontEnd y General:
- **BackEnd**
	- MongoAtlas: Servicio que nos permite tener bases de datos en la nube
	- Python: Lenguaje de programacion con el que se ha programado todo el programa
	- Modulo de python: Hemos usado diversos modulos que nos facilitaban ciertas tareas:
		- pymongo: Nos permite realizar la conexion a la base de datos y trabajar con los datos que haya dentro
		- certifi: Necesario para conectarse con la base de datos de manera correcta
		- os: Nos permite trabajar con directorios
		- shutil: Necesario para copiar archivos de una carpeta a otra 
- **FrontEnd**
	- Hugo: Es un generador de sitios estaticos en cual utilizamos para poder visualizar los documentos makrdown
- **General**
	- VSCode: Editor de texto en el cual hemos programado todo el codigo
	- Git: Control de versiones
# ***Pruebas***
## **Accesso a datos**
Con las funciones de acceso a datos no hemos realizado muchas pruebas.

- `obtener_cluster(uri)`. Hemos comprobado que una vez dentro de un cluster nuestro esté una BBDD especifica.
```python
ruta = "mongodb+srv://m001-student:12345@sandbox.glkvp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
cluster = obtener_cluster(ruta)
assert "amenities" in cluster.list_database_names()
```

- `obtener_bd(cluster, bd)`. Hemos comprobado que dentro de una BBDD nuestra esté una coleccion especifica.
```python
ruta = "mongodb+srv://m001-student:12345@sandbox.glkvp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
cluster = MongoClient(ruta)
db = cluster["amenities"]
assert "packs2" in db.list_collection_names()
```
## **Logica**
`obtener_documentos(coleccion, filtro)`. 
La funcion a partir de una coleccion llena de documentos busca solo los documentos que concuerdan con el filtro.
1. Creamos una coleccion usando las funciones que hemos creado.
2. Creamos un filtro, un diccionario, en base a dos valores llamados `clave_filtro`, `valor_filtro`.
3. Despues utilizando la funcion que está siendo testeada obtenemos una lista de diccionarios
4. Por ultio comprobamos que cada diccionario dentro de esta lista tenga de clave-valor los que le hemos pasado.
```python
cluster = obtener_cluster(
	"mongodb+srv://matias:12345@proyecto.bjagm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
)
db = obtener_bd(cluster, "prueba")
coleccion = obtener_coleccion(db, "prueba")

clave_filtro = "r"
valor_filtro = 125

filtro = {clave_filtro: valor_filtro}

lista_docs = obtener_documentos(coleccion, filtro)

for doc in lista_docs:
	assert doc[clave_filtro] == valor_filtro
```
Otro test es comprobar que sucede cuando el filtro esta vacio.
1. Lo unico diferente es cuando utilizamos la funcion de obtener documentos, a está le pasamos un diccionario vacio, por lo que debería volver todos los documentos dentro de una coleccion.
2. Despues comprobamos que la cantidad de documentos dentro de la lista sea la misma que los que hay en la coleccion.
```python
cluster = obtener_cluster(
	"mongodb+srv://matias:12345@proyecto.bjagm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
)
db = obtener_bd(cluster, "prueba")
coleccion = obtener_coleccion(db, "prueba")

numero_documentos = coleccion.count_documents({})

filtro = {}

lista_docs = obtener_documentos(coleccion, filtro)

assert numero_documentos == len(lista_docs)
```
`obtener_texto_para_markdown(lista_documentos)`.
La funcion crea a partir de una lista de diccionarios un string. En este test solo hay una prueba.
1. Primero creamos una lista de diccionarios
2. Despues el texto que deberia dar una vez llamada a la funcion
3.  Por ultimo comprobamos que utilizando la funcion pasando la lista de diccionarios devuelva exactamente el texto que hemos creado

```python
lista_documentos = [
	{
		"_id": {"$oid": "619a9b91a2b4bbbb8e69bc60"},
		"PricePack": "Free",
		"NamePack": "Free Pack",
		"ContentPack": "This pack includes a bag full of sweets",
		"HasCupon": False,
		"HasParking": False,
	},
	{
		"_id": {"$oid": "619a9b92a2b4bbbb8e69bc61"},
		"PricePack": "5€",
		"NamePack": "Tier 1 Pack",
		"ContentPack": "this low-priced pack includes a bag of sweets plus an organized hotel welcome ",
		"HasCupon": False,
		"HasParking": False,
	},
]

texto_resultante = "# Free Pack\n\nThis pack includes a bag full of sweets\n\nEl precio de este pack es: Free\n\n_Cupon_ ❌\n\n_Parking_ ❌\n\n# Tier 1 Pack\n\nthis low-priced pack includes a bag of sweets plus an organized hotel welcome \n\nEl precio de este pack es: 5€\n\n_Cupon_ ❌\n\n_Parking_ ❌\n\n"

assert obtener_texto_para_markdown(lista_documentos) == texto_resultante
```
`crear_nombre_archivo(filtro)`.
Esta función a partir de un diccionario devuelve un string. En el primer test hay 3 subtest que comprueban lo mismo.
1. Creamos un filtro para pasarle a la funcion
2. Y llamamos a la funcion con este filtro comrobando sea igual a una string que creamos en el test
```python
filtro = {"a": 1}
assert crear_nombre_archivo(filtro) == "a1"

filtro = {"a": 1, "b": "alohomora"}
assert crear_nombre_archivo(filtro) == "a1balohomora"

filtro = {"a": 1, "b": "alohomora", "c": [1, 2, 3]}
assert crear_nombre_archivo(filtro) == "a1balohomorac[1, 2, 3]"
```
`crear_archivos_markdown(texto, nombre)`.
Esta crea archivos markdown a partir de dos strings, la primera el texto que será escrito dentro del archivo y la segunda el nombre del archivo. En esta funcion hay varios test. El primero comprobamos si funciona pasando parametros normales.
1. Primero creamos dos strings para pasarle a la funcion
2. Depues llamamos a la funcion pasado estos strings
3. Luego creamos una ruta en la cual está el archivo recien creado y comprobamos si ese arhivo existe
4. A continuacion abrimos el arhivo en python
5. Creamos un acumulado y guardamos dentro cada linea del archivo
6. Para finalizar comprobamos que el acumulador sea exactamente igual al texto que le pasamos al inicio
```python
texto = "texto1"
nombre = "nombre1"

crear_archivos_markdown(texto, nombre)

ruta_archivo = "./markdowns/" + nombre + ".md"

assert path.isfile(ruta_archivo)

archivo = open(ruta_archivo, "r")

acu = ""
for linea in archivo.readlines():
	acu += linea
	
assert texto == acu
```
El segundo test comprueba que sucede cuando el filtro texto esta vacio. En este test se reutiliza el mismo codigo que en test anterior, ademas de una linea la cual utiliza la funcion `getsize`. En esta linea comprobamos que el tamaño del archivo que hemos creado sea 0.
```python
texto = ""
nombre = "nombre2"

crear_archivos_markdown(texto, nombre)

ruta_archivo = "./markdowns/" + nombre + ".md"

assert path.isfile(ruta_archivo)

archivo = open(ruta_archivo, "r")

acu = ""
for linea in archivo.readlines():
	acu += linea

assert texto == acu
assert path.getsize(ruta_archivo) == 0
 ```
El ultimo test comprueba que sucede cuando el nombre esta vacio. Al igual que el anterior el codigo es practicamente el mismo que el primero, con la unica diferencia de que al crear la variable `ruta_archivo`, en vez de poner la variable nombre, pone `default`, que es el nombre que le hemos puesto por defecto a la funcion.
```python
texto = "texto2"
nombre = ""

crear_archivos_markdown(texto, nombre)

ruta_archivo = "./markdowns/" + "default" + ".md"

assert path.isfile(ruta_archivo)

archivo = open(ruta_archivo, "r")

acu = ""
for linea in archivo.readlines():
	acu += linea
	
assert texto == acu
```
`mover_markdowns(ruta_destino)`.
Este modulo copia todos los archivos dentro de la carpeta `markdown`, carpeta que hemos creado en el otro modulo, dentro de la carpeta en `ruta_destino`. Solo hay un test que comprueba que funcione.
1. Especicamos la carpeta donde estan los archivos markdown.
2. Despues guardamos la ruta de donde copiaremos los archivos.
3. Llamaremos a la funcion pasandole la `ruta_destino`.
4. Para finalizar, comprobamos que en la `ruta_destino` hayan la misma cantidad de archivos que en la `ruta_origen`
```python
ruta_origen = "./markdowns"
ruta_destino = "./logica/test/carpeta_de_prueba/"

mover_markdowns(ruta_destino)

assert len(listdir(ruta_origen)) == len(listdir(ruta_destino))
```



# ***Clockify***

## **Estimación inicial**

![](https://i.imgur.com/ArsMBZR.png)

## **Estimación real -> clockify**

- **Programación:** en la parte de programación estimamos emplear alrededor de 40 horas de trabajo, pero al final fueron menos de las horas estimadas.
- **Hugo:** en hugo nos paso lo contrario, estimamos unas 10 horas, pero al final fueron muchas más, debido a que la tecnología era compleja y nueva para nosotros.
- **BBDD:** con base de datos, estimamos unas 15 horas, ya que pensabamos que nos sería mas complicado de lo que realmente fue

## **Comparación temporal**

![](https://i.imgur.com/8DgV41Y.png)


# ***Dificultades***

El principal problema que tuvimos al momento de llevar a cabo el proyecto fue usar *HUGO*, ya que era una nueva tecnología y por más que miramos muchas guías y tutoriales, no nos dió el tiempo necesario para poder implementar muchas de las funcionalidades que nos ofrece.

Otro cosa que nos contrajo dificultad, fue implementar casos test en el proyecto. Pero al final pudimos implementar algunos test que se nos ocurrió.


# ***Futuras mejoras***

Para poder mejorar nuestro proyecto, teniamos en mente implementar que las funciones CRUD se puedan llevar a cabo de una forma más sencilla para el usuario. También podriamos mejorar el aspecto de la página web de **Hugo**, refactorizar un poco más el código y implementar más casos test.