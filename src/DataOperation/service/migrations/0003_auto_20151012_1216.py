# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_remove_service_category_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service_api',
            old_name='url',
            new_name='serve_url',
        ),
        migrations.AlterField(
            model_name='service_activepack',
            name='service',
            field=models.ForeignKey(related_name='base_activepack', to='service.Service_base'),
        ),
        migrations.AlterField(
            model_name='service_base',
            name='provider',
            field=models.ForeignKey(related_name='base_provider', to='service.Service_provider'),
        ),
        migrations.AlterField(
            model_name='service_base',
            name='serve_tags',
            field=models.ManyToManyField(related_name='base_tags', to='service.Service_tag', blank=True),
        ),
        migrations.AlterField(
            model_name='service_base',
            name='serve_type',
            field=models.ForeignKey(related_name='type_base', to='service.Service_type'),
        ),
        migrations.AlterField(
            model_name='service_statistics',
            name='service',
            field=models.OneToOneField(related_name='base_statistics', to='service.Service_base'),
        ),
        migrations.AlterField(
            model_name='service_type',
            name='category',
            field=models.ForeignKey(related_name='cate_type', to='service.Service_category'),
        ),
    ]
