# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 21:13
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='video',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location=('/home/chudix/projects/workoutholic/uploads',)), upload_to='exercises/videos/'),
        ),
    ]
