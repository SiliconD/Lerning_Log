# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 06:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DJ', '0004_auto_20170911_0142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='data_added',
            new_name='date_added',
        ),
    ]
