import csv
import json
import logging
import os.path
import sys

from datetime import datetime as dt
from xkcdpass import xkcd_password as xp

from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group

from sigia import base_settings
from perfiles.models import Perfil

fecha = dt.now()
ARCHIVO = '{}{}'.format(base_settings.BASE_DIR, '/test_data/usuarios.json')
LOG_LOCATION = '{}/{}/{}'.format(base_settings.BASE_DIR,
                                 'logs/usuarios/', fecha.strftime("%Y-%m-%d"))
LOG_FILE = '{}/{}'.format(LOG_LOCATION, fecha.strftime("%X"))
URL = ''

GRUPOS = {
    1: 'Profesores',
    2: 'Director De Departamento',
    3: 'Director de Escuela',
    4: 'Administrativos',
    5: 'Comision de Anteproyecto',
    6: 'Decanos'
}

if not os.path.exists(LOG_LOCATION):
    os.makedirs(LOG_LOCATION)

logging.basicConfig(filename='creacion_{}.log'.format(LOG_FILE), level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def cargar_usuarios(usuarios_dict):
    """Utiliza el archivo provisto para la carga de usuarios
    
    Arguments:
        usuarios_dict {string} -- [path al archivo a utilizar]
    
    Returns:
        [dict] -- [Datos de los usuarios a ser registrados]
    """

    with open(ARCHIVO, 'r') as f:
        data = json.load(f)
    return data


def cargar_webservice(url):
    return {'valor': 'Empty'}


def generar_username(nombre: str, apellido: str, codigo: str):
    return '{}{}{}'.format(nombre[0], apellido, codigo)


class Command(BaseCommand):
    help = 'Carga usuarios iniciales'

    def handle(self, *args, **options):
        usuarios_creados = dict() # Listado de usuarios creados en la corrida
        wordfile = xp.locate_wordfile() # Inicializacion de xkcdpass
        words = xp.generate_wordlist(wordfile=wordfile, min_length=5, max_length=5) # Iniciar el listado para xkcdpass

        # Carga de Datos
        if base_settings.DEBUG is True:
            datos = cargar_usuarios(ARCHIVO) # Utiliza el archivo local
        else:
            datos = cargar_webservice(URL) # Utiliza webservice provisto

        # Procedimientos
        for i, row in enumerate(datos):
            try:
                # Crear usuario
                ds = row['info_perfil']
                primer_nombre = ds['primer_nombre']
                primer_apellido = ds['primer_apellido']
                codigo_profesor = ds['cod_profesor']
                user_name = generar_username(primer_nombre[0], primer_apellido, codigo_profesor)
                passcode = xp.generate_xkcdpassword(words, acrostic="troll", delimiter="-", numwords=2)
                u, created = User.objects.get_or_create(
                    username=user_name, first_name=primer_nombre, last_name=primer_apellido)
                if created:
                    u.set_password(passcode)
                    u.save()
                    usuarios_creados.update({i: {'usuario': user_name, 'password': passcode}})
                    # Agregar a grupos
                    grupos = row['grupos'].split()
                    for grupo in grupos:
                        try:
                            g = Group.objects.get(name=grupo)
                            u.groups.add(g)
                            logging.info('Usuario agregado {} al grupo: {}'.format(u.user_name, g.name))
                        except ObjectDoesNotExist as exc:
                            logging.error(exc)
                    # Crear perfil
                    ds['fecha_nacimiento'] = dt.strptime(ds['fecha_nacimiento'], '%Y-%m-%d').date()
                    Perfil.objects.update_or_create(usuario=u, defaults=ds)
            except:
                print("Error")
        
        # Guardar la carga actual.
        with open(USER_CSV, 'a') as uc:
            w = csv.DictWriter(uc, usuarios_creados.keys())
            w.writeheader()
            w.writerow(usuarios_creados)
