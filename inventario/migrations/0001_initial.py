# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-17 23:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ubicacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=5)),
                ('tipo', models.CharField(choices=[('1', 'Aula'), ('2', 'Laboratorio'), ('3', 'Oficina')], max_length=1)),
                ('cod_sede', models.CharField(blank=True, max_length=2)),
                ('cod_facultad', models.CharField(blank=True, max_length=2)),
                ('ubicacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ubicacion.FacultadInstancia')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etiqueta', models.CharField(max_length=120, unique=True)),
                ('cod_sede', models.CharField(blank=True, max_length=2)),
                ('cod_facultad', models.CharField(blank=True, max_length=2)),
                ('observaciones', models.TextField(blank=True, max_length=500)),
                ('aula', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.Aula')),
            ],
        ),
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120, unique=True)),
                ('url', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120, unique=True)),
                ('url', models.URLField(blank=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modelos', to='inventario.Categoria')),
                ('fabricante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modelos', to='inventario.Fabricante')),
            ],
        ),
        migrations.AddField(
            model_name='equipo',
            name='modelo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipos', to='inventario.Modelo'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='ubicacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='equipos', to='ubicacion.FacultadInstancia'),
        ),
    ]