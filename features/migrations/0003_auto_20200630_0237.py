# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-30 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0002_auto_20200629_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='created_date',
            field=models.DateTimeField(),
        ),
    ]