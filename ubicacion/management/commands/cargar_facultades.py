import csv
import logging
import sys
from sigia import base_settings
from django.core.management.base import BaseCommand, CommandError
from ubicacion.models import Unidad



logger = logging.getLogger(__name__)
ARCHIVO= '{}{}'.format(base_settings.BASE_DIR, '/import-files/facultad.csv')
ESTATUS = {
    'A': True,
    'I': False
}


class Command(BaseCommand):
    help = 'Carga datos de '

    def handle(self, *args, **options):
        with open(ARCHIVO, 'r') as f:
            data = csv.DictReader(f)
            for row in data:
                try:
                    row['activo'] = ESTATUS[row['activo']]
                    u, created = Unidad.objects.update_or_create(cod_unidad=row['cod_unidad'], defaults=row)
                    if created:
                        logger.info(' {} creada exitosamente'.format(row['cod_unidad']))
                except:
                    logger.error('Hubo un error al crear la facultad {}'.format(sys.exc_info()[1]))