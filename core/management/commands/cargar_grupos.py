import logging
import os
import sys
from datetime import datetime as dt
from django.conf import settings

from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


fecha = dt.now()
LOG_LOCATION = '{}/{}/{}'.format(settings.BASE_DIR,
                                 'logs/grupos/creacion/', fecha.strftime("%Y-%m-%d"))
LOG_FILE = '{}/{}.log'.format(LOG_LOCATION, fecha.strftime("%X"))

if not os.path.exists(LOG_LOCATION):
    os.makedirs(LOG_LOCATION)       

logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')                          

permisos_profesores = ['add_actividad', 'change_actividad']

permisos_directores_departamento = ['ver_departamento', 'ver_actividades_departamento', 'ver_profesores_departamento', 'aprobar_actividad']

permisos_directores_escuela = ['ver_escuela', 'ver_estudiantes_escuela', 'ver_trabajos_escuela']

permisos_administrativos = ['ver_estudiantes_escuela', 'change_estudiante', 'ver_equipos_facultad', 'ver_aulas_facultad']

permisos_comision = ['ver_trabajos_escuela', 'change_trabajograduacion', 'add_trabajograduacion']

permisos_decanos = ['ver_facultad', 'ver_profesores_facultad', 'ver_estudiantes_facultad', 'ver_trabajos_facultad', 'ver_actividades_facultad', 'ver_equipos_facultad', 'ver_aulas_facultad']

lista = {
    'Profesores': permisos_profesores,
    'Director de Departamento': permisos_directores_departamento,
    'Director de Escuela': permisos_directores_escuela,
    'Administrativos': permisos_administrativos,
    'Comision de Anteproyecto': permisos_comision,
    'Decanos': permisos_decanos,
}

class Command(BaseCommand):
    help = 'Crea los grupos de usuarios para el sistema y asigna permisos correspondientes.'

    def handle(self, *args, **options):
        for grupo, permisos in lista.items():
            g, created = Group.objects.get_or_create(name=grupo.title())
            if created:
                logging.info('Grupo {} creado.'.format(grupo))
            for permiso in permisos:
                try:
                    p = Permission.objects.get(codename=permiso)
                    if p not in g.permissions.all():
                        g.permissions.add(p)
                        logging.info('Se agrego el permiso {} al grupo {}.'.format(permiso, g))
                except ObjectDoesNotExist:
                    logger.error('Hubo un error al agregar el permiso {} al grupo {}: {}'.format(permiso, g,
                                                                                                    sys.exc_info()[1]))
