# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0011_auto_20150430_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='artistStyle',
        ),
    ]
