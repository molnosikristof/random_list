# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-25 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RandomList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=1000)),
                ('list_to_randomize', models.CharField(max_length=1000)),
            ],
        ),
    ]