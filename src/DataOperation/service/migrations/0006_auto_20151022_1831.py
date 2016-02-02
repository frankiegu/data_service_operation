# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_service_api_proxy_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service_category',
            old_name='category_abbreviation',
            new_name='cate_abbreviation',
        ),
        migrations.RemoveField(
            model_name='service_api',
            name='proxy_url',
        ),
    ]
