# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 05:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('granjasalmoral', '0017_auto_20161001_0515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infopersonal',
            name='img',
            field=models.FileField(null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='justificante',
            name='soporte',
            field=models.FileField(null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='pagare',
            field=models.FileField(null=True, upload_to='uploads/'),
        ),
    ]