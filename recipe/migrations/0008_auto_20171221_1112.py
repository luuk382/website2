# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-21 10:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0007_auto_20171221_1111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='text',
            new_name='recipe',
        ),
    ]
