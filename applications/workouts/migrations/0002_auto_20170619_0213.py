# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 02:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Routine',
            new_name='Workout',
        ),
        migrations.RenameField(
            model_name='segment',
            old_name='routine',
            new_name='workout',
        ),
    ]