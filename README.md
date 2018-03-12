# Plataforma SIGIA para la Universidad de Panama

El sistema de gestion de informacion academica/administrativa (SIGIA) es una plataforma la cual 
pretende proveer un conjunto de aplicaciones para agilizar y facilitar varias de las acciones que se
realizan dentro de las unidades academicas de la universidad.

# Requerimientos

1. PostgreSQL 9.5.2
1. Nginx
1. Python 3.5.2
1. Django 1.11.8
1. Python-Pip3
2. Pipenv 

# Configuracion inicial
## Configuracion de Postgresql
1. sudo -u postgres psql
1. CREATE DATABASE sigia;
1. CREATE USER sigia_user WITH PASSWORD 'password';
1. ALTER ROLE sigia_user SET client_encoding TO 'utf8';
1. ALTER ROLE sigia_user SET timezone TO 'UTC';
1. ALTER ROLE sigia_user SET default_transaction_isolation TO 'read committed';
1. GRANT ALL PRIVILEGES ON DATABASE sigia TO sigia_user;
1. \q

## Instalacion de paquetes
1. pipenv install

## Comandos manage.py
1. makemigrations
1. migrate
1. crear_grupos
1. createsuperuser (Seguir los pasos que aparecen en la consola)

#### Views
1. Include list unapproved activities view.
1. Include rejected activities view.
1. Include rejected anteproyecto view.
1. Terminar las plantillas.
1. Terminar los metodos de django-autocomplete-light
1. Agregar graficas de unidades
1. Generar reportes personalizados (Utilizando la reportlab o weasyprint o wkhtmltopdf)
1. Implementar documentacion con sphinx

### Cron Jobs
Entre los cron jobs que se utilizaran para mantener actualizado los datos se utilizaran los siguientes comandos administrativos
1. cargar_ubicaciones
1. cargar_estudiantes

# To-Do - Durante pruebas
1. Restringir el acceso a vistas
1. Completar la asignacion de permisos
