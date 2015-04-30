# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_auto_20150430_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classifiedinto',
            name='classifiedIntoArtworkTitle',
        ),
        migrations.RemoveField(
            model_name='classifiedinto',
            name='classifiedIntoGroupName',
        ),
        migrations.DeleteModel(
            name='classifiedInto',
        ),
    ]
