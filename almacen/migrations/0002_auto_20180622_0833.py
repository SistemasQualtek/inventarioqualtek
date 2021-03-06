# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-22 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='almacen',
            name='cantidad_caja',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='almacen',
            name='cantidad_rb',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='almacen',
            name='codigo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='almacen',
            name='existencia',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='almacen',
            name='medida',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
