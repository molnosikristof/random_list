# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-25 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('random_list_app', '0002_auto_20210125_2011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='randomlist',
            old_name='list_to_randomize',
            new_name='list_content',
        ),
        migrations.AlterField(
            model_name='randomlist',
            name='list_name',
            field=models.CharField(max_length=100),
        ),
    ]
