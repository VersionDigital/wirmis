# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-02 11:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boola', '0005_auto_20161103_0900'),
        ('disciple', '0009_remove_dispatch_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispatch',
            name='booking',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='boola.Booking'),
            preserve_default=False,
        ),
    ]
