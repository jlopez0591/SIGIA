# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-17 23:41
from __future__ import unicode_literals

import actividades.models
import utils.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ubicacion', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_sede', models.CharField(blank=True, max_length=2)),
                ('cod_facultad', models.CharField(blank=True, max_length=2)),
                ('cod_departamento', models.CharField(blank=True, max_length=2)),
                ('clase', models.CharField(blank=True, choices=[('estadia_postdoctoral', 'Estadia Postdoctoral'), ('publicacion', 'Publicacion'), ('investigacion', 'Investigacion'), ('libro', 'Libro'), ('conferencia', 'Conferencia'), ('ponencia', 'Ponencia'), ('proyecto', 'Proyecto'), ('premio', 'Premio'), ('idioma', 'Idioma'), ('titulo', 'Titulo'), ('otro', 'Otro')], max_length=30, null=True)),
                ('fecha', models.DateField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('nombre_actividad', models.CharField(max_length=120)),
                ('resumen', models.TextField(blank=True, max_length=1000)),
                ('estado', models.CharField(choices=[('espera', 'En Espera de Aprobacion'), ('rechazado', 'Rechazado'), ('aprobado', 'Aprobado')], default='espera', max_length=25)),
                ('motivo_rechazo', models.TextField(blank=True, max_length=500)),
                ('archivo', models.FileField(upload_to=actividades.models.user_directory_path, validators=[
                    utils.validators.validate_file_type])),
            ],
            options={
                'permissions': (('aprobar_actividad', 'Aprobar Actividad'),),
                'manager_inheritance_from_future': True,
                'verbose_name_plural': 'Actividades',
            },
        ),
        migrations.CreateModel(
            name='CentroEstudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120, unique=True)),
                ('pais', django_countries.fields.CountryField(max_length=2)),
            ],
            options={
                'verbose_name_plural': 'Centros de Estudio',
            },
        ),
        migrations.CreateModel(
            name='InfoTitulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120, unique=True)),
                ('nivel', models.CharField(choices=[('licenciatura', 'Licenciatura'), ('postgrado', 'Postgrado'), ('maestria', 'Maestria'), ('doctorado', 'Doctorado')], max_length=25)),
            ],
            options={
                'verbose_name_plural': 'Informacion de Titulos',
            },
        ),
        migrations.CreateModel(
            name='Conferencia',
            fields=[
                ('actividad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='actividades.Actividad')),
                ('duracion', models.PositiveIntegerField(blank=True, default=0)),
            ],
            options={
                'manager_inheritance_from_future': True,
                'verbose_name_plural': 'Conferencia',
            },
            bases=('actividades.actividad',),
        ),
        migrations.CreateModel(
            name='EstadiaPostdoctoral',
            fields=[
                ('actividad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='actividades.Actividad')),
                ('lugar', models.CharField(max_length=1020)),
                ('duracion', models.PositiveIntegerField(blank=True, default=0)),
            ],
            options={
                'manager_inheritance_from_future': True,
                'verbose_name_plural': 'Estadias postdoctorales',
            },
            bases=('actividades.actividad',),
        ),
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('actividad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='actividades.Actividad')),
                ('nombre', models.CharField(choices=[('af', 'Afrikaans'), ('ar', 'Arabic'), ('ast', 'Asturian'), ('az', 'Azerbaijani'), ('bg', 'Bulgarian'), ('be', 'Belarusian'), ('bn', 'Bengali'), ('br', 'Breton'), ('bs', 'Bosnian'), ('ca', 'Catalan'), ('cs', 'Czech'), ('cy', 'Welsh'), ('da', 'Danish'), ('de', 'German'), ('dsb', 'Lower Sorbian'), ('el', 'Greek'), ('en', 'English'), ('en-au', 'Australian English'), ('en-gb', 'British English'), ('eo', 'Esperanto'), ('es', 'Spanish'), ('es-ar', 'Argentinian Spanish'), ('es-co', 'Colombian Spanish'), ('es-mx', 'Mexican Spanish'), ('es-ni', 'Nicaraguan Spanish'), ('es-ve', 'Venezuelan Spanish'), ('et', 'Estonian'), ('eu', 'Basque'), ('fa', 'Persian'), ('fi', 'Finnish'), ('fr', 'French'), ('fy', 'Frisian'), ('ga', 'Irish'), ('gd', 'Scottish Gaelic'), ('gl', 'Galician'), ('he', 'Hebrew'), ('hi', 'Hindi'), ('hr', 'Croatian'), ('hsb', 'Upper Sorbian'), ('hu', 'Hungarian'), ('ia', 'Interlingua'), ('id', 'Indonesian'), ('io', 'Ido'), ('is', 'Icelandic'), ('it', 'Italian'), ('ja', 'Japanese'), ('ka', 'Georgian'), ('kk', 'Kazakh'), ('km', 'Khmer'), ('kn', 'Kannada'), ('ko', 'Korean'), ('lb', 'Luxembourgish'), ('lt', 'Lithuanian'), ('lv', 'Latvian'), ('mk', 'Macedonian'), ('ml', 'Malayalam'), ('mn', 'Mongolian'), ('mr', 'Marathi'), ('my', 'Burmese'), ('nb', 'Norwegian Bokmål'), ('ne', 'Nepali'), ('nl', 'Dutch'), ('nn', 'Norwegian Nynorsk'), ('os', 'Ossetic'), ('pa', 'Punjabi'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pt-br', 'Brazilian Portuguese'), ('ro', 'Romanian'), ('ru', 'Russian'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('sq', 'Albanian'), ('sr', 'Serbian'), ('sr-latn', 'Serbian Latin'), ('sv', 'Swedish'), ('sw', 'Swahili'), ('ta', 'Tamil'), ('te', 'Telugu'), ('th', 'Thai'), ('tr', 'Turkish'), ('tt', 'Tatar'), ('udm', 'Udmurt'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('vi', 'Vietnamese'), ('zh-hans', 'Simplified Chinese'), ('zh-hant', 'Traditional Chinese')], max_length=7)),
                ('nivel_hablado', models.CharField(choices=[('basico', 'Basico'), ('intermedio', 'Intermedio'), ('avanzado', 'Avanzado'), ('nativo', 'Nativo')], default='nativo', max_length=15)),
                ('nivel_escrito', models.CharField(choices=[('basico', 'Basico'), ('intermedio', 'Intermedio'), ('avanzado', 'Avanzado'), ('nativo', 'Nativo')], default='nativo', max_length=15)),
            ],
            options={
                'manager_inheritance_from_future': True,
                'verbose_name_plural': 'Idiomas',
            },
            bases=('actividades.actividad',),
        ),
        migrations.CreateModel(
            name='Investigacion',
            fields=[
                ('actividad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='actividades.Actividad')),
                ('codigo', models.CharField(max_length=100)),
                ('duracion', models.PositiveIntegerField(blank=True, default=0)),
            ],
            options={
                'manager_inheritance_from_future': True,
                'verbose_name_plural': 'Investigaciones',
            },
            bases=('actividades.actividad',),
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('actividad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='actividades.Actividad')),
                ('isbn', models.CharField(max_length=1020)),
                ('editorial', models.CharField(max_length=1020)),
            ],
            options={
                'manager_inheritance_from_future': True,
                'verbose_name_plural': 'Libros',
            },
            bases=('actividades.actividad',),
        ),
        migrations.CreateModel(
            name='Ponencia',
            fields=[
                ('actividad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='actividades.Actividad')),
                ('pais', django_countries.fields.CountryField(max_length=2)),
            ],
            options={
                'manager_inheritance_from_future': True,
                'verbose_name_plural': 'Ponencias',
            },
            bases=('actividades.actividad',),
        ),
        migrations.CreateModel(
            name='Premio',
            fields=[
                ('actividad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='actividades.Actividad')),
                ('tipo', models.CharField(choices=[('nacional', 'Nacional'), ('internacional', 'Internacional')], max_length=100)),
            ],
            options={
                'manager_inheritance_from_future': True,
                'verbose_name_plural': 'Premios',
            },
            bases=('actividades.actividad',),
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('actividad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='actividades.Actividad')),
                ('tipo', models.CharField(choices=[('estudio', 'Estudio de Factibilidad'), ('asesoria', 'Asesoria'), ('planos', 'Planos'), ('especificacion', 'Especificaciones Tecnicas'), ('proyecto', 'Proyectos'), ('aplicacion', 'Desarrollo de Aplicaciones'), ('poemario', 'Poemarios'), ('libreto', 'Libretos'), ('recital', 'Recitales'), ('teatro', 'Direccion de Teatro'), ('actuacion', 'Actuacion'), ('danza', 'Danza'), ('concierto', 'Conciertos'), ('produccion', 'Produccion Artistica'), ('audiovisual', 'Audiovisual'), ('grafico', 'Diseno Grafico'), ('arte', 'Obra de Arte')], max_length=100)),
            ],
            options={
                'manager_inheritance_from_future': True,
                'verbose_name_plural': 'Proyectos',
            },
            bases=('actividades.actividad',),
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('actividad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='actividades.Actividad')),
                ('tipo', models.CharField(choices=[('revista_especializada_internacional', 'Revista Especializada Internacional'), ('revista_general_internacional', 'Revista General Internacional'), ('revista_general_nacional', 'Revista General Nacional'), ('periodico_nacional', 'Periodico Nacional'), ('periodicio_ilimitado', 'Periodico Ilimitado'), ('boletin', 'Boletin'), ('gaceta', 'Gaceta'), ('otros', 'Otros')], default='otros', max_length=100)),
                ('lugar_publicacion', models.CharField(max_length=1020)),
            ],
            options={
                'manager_inheritance_from_future': True,
                'verbose_name_plural': 'Publicaciones',
            },
            bases=('actividades.actividad',),
        ),
        migrations.CreateModel(
            name='Titulo',
            fields=[
                ('actividad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='actividades.Actividad')),
            ],
            options={
                'manager_inheritance_from_future': True,
                'verbose_name_plural': 'Titulos',
            },
            bases=('actividades.actividad',),
        ),
        migrations.AlterUniqueTogether(
            name='centroestudio',
            unique_together=set([('nombre', 'pais')]),
        ),
        migrations.AddField(
            model_name='actividad',
            name='departamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='actividades', to='ubicacion.DepartamentoInstancia'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='facultad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='actividades', to='ubicacion.FacultadInstancia'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_actividades.actividad_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='sede',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='actividades', to='ubicacion.Sede'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='actividades', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='titulo',
            name='centro_estudio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actividades.CentroEstudio'),
        ),
        migrations.AddField(
            model_name='titulo',
            name='info_titulo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actividades.InfoTitulo'),
        ),
        migrations.AlterUniqueTogether(
            name='libro',
            unique_together=set([('isbn',)]),
        ),
        migrations.AlterUniqueTogether(
            name='investigacion',
            unique_together=set([('codigo',)]),
        ),
        migrations.AlterUniqueTogether(
            name='actividad',
            unique_together=set([('usuario', 'nombre_actividad')]),
        ),
    ]