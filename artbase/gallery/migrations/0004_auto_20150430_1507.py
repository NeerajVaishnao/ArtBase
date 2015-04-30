# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20150429_2008'),
    ]

    operations = [
        migrations.CreateModel(
            name='likeGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('likeGroupName', models.CharField(default=b'NULL', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='artwork',
            name='artworkType',
            field=models.CharField(default=b'NULL', max_length=20),
        ),
        migrations.AddField(
            model_name='customer',
            name='customerId',
            field=models.IntegerField(default=0, serialize=False, primary_key=True, db_column=b'customerId'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customerName',
            field=models.CharField(max_length=20),
        ),
        migrations.AddField(
            model_name='likegroup',
            name='likeGroupCustomerId',
            field=models.ForeignKey(to='gallery.customer', db_column=b'customerId'),
        ),
    ]
