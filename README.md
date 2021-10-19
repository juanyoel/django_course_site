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
