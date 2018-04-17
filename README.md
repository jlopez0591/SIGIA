# Plataforma SIGIA para la Universidad de Panama

El sistema de gestion de informacion academica/administrativa (SIGIA) es una plataforma la cual 
pretende proveer un conjunto de aplicaciones para agilizar y facilitar varias de las acciones que se
realizan dentro de las unidades academicas de la universidad.

Entre las utilidades que se proponen manejar son las siguientes:

1. Inventario: Inventario de equipo y aulas de las facultades.
2. Estudiantes: Perfiles de los estudiantes, anteproyectos y proyectos de graduacion.
3. Profesores: Perfiles de los profesores y actividades de los mismos.

Como beneficio para los usuarios del sistema, los administrativos de los distintos departamentos
podran descargar reportes de sus respectivas unidades academicas en formato .xlsx (Excel)

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

Una vez realizadas las instalaciones anteriores se deben ejecutar los siguientes comandos en el orden indicado
esto es para crear las migraciones y cargar datos de prueba, en caso de que estos sean necesarios.

```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py cargar_grupos
$ python manage.py loaddata ubicacion/fixtures/ubicacion.json # Opcional pruebas
$ python manage.py cargar_ubicaciones
$ python manage.py cargar_demo # Opcional
$ python manage.py cargar_usuarios
$ python manage.py cargar_estudiantes
```

