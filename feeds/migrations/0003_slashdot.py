# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0002_auto_20170914_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slashdot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('url', models.URLField(blank=True, max_length=500, null=True)),
                ('num_comments', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-num_comments'],
            },
        ),
    ]
