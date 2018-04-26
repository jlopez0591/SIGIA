# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-26 21:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ubicacion', '0003_auto_20180417_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrera',
            name='fecha_actualizacion',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='carrera',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carrerainstancia',
            name='fecha_actualizacion',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='carrerainstancia',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='departamento',
            name='fecha_actualizacion',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='departamento',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='departamentoinstancia',
            name='fecha_actualizacion',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='departamentoinstancia',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='escuela',
            name='fecha_actualizacion',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='escuela',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='escuelainstancia',
            name='fecha_actualizacion',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='escuelainstancia',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='facultad',
            name='fecha_actualizacion',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='facultad',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='facultadinstancia',
            name='fecha_actualizacion',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='facultadinstancia',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sede',
            name='fecha_actualizacion',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='sede',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]