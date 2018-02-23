import json
import logging
import os
import sys

from django.core.management.base import BaseCommand
from inventario.models import Fabricante
from sigia import base_settings


class Command(BaseCommand):
    help = 'Cargar listado de fabricantes'

    def handle(self, *args, **options):
        data = cargar_archivo()
        for row in data:
            try:
                f, created = Fabricante.objects.get_or_create(**row)
                if created:
                    logging.info('Fabricante {} creado.'.format(f))
            except:
                logging.error('Hubo un error al crear al fabricante {} - Error: {}', f['nombre'], sys.exc_info()[1])


def cargar_archivo():
    lista = dict()
    return lista
