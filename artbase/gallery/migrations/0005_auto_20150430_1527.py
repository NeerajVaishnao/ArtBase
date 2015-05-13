# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20150430_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='classifiedInto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('classifiedIntoArtworkTitle', models.ForeignKey(to='gallery.artwork', db_column=b'artworkTitle')),
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
            model_name='group',
            name='groupArtist',
            field=models.ForeignKey(to='gallery.artist', db_column=b'artistName'),
        ),
        migrations.AddField(
            model_name='classifiedinto',
            name='classifiedIntoGroupName',
            field=models.ForeignKey(to='gallery.group', db_column=b'groupName'),
        ),
    ]
