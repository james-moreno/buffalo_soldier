# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 16:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landr', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='last_name',
            new_name='alias',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='first_name',
            new_name='name',
        ),
    ]
