# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 23:57
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('councilmatic_core', '0012_auto_20160707_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='extras',
            field=jsonfield.fields.JSONCharField(default='{}', max_length=255),
        ),
        migrations.AlterField(
            model_name='event',
            name='extras',
            field=jsonfield.fields.JSONCharField(default='{}', max_length=255),
        ),
        migrations.AlterField(
            model_name='organization',
            name='extras',
            field=jsonfield.fields.JSONCharField(default='{}', max_length=255),
        ),
        migrations.AlterField(
            model_name='person',
            name='extras',
            field=jsonfield.fields.JSONCharField(default='{}', max_length=255),
        ),
    ]
