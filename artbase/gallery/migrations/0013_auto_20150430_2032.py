# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0012_remove_artist_artiststyle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='customersLikeArtist',
        ),
        migrations.AddField(
            model_name='artist',
            name='artistStyle',
            field=models.CharField(default=b'NULL', max_length=20),
        ),
    ]
