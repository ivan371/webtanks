# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webtanks', '0004_auto_20150529_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='request11',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='field',
            name='request12',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='field',
            name='request13',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='field',
            name='request21',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='field',
            name='request22',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='field',
            name='request23',
            field=models.IntegerField(default=0),
        ),
    ]
