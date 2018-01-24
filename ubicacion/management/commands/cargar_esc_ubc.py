import csv
import logging
import sys
from sigia import base_settings
from django.core.management.base import BaseCommand, CommandError
from ubicacion.models import SeccionInstancia

logger = logging.getLogger(__name__)
ARCHIVO = '{}{}'.format(base_settings.BASE_DIR, '/import-files/esc_ubc.csv')
ESTATUS = {
    'A': True,
    'I': False
}


class Command(BaseCommand):
    help = 'Carga datos de las instancias de escuelas'

    def handle(self, *args, **options):
        with open(ARCHIVO, 'r') as f:
            data = csv.DictReader(f)
            for row in data:
                try:
                    if row['activo']:
                        row['activo'] = ESTATUS[row['activo']]
                    else:
                        row['activo'] = True
                    s, created = SeccionInstancia.objects.update_or_create(cod_sede=row['cod_sede'],
                                                                           cod_unidad=row['cod_unidad'],
                                                                           cod_seccion=row['cod_seccion'], defaults=row)
                    if created:
                        logger.info(' {} - {} - {} creada exitosamente'.format(row['cod_sede'], row['cod_unidad'],
                                                                               row['cod_seccion']))
                except:
                    logger.error('Hubo un error al crear la escuela {} - {} - {} : error {}'.format(row['cod_sede'],
                                                                                                    row['cod_unidad'],
                                                                                                    row['cod_seccion'],
                                                                                                    sys.exc_info()))
