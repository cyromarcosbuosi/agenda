# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-12-11 17:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_auto_20171211_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='data_alteracao',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]