# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-20 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front_desk', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkin',
            name='debcamp_meal_card',
        ),
        migrations.RemoveField(
            model_name='checkin',
            name='debconf_meal_card',
        ),
        migrations.AddField(
            model_name='checkin',
            name='key_card',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AddField(
            model_name='checkin',
            name='returned_card',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checkin',
            name='returned_key',
            field=models.BooleanField(default=False),
        ),
    ]
