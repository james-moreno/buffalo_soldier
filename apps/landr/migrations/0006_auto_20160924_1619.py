# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-24 23:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landr', '0005_auto_20160923_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poke',
            name='poke_total',
        ),
        migrations.RemoveField(
            model_name='register',
            name='pokes',
        ),
        migrations.AddField(
            model_name='poke',
            name='pokes',
            field=models.ManyToManyField(to='landr.Register'),
        ),
    ]
