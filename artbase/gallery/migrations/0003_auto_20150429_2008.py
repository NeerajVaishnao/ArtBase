# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20150429_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='id',
        ),
        migrations.RemoveField(
            model_name='group',
            name='id',
        ),
        migrations.AddField(
            model_name='group',
            name='groupArtist',
            field=models.ForeignKey(db_column=b'artistName', default=b'NULL', to='gallery.artist'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customerName',
            field=models.CharField(max_length=20, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='groupName',
            field=models.CharField(max_length=20, serialize=False, primary_key=True),
        ),
    ]
