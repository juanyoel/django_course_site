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


