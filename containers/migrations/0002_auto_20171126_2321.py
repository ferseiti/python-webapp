# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-26 23:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('containers', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserPorts',
            new_name='UserPort',
        ),
    ]