# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 10:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0007_reddit_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reddit',
            name='updated',
        ),
    ]
