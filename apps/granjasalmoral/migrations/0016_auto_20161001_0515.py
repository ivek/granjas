# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 05:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('granjasalmoral', '0015_auto_20161001_0511'),
    ]

    operations = [
        migrations.AddField(
            model_name='infopersonal',
            name='razon_social',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='granjasalmoral.empresas'),
        ),
        migrations.AlterField(
            model_name='infopersonal',
            name='id_personal',
            field=models.CharField(max_length=30),
        ),
    ]
