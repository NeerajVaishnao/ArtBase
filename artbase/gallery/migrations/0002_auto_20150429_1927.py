# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customerLikeArtist',
            field=models.ForeignKey(to='gallery.artist', db_column=b'artistName'),
        ),
    ]
