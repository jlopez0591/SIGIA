# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-11 17:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import utils.uploads
import utils.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ubicacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anteproyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_sede', models.CharField(blank=True, max_length=120)),
                ('cod_facultad', models.CharField(blank=True, max_length=120)),
                ('cod_escuela', models.CharField(blank=True, max_length=120)),
                ('cod_carrera', models.CharField(blank=True, max_length=120)),
                ('nombre_proyecto', models.CharField(blank=True, max_length=120)),
                ('fecha_registro', models.DateField(auto_now_add=True, null=True)),
                ('fecha_aprobacion', models.DateField(blank=True, null=True)),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('rechazado', 'Rechazado'), ('aprobado', 'Aprobado')], default='pendiente', max_length=15)),
                ('archivo', models.FileField(blank=True, upload_to=utils.uploads.anteproyecto_upload_rename, validators=[utils.validators.validate_file_type])),
                ('resumen', models.TextField(blank=True, max_length=500)),
                ('asesor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='anteproyecto', to=settings.AUTH_USER_MODEL)),
                ('carrera', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='anteproyectos', to='ubicacion.CarreraInstancia')),
                ('escuela', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='anteproyectos', to='ubicacion.EscuelaInstancia')),
            ],
            options={
                'permissions': (('aprobar_anteproyecto', 'Aprobar Anteproyecto'), ('ver_anteproyecto_facultad', 'Ver Anteproyectos en Facultad'), ('ver_anteproyecto_escuela', 'Ver Anteproyecto en Escuela')),
            },
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provincia', models.CharField(blank=True, choices=[('0', '00'), ('1', '01'), ('2', '02'), ('3', '03'), ('4', '04'), ('5', '05'), ('6', '06'), ('7', '07'), ('8', '08'), ('9', '09')], default='00', max_length=5)),
                ('clase', models.CharField(blank=True, choices=[('00', '00'), ('N', 'N'), ('E', 'E'), ('EC', 'EC'), ('PE', 'PE'), ('AV', 'AV'), ('PI', 'PI')], default='00', max_length=5)),
                ('tomo', models.CharField(blank=True, default='000', max_length=5)),
                ('folio', models.CharField(blank=True, default='0000', max_length=5)),
                ('primer_nombre', models.CharField(blank=True, max_length=120)),
                ('segundo_nombre', models.CharField(blank=True, max_length=120)),
                ('primer_apellido', models.CharField(blank=True, max_length=120)),
                ('segundo_apellido', models.CharField(blank=True, max_length=120)),
                ('direccion', models.CharField(blank=True, max_length=120)),
                ('sexo', models.CharField(blank=True, choices=[('M', 'Hombre'), ('F', 'Mujer')], max_length=120)),
                ('telefono', models.CharField(blank=True, max_length=120)),
                ('tipo_sangre', models.CharField(blank=True, choices=[('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=120)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('discapacidad', models.TextField(blank=True, max_length=500, null=True)),
                ('pais', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('correo', models.EmailField(blank=True, max_length=254)),
                ('telefono_oficina', models.CharField(blank=True, max_length=120)),
                ('celular', models.CharField(blank=True, max_length=120)),
                ('celular_oficina', models.CharField(blank=True, max_length=120)),
                ('cod_sede', models.CharField(blank=True, default='XX', max_length=2)),
                ('cod_facultad', models.CharField(blank=True, default='XX', max_length=2)),
                ('cod_escuela', models.CharField(blank=True, default='XX', max_length=2)),
                ('cod_carrera', models.CharField(blank=True, default='XX', max_length=2)),
                ('turno', models.CharField(blank=True, choices=[('D', 'Diurno'), ('V', 'Vespertino'), ('N', 'Nocturno')], max_length=1)),
                ('fecha_ingreso', models.DateField(blank=True, null=True)),
                ('semestre_ingreso', models.CharField(blank=True, choices=[('0', ''), ('1', 'I'), ('2', 'II')], max_length=5)),
                ('ultimo_anio', models.CharField(blank=True, max_length=4)),
                ('ultimo_semestre', models.CharField(blank=True, max_length=5)),
                ('fecha_graduacion', models.DateField(blank=True, null=True)),
                ('carrera', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='estudiantes', to='ubicacion.CarreraInstancia')),
                ('escuela', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='estudiantes', to='ubicacion.EscuelaInstancia')),
                ('facultad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='estudiantes', to='ubicacion.FacultadInstancia')),
                ('sede', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='estudiantes', to='ubicacion.Sede')),
            ],
            options={
                'permissions': (('view_estudiante', 'Can view estudiante'),),
            },
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_sede', models.CharField(blank=True, max_length=120)),
                ('cod_facultad', models.CharField(blank=True, max_length=120)),
                ('cod_escuela', models.CharField(blank=True, max_length=120)),
                ('cod_carrera', models.CharField(blank=True, max_length=120)),
                ('fecha_entrega', models.DateField(blank=True, null=True)),
                ('fecha_sustentacion', models.DateField(blank=True, null=True)),
                ('programa', models.CharField(choices=[('licenciatura', 'Licenciatura'), ('especializacion', 'Especialización'), ('maestria', 'Maestria'), ('doctorado', 'Doctorado')], default='licenciatura', max_length=25)),
                ('nota', models.CharField(blank=True, max_length=3)),
                ('detalle', models.TextField(blank=True, max_length=500)),
                ('archivo', models.FileField(blank=True, upload_to='proyectos')),
                ('anteproyecto', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='estudiantes.Anteproyecto')),
                ('carrera', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proyectos', to='ubicacion.CarreraInstancia')),
                ('escuela', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proyectos', to='ubicacion.EscuelaInstancia')),
                ('estudiante', models.ManyToManyField(related_name='proyectos', to='estudiantes.Estudiante')),
                ('facultad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proyectos', to='ubicacion.FacultadInstancia')),
                ('jurados', models.ManyToManyField(related_name='jurado', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='anteproyecto',
            name='estudiante',
            field=models.ManyToManyField(related_name='anteproyectos', to='estudiantes.Estudiante'),
        ),
        migrations.AddField(
            model_name='anteproyecto',
            name='facultad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='anteproyectos', to='ubicacion.FacultadInstancia'),
        ),
        migrations.AddField(
            model_name='anteproyecto',
            name='registrado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='registros', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='anteproyecto',
            name='sede',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='anteproyectos', to='ubicacion.Sede'),
        ),
        migrations.AlterUniqueTogether(
            name='estudiante',
            unique_together=set([('provincia', 'clase', 'tomo', 'folio')]),
        ),
    ]
