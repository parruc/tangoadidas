# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-03 19:25
from __future__ import unicode_literals

import adidas.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adidas', '0015_event_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=adidas.models.user_directory_path, verbose_name='Immagine del profili'),
        ),
    ]
