import csv
import json
import logging
import os.path
import sys

from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group

from django.conf import settings
from perfiles.models import Perfil


user_info = [
    {
        'user_name': 'pruebas',
        'first_name': 'Pruebas',
        'last_name': 'Usuario',
        'password': 'test2018',
        'grupos': [],
        'perfil': {
            'primer_nombre': 'Pruebas',
            'primer_apellido': 'Usuario',
            'provincia': '01',
            'clase': '00',
            'tomo': '000',
            'folio': '0000',
            'cod_sede': '00',
            'cod_facultad': '00',
            'cod_escuela': '00',
            'cod_departamento': '00'
        }
    }, 
    {
        'user_name': 'profesor',
        'first_name': 'Profesor',
        'last_name': 'Usuario',
        'password': 'teach2018',
        'grupos': ['Profesores'],
        'perfil': {
            'primer_nombre': 'Profesor',
            'primer_apellido': 'Usuario',
            'provincia': '02',
            'clase': '00',
            'tomo': '000',
            'folio': '0000',
            'cod_sede': '00',
            'cod_facultad': '00',
            'cod_escuela': '00',
            'cod_departamento': '00'
        }
    }, 
    {
        'user_name': 'departamento',
        'first_name': 'Departamento',
        'last_name': 'Usuario',
        'password': 'dpto2018',
        'grupos': ['Director de Departamento'],
        'perfil': {
            'primer_nombre': 'Departamento',
            'primer_apellido': 'Usuario',
            'provincia': '03',
            'clase': '00',
            'tomo': '000',
            'folio': '0000',
            'cod_sede': '00',
            'cod_facultad': '00',
            'cod_escuela': '00',
            'cod_departamento': '00'
        }
    }, 
    {
        'user_name': 'escuela',
        'first_name': 'Escuela',
        'last_name': 'Usuario',
        'password': 'schl2018',
        'grupos': ['Director de Escuela'],
        'perfil': {
            'primer_nombre': 'Escuela',
            'primer_apellido': 'Usuario',
            'provincia': '04',
            'clase': '00',
            'tomo': '000',
            'folio': '0000',
            'cod_sede': '00',
            'cod_facultad': '00',
            'cod_escuela': '00',
            'cod_departamento': '00'
        }
    }, 
    {
        'user_name': 'comision',
        'first_name': 'Comision',
        'last_name': 'Usuario',
        'password': 'comit2018',
        'grupos': ['Comision de Anteproyecto'],
        'perfil': {
            'primer_nombre': 'Comision',
            'primer_apellido': 'Usuario',
            'provincia': '05',
            'clase': '00',
            'tomo': '000',
            'folio': '0000',
            'cod_sede': '00',
            'cod_facultad': '00',
            'cod_escuela': '00',
            'cod_departamento': '00'
        }
    }, 
    {
        'user_name': 'administrativo',
        'first_name': 'Administrativo',
        'last_name': 'Usuario',
        'password': 'admi2018',
        'grupos': ['Administrativos'],
        'perfil': {
            'primer_nombre': 'Administrativo',
            'primer_apellido': 'Usuario',
            'provincia': '06',
            'clase': '00',
            'tomo': '000',
            'folio': '0000',
            'cod_sede': '00',
            'cod_facultad': '00',
            'cod_escuela': '00',
            'cod_departamento': '00'
        }
    },
    {
        'user_name': 'decano',
        'first_name': 'Decano',
        'last_name': 'Usuario',
        'password': 'dean2018',
        'grupos': ['Decanos'],
        'perfil': {
            'primer_nombre': 'Decano',
            'primer_apellido': 'Usuario',
            'provincia': '07',
            'clase': '00',
            'tomo': '000',
            'folio': '0000',
            'cod_sede': '00',
            'cod_facultad': '00',
            'cod_escuela': '00',
            'cod_departamento': '00'
        }
    }
]


class Command(BaseCommand):
    help = 'Carga usuarios demo'

    def handle(self, *args, **options):
        for data in user_info:
            u, created = User.objects.get_or_create(username=data['user_name'], first_name=data['first_name'], last_name=data['last_name'])
            if created:
                u.set_password(data['password'])
                u.save()
            for grupo in data['grupos']:
                try:
                    g = Group.objects.get(name=grupo.title())
                    u.groups.add(g)
                    print('Usuario agregado {} al grupo: {}'.format(u.username, g.name))
                except ObjectDoesNotExist as exc:
                    print(exc)
            p, created = Perfil.objects.update_or_create(usuario=u, defaults=data['perfil'])
            if created:
                print("Perfil creado {0}".format(p))

