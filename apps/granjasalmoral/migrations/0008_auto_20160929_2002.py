# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 20:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('granjasalmoral', '0007_auto_20160929_2000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comision',
            name='id_personal',
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
        migrations.AlterField(
            model_name='infopersonal',
            name='fech_ingreso_cooperativa',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='infopersonal',
            name='fech_ingreso_empresa',
            field=models.DateField(blank=True),
        ),
        migrations.DeleteModel(
            name='comision',
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
