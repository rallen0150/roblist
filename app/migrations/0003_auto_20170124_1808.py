# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_item_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]