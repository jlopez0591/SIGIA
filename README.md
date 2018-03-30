# Plataforma SIGIA para la Universidad de Panama

El sistema de gestion de informacion academica/administrativa (SIGIA) es una plataforma la cual 
pretende proveer un conjunto de aplicaciones para agilizar y facilitar varias de las acciones que se
realizan dentro de las unidades academicas de la universidad.

Entre las utiliades que se proponen manejar son las siguientes:

1. Inventario: Inventario de equipo y aulas de las facultades.
2. Estudiantes: Perfiles de los estudiantes, anteproyectos y proyectos de graduacion.
3. Profesores: Perfiles de los profesores y actividades de los mismos.

# Requerimientos

1. PostgreSQL 9.5.2
1. Nginx
1. Python 3.5.2
1. Django 1.11.8
1. Python-Pip3
2. Pipenv 

# Configuracion inicial
## Configuracion de Postgresql
```
postgres=#  sudo -u postgres psql
postgres=#  CREATE DATABASE sigia;
postgres=#  CREATE USER sigia_user WITH PASSWORD 'password';
postgres=#  ALTER ROLE sigia_user SET client_encoding TO 'utf8';
postgres=#  ALTER ROLE sigia_user SET timezone TO 'UTC';
postgres=#  ALTER ROLE sigia_user SET default_transaction_isolation TO 'read committed';
postgres=#  GRANT ALL PRIVILEGES ON DATABASE sigia TO sigia_user;
postgres=#  \q
```


## Instalacion de paquetes

```
$ pipenv install

```
## Comandos manage.py
```
$ ./manage.py makemigrations
$ ./manage.py migrate
$ ./manage.py cargar_grupos
$ ./manage.py cargar_ubicaciones
$ ./manage.py cargar_usuarios
$ ./manage.py cargar_estudiantes
