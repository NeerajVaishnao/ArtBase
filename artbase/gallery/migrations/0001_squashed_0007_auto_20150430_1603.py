# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    replaces = [(b'gallery', '0001_initial'), (b'gallery', '0002_auto_20150429_1927'), (b'gallery', '0003_auto_20150429_2008'), (b'gallery', '0004_auto_20150430_1507'), (b'gallery', '0005_auto_20150430_1527'), (b'gallery', '0006_auto_20150430_1549'), (b'gallery', '0007_auto_20150430_1603')]

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
                ('artworkType', models.CharField(default=b'NULL', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('customerName', models.CharField(max_length=20)),
                ('customerAddress', models.CharField(max_length=20)),
                ('customerAmount', models.IntegerField(default=0)),
                ('customerLikeArtist', models.ForeignKey(to='gallery.artist', db_column=b'artistName')),
                ('customerId', models.IntegerField(default=0, serialize=False, primary_key=True, db_column=b'customerId')),
            ],
        ),
        migrations.CreateModel(
            name='group',
            fields=[
                ('groupName', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('groupArtist', models.ForeignKey(to='gallery.artist', db_column=b'artistName')),
            ],
        ),
        migrations.CreateModel(
            name='likeGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('likeGroupName', models.CharField(default=b'NULL', max_length=20)),
                ('likeGroupCustomerId', models.ForeignKey(to='gallery.customer', db_column=b'customerId')),
            ],
        ),
        migrations.CreateModel(
            name='likeArtist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('likeArtistArtistName', models.ForeignKey(to='gallery.artist', db_column=b'artistName')),
                ('likeArtistCustomerId', models.ForeignKey(to='gallery.customer', db_column=b'customerId')),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='customerId',
            field=models.IntegerField(default=0, serialize=False, primary_key=True),
        ),
    ]
