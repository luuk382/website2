# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-21 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0009_auto_20171221_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='dietary',
            field=models.CharField(choices=[(1, 'Omnivore'), (2, 'Carnivore'), (3, 'Herbivore')], default='Omnivore', max_length=100),
        ),
    ]
