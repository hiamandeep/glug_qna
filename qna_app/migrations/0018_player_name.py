# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-04 22:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna_app', '0017_auto_20180304_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
