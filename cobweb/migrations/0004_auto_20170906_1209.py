# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-06 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cobweb', '0003_agent_software'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='software',
            options={'verbose_name_plural': 'Software'},
        ),
        migrations.AddField(
            model_name='user',
            name='deprecated',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date Deprecated'),
        ),
    ]
