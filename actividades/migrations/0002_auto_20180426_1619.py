# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-26 21:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='fecha_actualizacion',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True),
        ),
    ]
