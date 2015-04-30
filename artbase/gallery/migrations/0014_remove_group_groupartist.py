# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0013_auto_20150430_2032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='groupArtist',
        ),
    ]
