# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_auto_20151022_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='service_api',
            name='proxy_url',
            field=models.CharField(default=None, max_length=500),
            preserve_default=False,
        ),
    ]
