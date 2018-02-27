import datetime
import logging
import json
import sys
import os
from sigia import base_settings
from django.core.management.base import BaseCommand
from estudiantes.models import Estudiante

from sigia.base_settings import DEBUG

fecha = datetime.datetime.now().strftime("%Y-%m-%d")
ARCHIVO = '{}{}'.format(base_settings.BASE_DIR, '/test-data/node-estudiante.json')
LOG_LOCATION = '{}/{}'.format(base_settings.BASE_DIR, 'logs/estudiantes/creacion')
LOG_FILE = '{}/{}'.format(LOG_LOCATION, fecha)

if not os.path.exists(LOG_LOCATION):
    os.makedirs(LOG_LOCATION)

logging.basicConfig(filename='{}.log'.format(LOG_FILE), level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

ESTATUS = {
    'A': True,
    'I': False
}
FECHA_ACTUAL = str(datetime.datetime.now().year)  # Anio actual para ser especificos.


class Command(BaseCommand):
    help = 'Cargar y/o actualizar los datos de los estudiantes'

    def handle(self, *args, **options):
        data = self.load_file()
        for row in data:
            if row['ultimo_anio'] == FECHA_ACTUAL:
                try:
                    e, created = Estudiante.objects.update_or_create(
                        provincia=row['provincia'],
                        clase=row['clase'],
                        tomo=row['tomo'],
                        folio=row['folio'],
                        defaults=row
                    )
                    if created:
                        print('created')
                        logging.info(
                            'Estudiante {}-{}-{}-{} creado exitosamente'.format(row['provincia'], row['clase'],
                                                                                row['tomo'], row['folio']))
                except:
                    logging.error('Hubo un error al registrar al estudiante {} - {} - {} - {} \nError: {}'.format(
                        row['provincia'],
                        row['clase'],
                        row['tomo'],
                        row['folio'], sys.exc_info()[1]))
            else:
                pass

    def load_file(self):
        """
        Carga los datos de prueba desde el archivo "test_data/estudiante.json"
        :return: Objeto de tipo diccionario con el listado de estudiantes.
        """
        lista = dict()
        with open(ARCHIVO, 'r') as f:
            lista = json.load(f)
        return lista


def load_webservice(url):
    """

    :param url: Direccion con la cual accesamos al webservice
    :return: Objeto diccionario con lista de los estudiantes
    """
    # TODO: Agregar libreria "requests"
    pass
