# django_course_site


## Notas Generales:
* Para crear un proyecto Django se utiliza el comando **django-admin startproject [nombre_del_proyecto]**.
* Los archivos asgi.py y wsgi.py están relacionados con el despliegue de la aplicación.
* El archivo settings.py es utilizado para las configuraciones generales del proyecto. 
* El archivo urls.py es utilizado para controlar las rutas, las urls del proyecto.


## Notas Configuración:
* Los proyectos son las combinaciones y relaciones de uno o varias apps (módulos) en los que se separa la lógica del proyecto. Para crear una nueva app dentro del proyecto se utiliza el comando **python manage.py startapp [nombre_de_app]**.


## Notas de app:
* El archivo views.py es utilizado para codificar las acciones que se realizan en dependencia de la url a la que accede el usuario. Básicamente es dónde se escribe la lógica del proyecto. En su forma más siemple lo que se registra en las views.py son funciones python.
* Cuando creamos una nueva app, debemos adicionarle el archivo urls.py dónde se registran las urls relacionadas directamente con el módulo (app).
* En el archivo urls.py que creamos vamos a crear un arreglo que debe llamarse obligatoriamente urlpatterns, debido a que es el nombre que django va a buscar, en el registramos las urls del módulo.
* Importar en el archivo anterior **from django.urls import path**, **from . import views**
* Debemos adicionar las apps que creamos al archivo settings.py dónde dice **INSTALED_APPS**.
* Luego debemos conectar la url de la app con la url general del proyecto.
  - En el archivo urls.py del proyecto al **from django.urls import path, include** le adicionamos include.
  - Luego agregamos los nuevos path() --> path('', include('meetups.urls'))


## Levantar servidor de desarrollo
* Para utilizar el servidor de desarrollo utilizamos el comando **python manage.py runserver**

