# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='artist',
            fields=[
                ('artistName', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('artistBirthPlace', models.CharField(max_length=20)),
                ('artistAge', models.IntegerField(default=0)),
                ('artistStyle', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='artwork',
            fields=[
                ('artworkTitle', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('artworkYear', models.IntegerField(default=0)),
                ('artworkPrice', models.IntegerField(default=0)),
                ('artworkArtist', models.ForeignKey(to='gallery.artist', db_column=b'artistName')),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customerName', models.CharField(max_length=20)),
                ('customerAddress', models.CharField(max_length=20)),
                ('customerAmount', models.IntegerField(default=0)),
                ('customerLikeArtist', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('groupName', models.CharField(max_length=20)),
            ],
        ),
    ]
