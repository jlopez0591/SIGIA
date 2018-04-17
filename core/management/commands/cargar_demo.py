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
        'grupos': []
    }, 
    {
        'user_name': 'profesor',
        'first_name': 'Profesor',
        'last_name': 'Usuario',
        'password': 'teach2018',
        'grupos': ['Profesores']
    }, 
    {
        'user_name': 'departamento',
        'first_name': 'Departamento',
        'last_name': 'Usuario',
        'password': 'dpto2018',
        'grupos': ['Director de Departamento']
    }, 
    {
        'user_name': 'escuela',
        'first_name': 'Escuela',
        'last_name': 'Usuario',
        'password': 'schl2018',
        'grupos': ['Director de Escuela']
    }, 
    {
        'user_name': 'comision',
        'first_name': 'Comision',
        'last_name': 'Usuario',
        'password': 'comit2018',
        'grupos': ['Comision de Anteproyecto']
    }, 
    {
        'user_name': 'administrativo',
        'first_name': 'Administrativo',
        'last_name': 'Usuario',
        'password': 'admi2018',
        'grupos': ['Administrativos']
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
                        g = Group.objects.get(name=grupo)
                        u.groups.add(g)
                        print('Usuario agregado {} al grupo: {}'.format(u.username, g.name))
                    except ObjectDoesNotExist as exc:
                        print(exc)
