# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 06:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0008_auto_20170913_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitequery',
            name='sw_distance',
            field=models.CharField(choices=[('close', '< 150'), ('not_close', '>= 150')], max_length=24, verbose_name='Distance from surface water'),
        ),
    ]
