# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-27 02:36
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20160427_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=DjangoUeditor.models.UEditorField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='cover',
            field=models.ImageField(default=b'default_cover.png', max_length=200, upload_to=b''),
        ),
    ]
