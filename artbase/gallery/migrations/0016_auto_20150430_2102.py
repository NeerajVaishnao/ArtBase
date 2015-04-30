# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0015_likegroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='classifiedInto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('classifiedIntoArtworkTitle', models.ForeignKey(to='gallery.artwork', db_column=b'artworkTitle')),
                ('classifiedIntoGroupName', models.ForeignKey(to='gallery.group', db_column=b'groupName')),
            ],
        ),
        migrations.CreateModel(
            name='likeArtist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('likeArtistArtistName', models.ForeignKey(to='gallery.artist', db_column=b'artistName')),
            ],
        ),
        migrations.RenameModel(
            old_name='customers',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customersAddress',
            new_name='customerAddress',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customersAmount',
            new_name='customerAmount',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customersId',
            new_name='customerId',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customersName',
            new_name='customerName',
        ),
        migrations.AlterField(
            model_name='likegroup',
            name='likeGroupCustomerId',
            field=models.ForeignKey(to='gallery.customers', db_column=b'customersId', to_field='customerId'),
        ),
        migrations.AddField(
            model_name='likeartist',
            name='likeArtistCustomerId',
            field=models.ForeignKey(to='gallery.customer', db_column=b'customerId'),
        ),
    ]
