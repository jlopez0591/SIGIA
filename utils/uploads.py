import os
import uuid


def anteproyecto_upload_rename(instance, filename):
    upload_to = 'anteproyectos'
    ext = filename.split('.')[-1]
    new_name = str(uuid.uuid4())
    sede = instance.cod_sede
    facultad = instance.cod_facultad
    # new_filename = '{0}/facultad/{1}/{2}/{3}.{4}'.format(upload_to, sede, facultad, new_name, ext)
    new_filename = '{0}/{1}/{2}.{3}'.format(upload_to, generate_path(upload_to, instance), new_name, ext)
    return new_filename


def proyecto_upload_rename(instance, filename):
    return ''


def solicitud_upload_rename(instance, filename):
    return ''


def perfil_upload_rename(instance, filename):
    return ''


def actividad_upload_rename(instance, filename):
    return ''


def generate_path(tipo, instancia):
    filename = ''
    filename += tipo
    try:
        filename += '/' + instancia.cod_sede
    except AttributeError:
        pass
    try:
        filename += '/' + instancia.cod_facultad
    except AttributeError:
        pass
    try:
        filename += '/' + instancia.cod_escuela
    except AttributeError:
        pass
    try:
        filename += '/' + instancia.cod_departamento
    except AttributeError:
        pass
    try:
        filename += '/' + instancia.cod_carrera
    except AttributeError:
        pass
    return filename
