# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-21 20:43
from __future__ import unicode_literals

import almacen.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('cod_barras', models.ImageField(blank=True, null=True, upload_to=almacen.models.upload_image_pathb)),
                ('descripcion', models.CharField(max_length=50)),
                ('medida', models.CharField(max_length=50)),
                ('unidad', models.CharField(max_length=50)),
                ('existencia', models.PositiveIntegerField(default=0)),
                ('cantidad_caja', models.PositiveIntegerField(default=0)),
                ('cantidad_rb', models.PositiveIntegerField(default=0)),
                ('proveedor', models.CharField(max_length=50, null=True)),
                ('ubicacion', models.CharField(max_length=50, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to=almacen.models.upload_image_path)),
            ],
        ),
    ]
