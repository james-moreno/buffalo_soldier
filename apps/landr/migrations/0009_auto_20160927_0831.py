# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 15:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landr', '0008_register_poke_total'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Register',
            new_name='User',
        ),
        migrations.RemoveField(
            model_name='poke',
            name='pokee',
        ),
        migrations.RemoveField(
            model_name='poke',
            name='poker',
        ),
        migrations.DeleteModel(
            name='Poke',
        ),
    ]
