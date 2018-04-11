import logging
import sys
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

logger = logging.getLogger(__name__)

permisos_profesores = ['add_actividad', 'ver_departamento']

permisos_directores_departamento = ['ver_departamento', 'change_actividad']

permisos_directores_escuela = ['ver_escuela', 'ver_estudiante', 'ver_anteproyecto']

permisos_administrativos = ['ver_escuela', 'add_anteproyecto', 'ver_estudiante', 'change_estudiante']

permisos_comision = ['ver_escuela', 'aprobar_anteproyecto']

permisos_decanos = ['ver_facultad', 'ver_departamento', 'ver_escuela', 'ver_perfil']

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
                logger.info('Grupo {} creado.'.format(grupo))
                for permiso in permisos:
                    try:
                        p = Permission.objects.get(codename=permiso)
                        g.permissions.add(p)
                        logger.info('Se agrego el permiso {} al grupo {}.'.format(permiso, g))
                    except:
                        logger.error('Hubo un error al agregar el permiso {} al grupo {}: {}'.format(permiso, g,
                                                                                                     sys.exc_info()[1]))
