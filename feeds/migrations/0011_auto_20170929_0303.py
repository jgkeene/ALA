# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 07:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0010_auto_20170929_0614'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackernews',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='hackernews',
            name='date',
            field=models.DateField(auto_now_add=True, db_index=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hackernews',
            name='updated',
            field=models.BooleanField(default=False),
        ),
    ]
