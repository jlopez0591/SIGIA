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
