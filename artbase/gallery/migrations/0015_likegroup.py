# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0014_remove_group_groupartist'),
    ]

    operations = [
        migrations.CreateModel(
            name='likeGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('likeGroupName', models.CharField(default=b'NULL', max_length=20)),
                ('likeGroupCustomerId', models.ForeignKey(to='gallery.customers', db_column=b'customersId')),
            ],
        ),
    ]
