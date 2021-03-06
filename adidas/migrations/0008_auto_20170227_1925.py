# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adidas', '0007_auto_20170227_0754'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PlayerPoints',
            new_name='PlayerPointsInEvent',
        ),
        migrations.RemoveField(
            model_name='player',
            name='points',
        ),
        migrations.AddField(
            model_name='player',
            name='points_in_event',
            field=models.ManyToManyField(through='adidas.PlayerPointsInEvent', to='adidas.Event', verbose_name='Punti'),
        ),
    ]
