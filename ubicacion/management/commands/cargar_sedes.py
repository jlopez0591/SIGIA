import datetime as dt

import csv
import logging
import sys
from django.core.management.base import BaseCommand, CommandError
from ubicacion.models import Sede
from sigia import base_settings

logger = logging.getLogger(__name__)
LOG_FILE = '{}/{}'.format(base_settings.BASE_DIR, 'logs/carga_sedes/')

current_date = dt.datetime.now()
ARCHIVO_SEDES = '{}{}'.format(base_settings.BASE_DIR, '/import-files/sede.csv')
ESTATUS = {
    'A': True,
    'I': False
}


class Command(BaseCommand):
    help = 'Carga datos de sedes.'

    def handle(self, *args, **options):
        with open(ARCHIVO_SEDES, 'r') as f:
            data = csv.DictReader(f)
            for row in data:
                try:
                    row['activo'] = ESTATUS[row['activo']]
                    s, created = Sede.objects.update_or_create(cod_sede=row['cod_sede'], defaults=row)
                    if created:
                        logger.info('Sede {} creada exitosamente'.format(row['cod_sede']))
                    else:
                        logger.info('Sede {} ya existia')
                except:
                    logger.error('Hubo un error al crear la sede {}'.format(sys.exc_info()[1]))
