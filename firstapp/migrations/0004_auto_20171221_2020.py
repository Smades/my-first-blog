# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-21 19:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_auto_20171221_2018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='activity',
            new_name='title',
        ),
    ]