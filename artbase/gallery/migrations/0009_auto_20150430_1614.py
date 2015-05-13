# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_auto_20150430_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likeartist',
            name='likeArtistArtistName',
        ),
        migrations.RemoveField(
            model_name='likeartist',
            name='likeArtistCustomerId',
        ),
        migrations.RemoveField(
            model_name='likegroup',
            name='likeGroupCustomerId',
        ),
        migrations.DeleteModel(
            name='likeArtist',
        ),
        migrations.DeleteModel(
            name='likeGroup',
        ),
    ]
