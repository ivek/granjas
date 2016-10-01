# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 20:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('granjasalmoral', '0006_comision_jornada_justificante_prestamo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comision',
            name='fecha_orden',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='infopersonal',
            name='fech_ingreso_cooperativa',
            field=models.DateField(default='0000-00-00'),
        ),
        migrations.AlterField(
            model_name='infopersonal',
            name='fech_ingreso_empresa',
            field=models.DateField(default='0000-00-00'),
        ),
        migrations.AlterField(
            model_name='justificante',
            name='fecha_justificante',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_prest',
            field=models.DateField(default='0000-00-00'),
        ),
    ]