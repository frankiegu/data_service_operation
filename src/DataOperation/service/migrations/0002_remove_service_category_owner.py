# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations #@UnusedImport


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service_category',
            name='owner',
        ),
    ]
