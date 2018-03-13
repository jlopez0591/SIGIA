from datetime import datetime as dt

import csv
import json
import logging
import os.path
import random
import string
import sys

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group

from sigia import base_settings
from perfiles.models import Perfil

fecha = dt.now()
ARCHIVO = '{}{}'.format(base_settings.BASE_DIR, '/test_data/usuarios.json')
LOG_LOCATION = '{}/{}/{}'.format(base_settings.BASE_DIR,
                                 'logs/usuarios/', fecha.strftime("%Y-%m-%d"))
LOG_FILE = '{}/{}'.format(LOG_LOCATION, fecha.strftime("%X"))
USER_CSV = ''
URL = ''

if not os.path.exists(LOG_LOCATION):
    os.makedirs(LOG_LOCATION)

logging.basicConfig(filename='creacion_{}.log'.format(LOG_FILE), level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    """
    Metodo para generar un password poco seguro
    :param size: Cantidad de caracteres del password
    :param chars: Conjunto de caracteres a utilizar
    :return: Password poco seguro
    """
    return ''.join(random.choice(chars) for _ in range(size))


def cargar_usuarios(usuarios_dict):
    # TODO: Agregar comentarios.
    with open(ARCHIVO, 'r') as f:
        data = json.load(f)
    return data


def cargar_webservice(url):
    return {'valor': 'Empty'}


def generar_username(nombre: str, apellido: str):
    return '{}{}'.format(nombre[0], apellido)


class Command(BaseCommand):
    help = 'Carga usuarios iniciales'

    def handle(self, *args, **options):
        usuarios_creados = dict()
        if base_settings.DEBUG is True:
            datos = cargar_usuarios(ARCHIVO)
        else:
            datos = cargar_webservice(URL)
        for i, row in enumerate(datos):
            try:
                ds = row['info_perfil']
                primer_nombre = ds['primer_nombre']
                primer_apellido = ds['primer_apellido']
                user_name = generar_username(primer_nombre[0], primer_apellido)
                passcode = id_generator()
                u, created = User.objects.get_or_create(
                    username=user_name, first_name=primer_nombre, last_name=primer_apellido)
                if created:
                    u.set_password(passcode)
                    u.save()
                    usuarios_creados.update({i: {'usuario': user_name, 'password': passcode}})

                    # TODO: Agregar a grupos
                    # TODO: Arreglar fecha
                    ds['fecha_nacimiento'] = dt.strptime(ds['fecha_nacimiento'], '%Y-%m-%d').date()
                    # TODO: Crear perfil
            except:
                print("Error")
            pass

        # Guardar la carga actual.
        with open(USER_CSV, 'a') as uc:
            w = csv.DictWriter(uc, usuarios_creados.keys())
            w.writeheader()
            w.writerow(usuarios_creados)

        # with open(ARCHIVO, 'r') as f:
        #     data = json.load(f)
        #     for i, row in enumerate(data):
        #         try:
        #             ds = row['info_perfil']
        #             user_name = '{}{}'.format(
        #                 ds['primer_nombre'][0], ds['primer_apellido'])
        #             # user_name = '{}{}{}{}'.format(ds['provincia'], ds['clase'], ds['tomo'], ds['folio']) # Removido para pruebas
        #             passcode = id_generator()
        #             u, created = User.objects.get_or_create(username=user_name, first_name=ds['primer_nombre'],
        #                                                     last_name=ds['primer_apellido'])
        #             if created:
        #                 u.set_password(passcode)
        #                 u.save()
        #                 result = 'Usuario {} creado con password {}'.format(
        #                     user_name, passcode)
        #                 logging.debug(result)
        #                 try:
        #                     g = Group.objects.get(name='Profesores')
        #                     u.groups.add(g)
        #                 except:
        #                     warning = 'Error al asignar grupo {} al usuario: {} - Error: {}'.format('Profesores', user_name,
        #                                                                                             sys.exc_info()[1])
        #                     logging.warning(warning)
        #                 try:
        #                     ds['fecha_nacimiento'] = dt.strptime(
        #                         ds['fecha_nacimiento'], '%Y-%m-%d').date()
        #                     Perfil.objects.update_or_create(
        #                         usuario=u, defaults=ds)
        #                     mensaje = 'Se agrego la informacion de perfil al usuario; {}'.format(
        #                         user_name)
        #                     logging.info(mensaje)
        #                 except:
        #                     warning = 'Hubo un error al agregar la informacion de perfil a: {}, error: {}'.format(
        #                         user_name,
        #                         sys.exc_info()[
        #                             1])
        #                     logging.warning(warning)
        #             else:
        #                 logging.debug('El usuario {} ya existe'.format(i))
        #         except:
        #             error = 'Hubo un error al crear al usuario: {}, error: {}'.format(
        #                 i, sys.exc_info()[1])
        #             logging.error(error)
