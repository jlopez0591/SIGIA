# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-05 00:45
from __future__ import unicode_literals

from django.db import migrations, models
import utils.uploads
import utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0003_auto_20180404_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anteproyecto',
            name='archivo',
            field=models.FileField(blank=True, upload_to=utils.uploads.anteproyecto_upload_rename, validators=[utils.validators.validate_file_type]),
        ),
    ]