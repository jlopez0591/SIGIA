import os
import uuid


def trabajo_upload_rename(instance, filename):
    upload_to = 'trabajos'
    ext = filename.split('.')[-1]
    new_name = str(uuid.uuid4())
    new_filename = '{0}/{1}/{2}.{3}'.format(upload_to, generate_path(upload_to, instance), new_name, ext)
    return new_filename


def solicitud_upload_rename(instance, filename):
    upload_to = 'solicitudes'
    ext = filename.split('.')[-1]
    new_name = str(uuid.uuid4())
    new_filename = '{0}/{1}.{2}'.format(upload_to, new_name, ext)
    return new_filename


def imagen_perfil_upload_rename(instance, filename):
    return ''


def reporte_actividad_upload_rename(instance, filename):
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
