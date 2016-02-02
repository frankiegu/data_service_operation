# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_auto_20151022_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_base',
            name='serve_abbreviation',
            field=models.SlugField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='service_category',
            name='cate_abbreviation',
            field=models.SlugField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='service_type',
            name='type_abbreviation',
            field=models.SlugField(unique=True, max_length=100),
        ),
    ]
