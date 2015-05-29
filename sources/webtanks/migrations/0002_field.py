# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webtanks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('field_id', models.IntegerField(default=0)),
                ('request11', models.IntegerField(default=0)),
                ('request12', models.IntegerField(default=0)),
                ('request13', models.IntegerField(default=0)),
                ('request21', models.IntegerField(default=0)),
                ('request22', models.IntegerField(default=0)),
                ('request23', models.IntegerField(default=0)),
                ('state1', models.IntegerField(default=0)),
                ('state2', models.IntegerField(default=0)),
            ],
        ),
    ]
