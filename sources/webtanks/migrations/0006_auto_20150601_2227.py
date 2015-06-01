# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('webtanks', '0005_auto_20150530_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='who',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
