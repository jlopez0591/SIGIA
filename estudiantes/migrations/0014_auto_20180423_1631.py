# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-23 21:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0013_auto_20180417_1603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudiante',
            old_name='semestre_ingreso',
            new_name='semestre',
        ),
    ]
