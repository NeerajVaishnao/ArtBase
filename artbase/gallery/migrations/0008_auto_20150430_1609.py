# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_auto_20150430_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customerId',
            field=models.IntegerField(default=0, serialize=False, primary_key=True, db_column=b'customerId'),
        ),
    ]
