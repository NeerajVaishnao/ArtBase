# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0010_auto_20150430_2006'),
    ]

    operations = [
        migrations.CreateModel(
            name='customers',
            fields=[
                ('customersId', models.IntegerField(serialize=False, primary_key=True)),
                ('customersName', models.CharField(max_length=20)),
                ('customersAddress', models.CharField(max_length=20)),
                ('customersAmount', models.IntegerField(default=0)),
                ('customersLikeArtist', models.ForeignKey(to='gallery.artist', db_column=b'artistName')),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='customerLikeArtist',
        ),
        migrations.DeleteModel(
            name='customer',
        ),
    ]
