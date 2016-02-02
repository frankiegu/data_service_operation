# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_auto_20151012_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='service_base',
            name='serve_abbreviation',
            field=models.SlugField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service_category',
            name='category_abbreviation',
            field=models.SlugField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service_type',
            name='type_abbreviation',
            field=models.SlugField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service_api',
            name='service',
            field=models.OneToOneField(related_name='base_api', to='service.Service_base'),
        ),
        migrations.AlterField(
            model_name='service_errorcode',
            name='error_type',
            field=models.ForeignKey(related_name='errorType_errorCode', to='service.Service_errorType'),
        ),
        migrations.AlterField(
            model_name='service_price',
            name='service',
            field=models.OneToOneField(related_name='base_price', to='service.Service_base'),
        ),
        migrations.AlterField(
            model_name='service_reqdemo',
            name='service',
            field=models.ForeignKey(related_name='base_reqdemo', to='service.Service_base'),
        ),
        migrations.AlterField(
            model_name='service_reqfield',
            name='service',
            field=models.ForeignKey(related_name='base_reqfield', to='service.Service_base'),
        ),
        migrations.AlterField(
            model_name='service_respdemo',
            name='service',
            field=models.ForeignKey(related_name='base_respdemo', to='service.Service_base'),
        ),
        migrations.AlterField(
            model_name='service_respfield',
            name='service',
            field=models.ForeignKey(related_name='base_respfield', to='service.Service_base'),
        ),
        migrations.AlterField(
            model_name='service_sdkpack',
            name='service',
            field=models.OneToOneField(related_name='base_sdkpack', to='service.Service_base'),
        ),
        migrations.AlterField(
            model_name='service_upgrade',
            name='service',
            field=models.ForeignKey(related_name='base_upgrade', to='service.Service_base'),
        ),
    ]
