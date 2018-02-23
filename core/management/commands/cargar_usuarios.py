from datetime import datetime as dt

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
ARCHIVO = '{}{}'.format(base_settings.BASE_DIR, '/import-files/user.json')
LOG_LOCATION = '{}/{}'.format(base_settings.BASE_DIR, 'logs/creacion_usuarios/')
LOG_FILE = '{}/{}'.format(LOG_LOCATION, fecha.strftime("%Y-%m-%d"))

if not os.path.exists(LOG_FILE):
    os.makedirs(LOG_FILE)

logging.basicConfig(filename='{}.log'.format(LOG_FILE), level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    """
    Metodo para generar un password poco seguro
    :param size: Cantidad de caracteres del password
    :param chars: Conjunto de caracteres a utilizar
    :return: Password poco seguro
    """
    return ''.join(random.choice(chars) for _ in range(size))


def cargar_usuarios():
    """
    Carga lista de usuarios
    :return:
    """
    pass


def cargar_webservice(url):
    pass


class Command(BaseCommand):
    help = 'Carga usuarios iniciales'

    def handle(self, *args, **options):
        with open(ARCHIVO, 'r') as f:
            data = json.load(f)
            for i, row in enumerate(data):
                try:
                    ds = row['info_perfil']
                    user_name = '{}{}{}{}'.format(ds['provincia'], ds['clase'], ds['tomo'], ds['folio'])
                    passcode = id_generator()
                    u, created = User.objects.get_or_create(username=user_name, first_name=ds['primer_nombre'],
                                                            last_name=ds['primer_apellido'])
                    if created:
                        u.set_password(passcode)
                        u.save()
                        result = 'Usuario {} creado con password {}'.format(user_name, passcode)
                        logging.debug(result)
                        try:
                            for grupo in row['grupos']:
                                g = Group.objects.get(name=grupo.title())
                                u.groups.add(g)
                        except:
                            warning = 'Error al asignar grupo {} al usuario: {} - Error: {}'.format(grupo, user_name,
                                                                                                    sys.exc_info()[1])
                            logging.warning(warning)
                        try:
                            ds['fecha_nacimiento'] = dt.strptime(ds['fecha_nacimiento'], '%Y-%m-%d').date()
                            Perfil.objects.update_or_create(usuario=u, defaults=ds)
                            mensaje = 'Se agrego la informacion de perfil al usuario; {}'.format(user_name)
                            logging.info(mensaje)
                        except:
                            warning = 'Hubo un error al agregar la informacion de perfil a: {}, error: {}'.format(
                                user_name,
                                sys.exc_info()[
                                    1])
                            logging.warning(warning)
                    else:
                        logging.debug('El usuario {} ya existe'.format(i))
                except:
                    error = 'Hubo un error al crear al usuario: {}, error: {}'.format(i, sys.exc_info()[1])
                    logging.error(error)
