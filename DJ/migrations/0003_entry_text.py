# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DJ', '0002_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='text',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
