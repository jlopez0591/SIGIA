import csv
import datetime
import logging
import sys
from sigia import base_settings
from django.core.management.base import BaseCommand, CommandError
from estudiantes.models import Estudiante

logger = logging.getLogger(__name__)
ARCHIVO = '{}{}'.format(base_settings.BASE_DIR, '/import-files/estudiantes.csv')
ESTATUS = {
    'A': True,
    'I': False
}
FECHA_ACTUAL = str(datetime.datetime.now().year)
FECHA_ACTUAL_DEV = str(datetime.datetime.now().year-1)


class Command(BaseCommand):
    help = 'Cargar o actualizar los datos de los estudiantes, esta informacion viene del archivo import-files/estudiantes.csv'

    def handle(self, *args, **options):
        with open(ARCHIVO, 'r') as f:
            data = csv.DictReader(f)
            for row in data:
                if row['ultimo_anio'] == FECHA_ACTUAL_DEV:
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
                            logger.info(
                                'Estudiante {}-{}-{}-{} creado exitosamente'.format(row['provincia'], row['clase'],
                                                                                    row['tomo'], row['folio']))
                    except:
                        logger.error('Hubo un error al registrar al estudiante {} - {} - {} - {} \nError: {}'.format(
                            row['provincia'],
                            row['clase'],
                            row['tomo'],
                            row['folio'], sys.exc_info()[1]))
                else:
                    print('No es reciente')
