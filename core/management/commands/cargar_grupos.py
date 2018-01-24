import logging
import sys
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group, Permission

logger = logging.getLogger(__name__)

permisos_profesores = [
    'add_idioma', 'add_titulo', 'add_ponencia', 'add_investigacion', 'add_premio', 'add_libro',
    'add_publicacion', 'add_estadiapostdoctoral', 'add_conferencia'
]

permisos_directores_departamento = [
    'aprobar_actividad', 'rechazar_actividad', 'consultar_detalle_departamento', 'ver_detalle_profesor'
]

permisos_directores_escuela = [
    'consultar_detalle_escuela', 'consultar_detalle_carrera', 'ver_detalle_estudiante'
]

permisos_administrativos = [
    'registrar_equipo', 'editar_equipo'
]

permisos_comision = [
    'create_anteproyecto', 'change_anteproyecto'
]

permisos_decanos = [
    'consultar_detalle_unidad', 'consultar_detalle_lescuela', 'consultar_detalle_departamento', 'consultar_detalle_escuela'
]

lista = {
    'Profesores': permisos_profesores,
    'Director de Departamento': permisos_directores_departamento,
    'Director de Escuela': permisos_directores_escuela,
    'Administrativos': permisos_administrativos,
    'Comision de Anteproyecto': permisos_comision,
    'Decanos': permisos_decanos,
}


class Command(BaseCommand):
    '''
        Comando para generar grupos y asignar permisos
    '''
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
