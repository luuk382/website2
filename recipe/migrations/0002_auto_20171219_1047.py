# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-19 09:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Recipe',
        ),
    ]
