# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-22 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0006_auto_20180622_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='almacen',
            name='costo',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True),
        ),
    ]