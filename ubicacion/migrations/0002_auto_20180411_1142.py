# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-11 16:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ubicacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamentoinstancia',
            options={'permissions': (('ver_departamento', 'Ver Departamento'),), 'verbose_name_plural': 'Instancias Departamento'},
        ),
        migrations.AlterModelOptions(
            name='escuelainstancia',
            options={'permissions': (('ver_escuela', 'Ver Escuela'),), 'verbose_name_plural': 'Instancias Secciones'},
        ),
        migrations.AlterModelOptions(
            name='facultadinstancia',
            options={'permissions': (('ver_facultad', 'Ver Facultad'),), 'verbose_name_plural': 'Instancias Facultades'},
        ),
        migrations.AlterUniqueTogether(
            name='departamentoinstancia',
            unique_together=set([('cod_sede', 'cod_facultad', 'cod_departamento')]),
        ),
    ]
