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

permisos_profesores = ['add_actividad', 'ver_departamento', 'change_perfil']

permisos_directores_departamento = ['ver_departamento', 'change_actividad', 'ver_perfil', 'aprobar_actividad']

# ver departamento = ver actividades del departamento, ver profesores del departamento
# ver perfil = Poder observar perfiles de otros profesores

permisos_directores_escuela = ['ver_escuela']

# Ver escuela = Ver detalle de escuela, ver estudiantes, ver anteproyectos y ver proyectos

permisos_administrativos = ['ver_escuela', 'add_anteproyecto', 'add_proyecto', 'change_estudiante']

# TODO: Agregar secretario administrativo con permisos de - invetario

# change_estudiante = editar estudiante, tarea de administrativos de la escuela

permisos_comision = ['ver_escuela', 'aprobar_anteproyecto', 'add_proyecto']

# TODO: Rearmar anteproyecto y proyecto como TrabajoDeGraduacion - Editar Permisos Acorde

permisos_decanos = ['ver_facultad', 'ver_departamento', 'ver_escuela', 'ver_perfil']

# ver facultad = debe poder ver todos los detalles de la facultad.

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
