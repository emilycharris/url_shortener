# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short_url_app', '0003_bookmark_private'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='title',
            field=models.CharField(default='', max_length=20),
        ),
    ]
