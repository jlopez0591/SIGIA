import datetime
import json
import logging
import os
import sys

from sigia import base_settings
from django.core.management.base import BaseCommand
from ubicacion.models import Sede, Unidad, Seccion, Carrera, UnidadInstancia, SeccionInstancia, CarreraInstancia

fecha = datetime.datetime.now().strftime("%Y-%m-%d")
ARCHIVO = '{}{}'.format(base_settings.BASE_DIR, 'logs/ubicacion.json/')
LOG_LOCATION = '{}/{}'.format(base_settings.BASE_DIR, 'logs/ubicacion/creacion')
LOG_FILE = '{}/{}'.format(LOG_LOCATION, fecha)

ESTATUS = {
    'A': True,
    'I': False
}

if not os.path.exists(LOG_FILE):
    os.makedirs(LOG_FILE)

logging.basicConfig(filename='{}.log'.format(LOG_FILE), level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class Command(BaseCommand):
    help = 'Carga y actualiza los datos de las ubicaciones'

    def handle(self, *args, **options):
        with open(ARCHIVO, 'r') as f:
            data = json.load(f)
            sedes = data['sedes']
            unidades = data['unidades']
            secciones = data['secciones']
            carreras = data['carreras']
            uni_ubc = data['uni_ubc']
            sec_ubc = data['sec_ubc']
            car_ubc = data['car_ubc']
        for sede in sedes:
            try:
                sede = apply_activo(sede)
                s, created = Sede.objects.update_or_create(cod_sede=sede['cod_sede'], defaults=sede)
                if created:
                    logging.info('Sede: {} creada'.format(sede['cod_sede']))
            except:
                logging.error('Sede: {}'.format(sede['cod_sede']))
        for unidad in unidades:
            try:
                unidad = apply_activo(unidad)
                u, created = Unidad.objects.update_or_create(cod_unidad=unidad['cod_unidad'], defaults=unidad)
                if created:
                    logging.info('Unidad: {} creada'.format(unidad['cod_unidad']))
            except:
                logging.error('Unidad: {}'.format(unidad['cod_unidad']))
        for seccion in secciones:
            try:
                seccion = apply_activo(seccion)
                s, created = Seccion.objects.update_or_create(cod_unidad=seccion['cod_unidad'],
                                                              cod_seccion=seccion['cod_seccion'], defaults=seccion)
                if created:
                    logging.info('Seccion {}{} creada'.format(seccion['cod_unidad'], seccion['cod_seccion']))
            except:
                logging.error('Seccion: {}{}'.format(seccion['cod_unidad'], seccion['cod_seccion']))
        # Carrera
        for carrera in carreras:
            pass
        # UnidadInstancia
        for unidad in uni_ubc:
            pass
        # SeccionInstancia
        for seccion in sec_ubc:
            pass
        # CarreraInstancia
        for carrera in car_ubc:
            pass


def apply_activo(data):
    """
    Agrega campo de activo a los datos de ubicacion
    :param data:
    :return: data
    """
    if data['activo']:
        data['activo'] = data['activo'].upper()
        data['activo'] = ESTATUS[data['activo']]
    else:
        data['activo'] = True
    return data


def load_webservices(url):
    """
    Consulta webservice de la DI y regresa los datos de ubicacion.
    :param url:
    :return: data
    """
    pass
