# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-06-10 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summer_plans', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='alias',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='\u533f\u540d\u6635\u79f0'),
        ),
        migrations.AddField(
            model_name='user',
            name='avatar_color',
            field=models.CharField(blank=True, choices=[(1, '#A0C1E5'), (2, '#DAE5A0'), (3, '#E5A1A0'), (4, '#D6A0E5'), (5, '#506B90')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_anon',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u533f\u540d'),
        ),
    ]
