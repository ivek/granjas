# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 05:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('granjasalmoral', '0018_auto_20161001_0518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comision',
            name='id_personal',
        ),
        migrations.RemoveField(
            model_name='infopersonal',
            name='razon_social',
        ),
        migrations.RemoveField(
            model_name='jornada',
            name='id_personal',
        ),
        migrations.RemoveField(
            model_name='justificante',
            name='id_personal',
        ),
        migrations.RemoveField(
            model_name='prestamo',
            name='id_personal',
        ),
        migrations.DeleteModel(
            name='comision',
        ),
        migrations.DeleteModel(
            name='InfoPersonal',
        ),
        migrations.DeleteModel(
            name='Jornada',
        ),
        migrations.DeleteModel(
            name='justificante',
        ),
        migrations.DeleteModel(
            name='prestamo',
        ),
    ]
