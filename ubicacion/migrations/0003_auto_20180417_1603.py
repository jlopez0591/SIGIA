# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-17 21:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ubicacion', '0002_auto_20180411_1142'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamentoinstancia',
            options={'permissions': (('ver_departamento', 'Ver Departamento'), ('ver_profesores_departamento', 'Ver Profesores'), ('ver_actividades_departamento', 'Ver Actividades')), 'verbose_name_plural': 'Instancias Departamento'},
        ),
        migrations.AlterModelOptions(
            name='escuelainstancia',
            options={'permissions': (('ver_escuela', 'Ver Escuela'), ('ver_estudiantes_escuela', 'Ver Estudiantes'), ('ver_trabajos_escuela', 'Ver Trabajos')), 'verbose_name_plural': 'Instancias Secciones'},
        ),
        migrations.AlterModelOptions(
            name='facultadinstancia',
            options={'permissions': (('ver_facultad', 'Ver Facultad'), ('ver_profesores_facultad', 'Ver Profesores'), ('ver_estudiantes_facultad', 'Ver Estudiantes'), ('ver_actividades_facultad', 'Ver Actividades'), ('ver_trabajos_facultad', 'Ver Trabajos')), 'verbose_name_plural': 'Instancias Facultades'},
        ),
    ]