## Para hacer uso de los **templates**:
 * Creamos una carpeta llamada templates en la app.
 * Dentro de la carpeta anterior creamos una carpeta con el nombre de la app. Debido a un tema orgnizativo, ya que cuando django va a desplique recoge todos los templates en una sola carpeta, lo que puede provocar problemas si tenemos varios templates con el mismo nombre.
 * En el archivo views.py utilizaremos la funcion render en vez del HTTResponse como teníamos hasta el momento.
   - render(request, 'meetups/index.html') siempre se le pasa como primer parametro el objeto request y como segundo el camino relativo a la plantilla que se estará utilizando.
 * Los archivos .js, .css, imagenes y demás los organizamos en sus respectivas carpetas dentro de un directorio static que creamos en la app.
 * Para usar alguno de los archivos de las carpetas mencionadas anteriormente se utiliza el lenguaje de plantillas de django --> **<link rel="stylesheet" href="{% static 'meetups/styles/base.css'%}">** ejemplo para utilizar un css.
 * En la views.py al método render se le pasa como parámetro un tercer argumento que será dónde se envia la data a mostrar en la vista, por ejemplo --> **return render(request, 'meetups/index.html', {
        'meetups': meetups
    })**, donde meetups en este ejemplo sería --> meetups = [
        {'title': 'A First Meetup'},
        {'title': 'A Second Meetup'}
    ]
 *  En la vista (html) podemos usar entonces esta data de la siguiente forma /n:
    ![image](https://user-images.githubusercontent.com/84333525/137948872-57954536-7c0f-45a7-942a-e6435425caee.png)
    - Nota: en este caso solo estamos accediendo al primer objeto del diccionario, pero es solo con fines demostrativos.
    - Lo correcto es iterar sobre todos los objetos del diccionario para mostrar sus datos en la vista.
 *  Ejemplo de condicional if en el lenguaje de plantillas de django /n: 
    ![image](https://user-images.githubusercontent.com/84333525/137949596-d7089337-5970-4820-ae67-d2523ef8cac5.png)
 *  Ejemplo de como sería un for /n:
    ![image](https://user-images.githubusercontent.com/84333525/137950834-a56dce88-f57a-429e-80c4-6979c99cde55.png)

## Crear una view con un parámetro dinámico:
* Crear la función en el archivo views.py, recordar que se le debe pasar como primer parametro el request, como segundo y obligatorio el parámetro que se va utilizar como identificador.
* Crear el archivo .html que se va a renderizar en la función.
* Agregar la nueva url por la cuál se va a llamar la view. Tener en cuenta que los parámetros dinámicos para conformar la url van entre brackets <> como en el siguiente ejemplo /n:
![image](https://user-images.githubusercontent.com/84333525/137972481-e78edca4-1dcd-43c4-a4fa-5d3f28649305.png)
* No se modifican las urls generales del proyecto porque ya estas fueron adicionadas.
* Cuándo se va a generar un link dinámico, o sea el que va a llamar a la url dinámica se usa {% url 'nombre de la vista que se va a llamar' %} porque de esta manera si necesitamos cambiar en un momento determinado la url sólo se cambiaría en un solo lugar ejemplo: /n
  ![image](https://user-images.githubusercontent.com/84333525/137982854-e130e6a5-6ca0-4940-9570-f31a117da8b9.png)
el tercer parametro sería la propiedad por la cual se va identificar el objeto para realizar las operaciones pertinentes.


## Herencia de código en las plantillas *(Creación de una plantilla base)* que contiene el código base que se hereda a todas las demás:
* Crear el directorio que contendrá la(s) plantillas base, generalmente debería tener este mismo nombre.
* En la plantilla base las secciones que las plantillas hijas van a sobrescribir se encierran entre bloques con la palabra clave block ejemplo:
  ![image](https://user-images.githubusercontent.com/84333525/138098393-aa9cb462-106a-46db-a0ba-7c30df03cb70.png)
* En la página hija se debe incluir el código que le indica de que plantilla estará heredando, ejemplo: 
  ![image](https://user-images.githubusercontent.com/84333525/138099424-dceaf678-f7b0-45f7-8563-2093182a36a5.png)


## Reutilización de código (partials):
* Se pueden escribir códigos reutilizables, a los que se le llaman partials o includes. Es el código que podemos utilizar independientemente de la página en la que estemos como por ejemplo la estructura de una lista.
* Creamos una carpeta para estos recursos, naturalmente le ponemos de nombre includes.
* Para incluir una porción de código utilizamos la palabra reservada include, ejemplo:
  ![image](https://user-images.githubusercontent.com/84333525/138113484-f1d23344-6664-4c1f-ab54-4eda8ef5c3de.png)


## DATA:
![image](https://user-images.githubusercontent.com/84333525/138116436-5fc58dc4-132c-4244-9830-a7b1052e8636.png)


* En Django no necesitamos conocer el lenguaje sql para interactuar con la BD, nos brinda una serie de herramientas que nos posibilita interactuar con la BD de forma sencilla.
* Para ser precisos esto se definen en los modelos:
 - Son clases representaciones de los datos que se estarán manejando en la aplicación.
 - Automáticamente para cada modelo Djando creará una tabla en la BD.
* Los modelos se definen en el archivo model.py de la app.
* Creamos la clase del modelo que se requiera y siempre se le debe pasar como parámetro *models.Model* que es lo que nos da acceso a las métodos necesarios para interactuar con la BD, ejemplo:
  ![image](https://user-images.githubusercontent.com/84333525/138118125-3863810f-9fec-4c39-9597-9ea6365b6053.png)
* Ejemplo de modelo:
  ![image](https://user-images.githubusercontent.com/84333525/138123005-d653a7e5-7f84-45d1-8f1b-64be8a742c06.png)
  - Para texto pequeños utilizamos *CharField()* definiendole la cantidad de caracteres que puede admitir el campo.
  - En la foto anterior el campo slug es de tipo *SlugField()* y lo marcamos como único, recordar que slug es similar a un id o algo así, es un código único que se utiliza para identificar un elemento pero de una forma que sea entendible para los humanos, por ejemplo, cuando escogemos un meetup de este proyecto, nos redirecciona a una nueva página, e identificamos a que meetup se está haciendo referencia mediante la propiedad slug del objeto en cuestión.

## Crear BD:
* Luego de ya tener los modelos necesarios o al menos parte de ellos que vamos a estar utilizando, debemos crear la BD.
* Para crear la BD debemos correr el siguiente código --> *python manage.py makemigrations*
  - Lo cual en este caso dará como resultado la creación de la migración de los modelos que se hayan definidos teniendo como resultado algo como el siguiente ejemplo:
    ![image](https://user-images.githubusercontent.com/84333525/138124517-6290dfee-88e1-4344-885e-19d1a379338f.png)
    
* Luego de tener creada la migración y verificar que se ha creado correctamente con los elementos necesarios, que dicho sea de paso las migraciones se guardan en la carpeta migrations de la app, pasamos a correr la migración con el siguiente código:
- *python manage.py migrate*
- Este comando es el encargado de correr la migración en la BD.

## Admin Area:
* A la administración del proyecto Django se accede a través de la url */admin*.
* Para poder acceder a este panel de administración debemos correr el siguiente comando:
  - python manage.py createsuperuser
* Todos los modelos (Tablas en la BD) pueden ser administrados desde este panel, para ello hay que registrarlos en el archivo *admin.py* de la siguiente manera:
  ![image](https://user-images.githubusercontent.com/84333525/138150403-b0d74905-b632-4ae3-bb10-b9ecab47e3ef.png)

- Agregamos el modelo que queremos adicionar al panel de administración --> *from . models import Meetup*
- Luego lo registramos de la siguiente manera --> *admin.site.register(Meetup)*
* Luego ya podemos adicionar via admin panel un objeto del modelo deseado (Lo cual ya me permite modificar la vista *views.py* y utilizar data real).


## Obteniendo data real desde la BD:
* Primero importamos el modelo o modelos con los cuales deseo interactuar con la BD, de la siguiente forma --> *from .models import Meetup*
* Luego puedo interactuar con la BD mediante un método estático llamado *objects* que contiene todos los métodos para interactuar con la BD.
  - ![image](https://user-images.githubusercontent.com/84333525/138152147-25c993c6-459c-4b9e-94a0-25a870be1382.png)
* Para obtener un objeto específico y buscarlo por un parámetro utilizamos *objects.get(param)* ejemplo:
  - ![image](https://user-images.githubusercontent.com/84333525/138155478-f52254e5-3594-4faa-ba7e-8e8da366ce1b.png)


## Upload Imagenes al proyecto:
* Para adicionar un campo imagen al modelo que lo requiera usamos el tipo *ImageField()* como veremos en la siguiente actualización del modelo con el que estamos trabajando.
 - ![image](https://user-images.githubusercontent.com/84333525/138156425-fb10a72f-1a2f-474d-adf9-e4fc6627ade0.png)

* Además debemos modificar el archivo de administración y setear algunas variables para que Django sepa dónde va a guardar estas imágenes, porque las mismas no se guardan en la BD, las BD no están optimizadas para guardar imágenes, en cambio este campo que se le esta adicionado lo que hace es guardar una referencia a dónde está guardado.
  - ![image](https://user-images.githubusercontent.com/84333525/138157288-a4fc053e-7b35-47d7-8b3a-f3cd769ab07f.png)

  - Estas variables se setean para poder decirle a Django dónde va a guaradar esas imágenes.
  - Para poder trabajar con imágenes se necesita instalar una librería externa que usa Django para este trabajo llamada Pillow, para esto usamos el comando:
    *python -m pip install Pillow*
    
## Notas sobre el trabajo con imágenes.
* Si se quiere poder visualizar la imágen que se sube en el panel de administración hay que realizar algunas modificaciones a los archivos de configuración:
 -  ![image](https://user-images.githubusercontent.com/84333525/138160702-9658a28b-9c0b-44e4-903f-7f1109deb216.png)

* Además para visualizar las imágenes del objeto en cuestión en la vista de usuarios se deben adicionar algunas conf. como muestro en el siguiente ejemplo:
  - primero mediante interpolación le pongo el nombre que crea conveniente:
  ![image](https://user-images.githubusercontent.com/84333525/138163020-2686a27b-52b8-4a94-8280-2f94bf39438a.png)
  - el paso anterior es en caso de que el lugar desde dónde se llama la imagen sea un partials de otra página en caso contrario se haría como en el siguiente ejemplo y listo:
  ![image](https://user-images.githubusercontent.com/84333525/138163225-2ff1b86e-2764-4484-a08b-03a48ab95405.png)

## Notas sobre el sitio de administración y la representación de objetos de la BD en el mismo:
* Por defecto para mostrar los objetos en el sitio de la administración o si se imprimen a lo que se está invocando es al métos str() o sea a la representación como string de dicho objeto. Ejemplo de lo antes dicho:
 - ![image](https://user-images.githubusercontent.com/84333525/138164170-40c9232e-d9c6-4336-9bdf-ad186b16b187.png)

* Para cambiar lo anterior se debe reimplementar dicho método de la siguiente manera:
  ![image](https://user-images.githubusercontent.com/84333525/138164481-a208daee-6f2b-404f-a078-c249c70f2b7d.png)
* Lo que nos daría como resultado lo siguiente:
  ![image](https://user-images.githubusercontent.com/84333525/138164623-22368ea6-dad3-475c-ac6a-da83a4f7917d.png)

* ** Si se quiere incluso dar más detalles y configurar los objetos en mayor profundidad podemos seguir los siguientes pasos **
* En el archivo *admin.py* puedes crear una clase que obligatoriamente tienes que pasarle como parámetro *admin.ModelAdmin* y dentro de la clase tiene varios atributos, uno de ellos es list_display, con el cual podemos configurar como se muestra nuestro objeto en el panel de administración, a continuación ejemplos:
 1. ![image](https://user-images.githubusercontent.com/84333525/138166102-332a397b-da5a-4969-8b7e-d993df2664c7.png)

  Primero adicionamos la clase y luego se la pasamos como segundo parámetro al *admin.site.register*
 2. Ejemplo de antes y después:
    Antes:
    ![image](https://user-images.githubusercontent.com/84333525/138166373-a665712a-2788-474f-a7d0-e2c9f2788869.png)

    Después:
    ![image](https://user-images.githubusercontent.com/84333525/138166490-a8db1376-9a71-402d-a75b-3c15a831428b.png)

* Además le podemos adicionar por dónde filtrar y muchísimas más features:
  ![image](https://user-images.githubusercontent.com/84333525/138167032-8514ca29-7d7d-4554-b466-06967f5bd996.png)
  ## Importante:
  * Recordemos que en este proyecto los objetos tienen un campo denominado slug, que no es más que una llave única de identificación que puede ser entendida por los humanos, Django tiene una feature muy buena que muestro a continuación con la cual, puedo autogenerar ese campo diciendole como debe ser creado:
  ![image](https://user-images.githubusercontent.com/84333525/138167649-82071f80-a475-4d4b-be1d-62944e6e3034.png)
- En este caso el campo señalado fue autogenerado al adicionar un nuevo Meetup y darle un título
  ![image](https://user-images.githubusercontent.com/84333525/138167909-46689281-9685-4b33-84d8-9e1096ac85e0.png)


## Relaciones entre tablas de las BD:
![image](https://user-images.githubusercontent.com/84333525/138204807-951e07cd-a3eb-4b4e-8f60-9805f04a84d5.png)

* ****Uno a mucho****:
* En este caso veremos la relación uno a muchos, debido a que un Meetup solo puede tener una locación, pero en una misma locación puede haber muchos meetups.
* Para ello agregamos al modelo del meetup la llave foranea de la locación como veremos en el próximo ejemplo:

![image](https://user-images.githubusercontent.com/84333525/138205224-0c2a27cb-67ac-4ea1-89d6-012cdbd24faa.png)

* Tendremos en cuenta que si una locación es eliminada de la BD entonces se eliminará el meetup que tenga asociado, para ello agregamos otro argumento como veremos en la próxima imagen:

![image](https://user-images.githubusercontent.com/84333525/138205458-4127e507-bb02-4638-bd1e-374d5d5c4b73.png)

* Podemos tener en cuenta que esta no es la única opción para cuando eliminamod un elemento, también podriamos setearlo a null, entre otros.

* ***** Mucho a mucho*****:
 Para demostrar las relaciones mucho a mucho en este caso adicionamos un nuevo model *participantes* debido a que un meetup puede tener muchos participantes y a su vez los participantes pueden estar en muchos meetups.
 * Para ello adicionamos al modelo Meetup el campo participantes que va a ser de tipo *ManyToManyField(Participant)* dónde le pasamos como parámetro el mdelo con el cual tiene la relación como veremos en la imagen siguiente:
  ![image](https://user-images.githubusercontent.com/84333525/138207118-5d3d512a-7ded-404a-be2e-d43ab571bc28.png)
  
  * Podemos tener en cuenta que esto lo podemos hacer en cualquiera de los dos modelos.
  * Django lo que hace es crear una tabla extra con los ids de ambos modelos, para decirle a Django que inicialmente puede no tener ninguna relación adicionamos un argumento más a la declaración de la relación como vemos en la próxima imagen:

  ![image](https://user-images.githubusercontent.com/84333525/138207483-811d2b72-a94e-4678-9fe6-8577d6c81ea1.png)

  Con este argumento *blank=TRUE* estamos permitiendo que el campo pueda ser *empty*
  
 * ## Nota importante: ##
   -  En el caso de los campos normales que definen a un modelo, en que le agregamos el parámetro *blak=True* deberíamos agregarle también el parámetro *null=True*:
   ![image](https://user-images.githubusercontent.com/84333525/138282279-7c5c2b56-8231-4ec6-9a98-efc4529b5f54.png)

  
## Trabajo con formularios: ##
* Podemos trabajar los formularios con las etiquetas *form* de siempre, pero convenientemente podemos usar las herramientas que nos proporciona Django para el trabajo con los formilarios.
* Agregamos un archivo *forms.py* a la app.
* A est archivo le agregamos el import forms y creamos una clase en que le pasamos form.ModelForm como parámetro para tener acceso a todos los features.
* Además importamos el modelo con el cual queremos vincular el formulario y creamos una nested class que es una feature de python como veremos en la siguiente imagen:
  ![image](https://user-images.githubusercontent.com/84333525/138292271-13edd49f-0822-4b47-a9d7-b5fa1d06e345.png)
de esta forma tenemos vinculado un modelo a un formulario específico.
* Además podemos restringir los campos que le creamos al formulario de la siguiente manera, estos son los que debe mostrar:
![image](https://user-images.githubusercontent.com/84333525/138292829-5c2e273f-1fdf-4c93-a9ec-bdbcc1e14e5a.png)

* Luego debemos vincular el formulario a la vista, para ello debemos modificar el archivo view.py con los siguientes parámetros:
 - Primero importamos el formulario desde el archivo *forms.py*
 - Segundo crear la variable en la vista que renderiza el formulario e iniciar la clase del formulario como veremos en la imagen
 - Tercero se le pasa esos valores en una nueva clave del diccionario que se retorna en la vista.
 - Ya estando en la vista debemos invocar al formulario mediante la clave que decidimos ponerle en el diccionario como veremos también en las imagenes de ejemplo.
 
 Imagenes:
  - ![image](https://user-images.githubusercontent.com/84333525/138459678-ca0a3616-4cc5-46e7-a90b-94cf12455b20.png)
  - ![image](https://user-images.githubusercontent.com/84333525/138459819-d5990a3b-ad1d-41de-a0c9-cd2c396b5b25.png)
  - ![image](https://user-images.githubusercontent.com/84333525/138459898-f0515450-63b7-4784-962a-dcffbfdaae23.png)

* Cuándo queremos hacer una petición desde un formulario como en ejemplo que necesitamos guardar la información del participante y para ello debemos enviar la información, debemos agregar las propiedas *actions* y *method* especificando el tipo de request que se va hacer.

![image](https://user-images.githubusercontent.com/84333525/138461521-c2cc8d66-9b41-47e1-b719-17581a7ba1cb.png)

* En caso de que queremos redireccionar a otra página el código se pondría en la propiedad *actions* como veremos en el ejemplo. Para este ejemplo queremos quedarnos en la misma página por si tenemos algún error.
  
  - ![image](https://user-images.githubusercontent.com/84333525/138462154-d65b9933-e1c4-4f9f-a2a5-5c7585ddbf21.png)

* Para dar seguridad a la información y protegernos específicamente contra ataques de tipo CSRF podemos utilizar las etiquetas convenientes para ello como veremos en el siguiente ejemplo:

  - ![image](https://user-images.githubusercontent.com/84333525/138462689-16418baf-b6e9-426e-ae9c-87f21663e0d6.png)

* Hasta el momento no habíamos manejado el tipo de las peticiones o request, para el caso que estamos analizando simplemente podemos poner una condicional como muestro a continuación:
 - ![image](https://user-images.githubusercontent.com/84333525/138463786-268b94a8-839c-4eb1-9b84-987f04d32ed1.png)

* Luego ya estamos en condiciones de poder guardar al participante como lo veremos en la siguiente imagen. Es importante guardar el retorno de la consulta para guaradar en la BD.
  - ![image](https://user-images.githubusercontent.com/84333525/138464693-b6c1112b-8753-46fb-aa90-a37c5fac210c.png)

* Como tenemos una relación mucho a mucho, tenemos que tener en cuenta que si agregamos un participante *Participant* tenemos que actualizar también el Meetup.
 - O sea recordar que en el modelo Meetup tenemos un campo que hace referencia al modelo Participant, por lo que si adicionamos un participante tenemos que agregarlo al modelo también :( --> **** ojo que no entendí bien la cosa ****

  - ![image](https://user-images.githubusercontent.com/84333525/138465991-73460823-5bdb-4fce-b410-14566bf789d5.png)

  - ![image](https://user-images.githubusercontent.com/84333525/138466102-da0eadae-0bec-4361-82a1-d0a12e520a28.png)
* En las palabras de instructor that's to add new related record

## Creamos una nueva página de confirmación:
* Válido para creación de cualquier otro tipo de página el subtitulo es sólo para guirarme en el ejemplo:
  - Creamos la vista UI, en este caso se le puso de nobre registration_succedd.html.
  - Luego debemos crear la función en el archivo *views.py* que va a renderizar esa vista y manejará la información debida.
  - Luego en el archivo *urls.py* adicionar el nuevo path.
  - Tener en cuenta que las urls como estas que no son dinámicas deben ir encima de las que si lo son, para evitar que Django intente matchear las url: (ver ejemplo)
  - Para redireccionar a la nueva página, sólo debemos importar *redirect* como veremos en la imagen, y llamar al método redirect pasandole como argumento la página a la que de be redireccionar y es todo.
  
-   ![image](https://user-images.githubusercontent.com/84333525/138470576-19a5fd6c-e1f3-454b-8f2c-64347001ccb9.png)
-   ![image](https://user-images.githubusercontent.com/84333525/138470639-965dee7d-07af-44e7-b0af-1fed12067481.png)
-   ![image](https://user-images.githubusercontent.com/84333525/138470739-d04d1ccc-4fe0-4690-8adb-a0b234d0df19.png)
-   ![image](https://user-images.githubusercontent.com/84333525/138470820-0ba95d34-534d-4e8e-b415-2e4ac86c7702.png)

## **//Interesante//
En el ejemplo del curso tenemos la siguiente situación curiosa
- ![image](https://user-images.githubusercontent.com/84333525/138474706-e4723c34-6b98-4d15-adea-fd605cf8c9fc.png)

Aquí estamos señalando el método con el que estamos guardando el participante en la BD, lo cuál no esta mal, pero nos causa un pequeño issue que pudiera que se me diera el caso en alguna situación, y es que como es un modelo de Participant lo que se esta creando, el mismo tiene como campo *email* el cual es único, lo que sucede es que un mismo participante debería poder registrarse en más de un Meetup, y ahí es dónde tenemos el problema, ya que al registrarse en uno, el correo ya existe en la BD y no le permite registrarse en otro porque le da error, para resolver eso seguimos los siguientes pasos:

![image](https://user-images.githubusercontent.com/84333525/138476003-8f99180f-5138-433e-bf67-68aa403a1a28.png)

*cleaned_data* este método del formulario nos permite acceder a la info que guarda un determinado campo del formulario
Se debe importar el módelo Participant para poder acceder a sus atributos, el método *get_or_create('argumento')* recibe como parámetro un argumento por el cuál buscará en la BD si existe y en caso contrario lo crea.

## Notas finales:
* Otra forma de trabajar con los formularios es heredar directamente de la clase Form, lo cual nos brinda muchas más posibilidades de validación, si lo hacemos así tenemos que tener en cuenta que tenemos que agregar los campos del formulario de forma manual
 - ![image](https://user-images.githubusercontent.com/84333525/138481528-90572054-48d2-4133-b8f9-e82e7f444b42.png)

* Otra nota final, es que hasta el momento cuando iniciamos el servidor, debemos escribir manualmente la url para que nos cargue la página principal, para corregir este problema, seguimos los siguientes pasos:
 1. En el archivo *urls.py* del proyecto hacemos la importación del RedirectView
    ![image](https://user-images.githubusercontent.com/84333525/138482009-4f2715a9-f9d0-4bb4-a988-e6e2e89dd6c3.png)

 2. En este mismo archivo haríamos los siguientes cambios:
    ![image](https://user-images.githubusercontent.com/84333525/138482544-1bc90fe4-12d7-4a41-bfa0-c5540a9191a1.png)

3. Por último modificaríamos el archivo *urls.py* de la app:
   ![image](https://user-images.githubusercontent.com/84333525/138482886-b9e33e4c-7564-477d-a49e-33a118fced4d.png)
