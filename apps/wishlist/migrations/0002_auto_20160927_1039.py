# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 17:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='added_by',
        ),
        migrations.RemoveField(
            model_name='item',
            name='user',
        ),
    ]