# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webtanks', '0003_auto_20150529_1532'),
    ]

    operations = [
        migrations.RenameField(
            model_name='field',
            old_name='state1',
            new_name='state',
        ),
        migrations.RemoveField(
            model_name='field',
            name='state2',
        ),
        migrations.AlterField(
            model_name='field',
            name='field_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='request11',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='request12',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='request13',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='request21',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='request22',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='request23',
            field=models.IntegerField(unique=True),
        ),
    ]
