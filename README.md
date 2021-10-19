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

