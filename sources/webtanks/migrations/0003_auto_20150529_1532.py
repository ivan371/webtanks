# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webtanks', '0002_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='user1',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='field',
            name='user2',
            field=models.ForeignKey(related_name='second', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
