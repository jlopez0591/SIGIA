# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-17 23:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now=True, null=True)),
                ('resumen', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Comentarios',
            },
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=120)),
                ('fecha_creacion', models.DateField(auto_now_add=True, null=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, null=True)),
                ('resumen', models.TextField(blank=True, max_length=500)),
                ('resuelto', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Solicitudes',
            },
        ),
        migrations.AddField(
            model_name='comentario',
            name='solicitud',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='solicitud.Solicitud'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
