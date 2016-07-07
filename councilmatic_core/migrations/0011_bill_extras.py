# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('councilmatic_core', '0010_auto_20160120_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='extras',
            field=jsonfield.fields.JSONCharField(max_length=255, blank=True),
        ),
    ]
