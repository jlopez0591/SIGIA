import datetime
import json
import logging
import os
import sys

from sigia import base_settings
from django.core.management.base import BaseCommand
from ubicacion.models import Sede, Unidad, Seccion, Carrera, UnidadInstancia, SeccionInstancia, CarreraInstancia

fecha = datetime.datetime.now().strftime("%Y-%m-%d")
ARCHIVO = '{}{}'.format(base_settings.BASE_DIR, '/test_data/node.json')
LOG_LOCATION = '{}/{}'.format(base_settings.BASE_DIR, 'logs/ubicacion/creacion')
LOG_FILE = '{}/{}'.format(LOG_LOCATION, fecha)

ESTATUS = {
    'A': True,
    'I': False
}

if not os.path.exists(LOG_LOCATION):
    os.makedirs(LOG_LOCATION)

logging.basicConfig(filename='{}.log'.format(LOG_FILE), level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class Command(BaseCommand):
    help = 'Cargar y/o actualizar los datos de las ubicaciones'

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
                print('Test1')
                sede = apply_activo(sede)
                print(data, '1')
                s, created = Sede.objects.update_or_create(cod_sede=sede['cod_sede'], defaults=sede)
                if created:
                    logging.info('Sede: {} creada'.format(sede['cod_sede']))
            except:
                logging.error('Sede: {} Error: {}'.format(sede['cod_sede'], sys.exc_info()[1]))
        for unidad in unidades:
            try:
                unidad = apply_activo(unidad)
                u, created = Unidad.objects.update_or_create(cod_facultad=unidad['cod_facultad'], defaults=unidad)
                if created:
                    logging.info('Unidad: {} creada'.format(unidad['cod_facultad']))
            except:
                logging.error('Unidad: {}'.format(unidad['cod_facultad']))
        for seccion in secciones:
            try:
                seccion = apply_activo(seccion)
                s, created = Seccion.objects.update_or_create(cod_facultad=seccion['cod_facultad'],
                                                              cod_escuela=seccion['cod_escuela'], defaults=seccion)
                if created:
                    logging.info('Seccion {}-{} creada'.format(seccion['cod_facultad'], seccion['cod_escuela']))
            except:
                logging.error('Seccion: {}-{}'.format(seccion['cod_facultad'], seccion['cod_escuela']))
        for carrera in carreras:
            try:
                carrera = apply_activo(carrera)
                c, created = Carrera.objects.update_or_create(cod_facultad=carrera['cod_facultad'],
                                                              cod_escuela=carrera['cod_escuela'],
                                                              cod_carrera=carrera['cod_carrera'], defaults=carrera)
                if created:
                    logging.info('Carrera {}-{}-{} creada'.format(carrera['cod_facultad'], carrera['cod_escuela'],
                                                                  carrera['cod_carrera']))
            except:
                logging.error(
                    'Carrera: {}-{}-{}'.format(carrera['cod_facultad'], carrera['cod_escuela'], carrera['cod_carrera']))
        for unidad in uni_ubc:
            try:
                try:
                    unidad = apply_activo(unidad)
                    u, created = UnidadInstancia.objects.update_or_create(cod_sede=unidad['cod_sede'],
                                                                          cod_facultad=unidad['cod_facultad'],
                                                                          defaults=unidad)
                    if created:
                        logging.info('Unidad: {}-{} creada'.format(unidad['cod_sede'], unidad['cod_facultad']))
                except:
                    logging.error('Unidad: {}'.format(unidad['cod_facultad']))
            except:
                logging.error('Unidad: {}-{}'.format(unidad['cod_sede'], unidad['cod_facultad']))
        for seccion in sec_ubc:
            try:
                seccion = apply_activo(seccion)
                s, created = SeccionInstancia.objects.update_or_create(cod_sede=seccion['cod_sede'],
                                                                       cod_facultad=seccion['cod_facultad'],
                                                                       cod_escuela=seccion['cod_escuela'],
                                                                       defaults=seccion)
                if created:
                    logging.info('Seccion {}-{}-{} creada'.format(seccion['cod_sede'], seccion['cod_facultad'],
                                                                  seccion['cod_escuela']))
            except:
                logging.error(
                    'Seccion: {}-{}-{}'.format(seccion['cod_sede'], seccion['cod_facultad'], seccion['cod_escuela']))
        for carrera in car_ubc:
            try:
                carrera = apply_activo(carrera)
                c, created = CarreraInstancia.objects.update_or_create(cod_sede=carrera['cod_sede'],
                                                                       cod_facultad=carrera['cod_facultad'],
                                                                       cod_escuela=carrera['cod_escuela'],
                                                                       cod_carrera=carrera['cod_carrera'],
                                                                       defaults=carrera)
                if created:
                    logging.info('Carrera {}-{}-{}-{} creada'.format(carrera['cod_sede'], carrera['cod_facultad'],
                                                                     carrera['cod_escuela'],
                                                                     carrera['cod_carrera']))
            except:
                logging.error(
                    'Carrera: {}-{}-{}-{}'.format(carrera['cod_sede'], carrera['cod_facultad'], carrera['cod_escuela'],
                                                  carrera['cod_carrera']))


def apply_activo(data):
    """
    Agrega campo de activo a los datos de ubicacion
    :param data:
    :return: data
    """
    print(type(data))
    if 'activo' in data:
        print('Activo existia')
        data['activo'] = data['activo'].upper()
        data['activo'] = ESTATUS[data['activo']]
    else:
        print('Activo no existia')
        data['activo'] = True
    print(data)
    return data


# TODO: Necesario la creacion de webservice por parte de la DI
def load_webservice(url):
    """
    Consulta webservice de la DI y regresa los datos de ubicacion.
    :param url: Direccion de acceso al webservice de la DI.
    :return: Objeto diccionario con lista de las ubicaciones.
    """
    pass
