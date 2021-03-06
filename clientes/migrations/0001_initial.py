# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-25 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('direccion', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('celular', models.CharField(blank=True, max_length=25)),
                ('empresa', models.CharField(max_length=50)),
                ('ejecutivo', models.CharField(blank=True, max_length=50)),
                ('usuario', models.IntegerField()),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
