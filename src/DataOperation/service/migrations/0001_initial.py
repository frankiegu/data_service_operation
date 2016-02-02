# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Common_httpDemo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('hyperlink', models.CharField(max_length=500)),
                ('create_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateField(default=django.utils.timezone.now, blank=True)),
            ],
            options={
                'verbose_name': 'Http\u901a\u7528\u793a\u4f8b',
                'verbose_name_plural': 'Http\u901a\u7528\u793a\u4f8b',
            },
        ),
        migrations.CreateModel(
            name='Service_activePack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pack_name', models.CharField(max_length=100)),
                ('pack_desc', models.CharField(max_length=500)),
                ('pack_price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('by_counts_or_time', models.IntegerField(choices=[(0, b'\xe5\x8c\x85\xe6\xac\xa1'), (1, b'\xe5\x8c\x85\xe6\x97\xb6')])),
                ('pack_counts', models.IntegerField()),
                ('pack_effective_time', models.PositiveIntegerField()),
                ('time_unit', models.IntegerField(choices=[(0, b'\xe6\xaf\x8f\xe5\xa4\xa9'), (1, b'\xe6\xaf\x8f\xe5\x91\xa8'), (3, b'\xe6\xaf\x8f\xe6\x9c\x88'), (4, b'\xe6\xaf\x8f\xe5\xb9\xb4'), (2, b'\xe4\xbb\x8e\xe4\xb8\x8d')])),
                ('status', models.IntegerField(choices=[(0, b'\xe5\xa4\xb1\xe6\x95\x88'), (1, b'\xe7\x94\x9f\xe6\x95\x88')])),
                ('create_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateField(default=django.utils.timezone.now, blank=True)),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u6d3b\u52a8\u5957\u9910',
                'verbose_name_plural': '\u670d\u52a1\u6d3b\u52a8\u5957\u9910',
            },
        ),
        migrations.CreateModel(
            name='Service_api',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=500)),
                ('format', models.CharField(max_length=100)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
            ],
            options={
                'verbose_name': '\u670d\u52a1api\u8be6\u60c5',
                'verbose_name_plural': '\u670d\u52a1api\u8be6\u60c5',
            },
        ),
        migrations.CreateModel(
            name='Service_base',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serve_name', models.CharField(max_length=200)),
                ('serve_desc', models.TextField()),
                ('serve_logo', models.ImageField(upload_to=b'images/service/ico/', blank=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u57fa\u7840\u4fe1\u606f',
                'verbose_name_plural': '\u670d\u52a1\u57fa\u7840\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Service_category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=100)),
                ('parent_category_id', models.IntegerField(default=0, blank=True)),
                ('serve_cate_logo', models.ImageField(upload_to=b'images/ico/', blank=True)),
                ('create_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('order_num', models.IntegerField()),
                ('owner', models.ForeignKey(related_name='categorys', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['order_num'],
                'verbose_name': '\u670d\u52a1\u7c7b\u522b',
                'verbose_name_plural': '\u670d\u52a1\u7c7b\u522b',
            },
        ),
        migrations.CreateModel(
            name='Service_contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('support_team', models.CharField(max_length=500)),
                ('support_telno', models.CharField(max_length=20)),
                ('groupQQ', models.CharField(max_length=20)),
                ('contactQQ', models.CharField(max_length=100)),
                ('partnerQQ', models.CharField(max_length=100)),
                ('create_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('service', models.OneToOneField(to='service.Service_base')),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u8054\u7edc\u4fe1\u606f',
                'verbose_name_plural': '\u670d\u52a1\u8054\u7edc\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Service_errorCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('error_code', models.CharField(max_length=100)),
                ('error_name', models.CharField(max_length=1000)),
                ('create_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateField(default=django.utils.timezone.now, blank=True)),
            ],
            options={
                'verbose_name': '\u8c03\u7528\u9519\u8bef\u4ee3\u7801',
                'verbose_name_plural': '\u8c03\u7528\u9519\u8bef\u4ee3\u7801',
            },
        ),
        migrations.CreateModel(
            name='Service_errorType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('error_type_name', models.CharField(max_length=200)),
                ('create_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateField(default=django.utils.timezone.now, blank=True)),
            ],
            options={
                'verbose_name': '\u8c03\u7528\u9519\u8bef\u7c7b\u578b',
                'verbose_name_plural': '\u8c03\u7528\u9519\u8bef\u7c7b\u578b',
            },
        ),
        migrations.CreateModel(
            name='Service_fieldType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('field_type_name', models.CharField(max_length=200)),
                ('create_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateField(default=django.utils.timezone.now, blank=True)),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u53c2\u6570\u7c7b\u578b',
                'verbose_name_plural': '\u670d\u52a1\u53c2\u6570\u7c7b\u578b',
            },
        ),
        migrations.CreateModel(
            name='Service_invokeDemo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('hyperlink', models.CharField(max_length=500)),
                ('provider', models.CharField(max_length=200)),
                ('create_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('service', models.ForeignKey(to='service.Service_base')),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u8c03\u7528\u793a\u4f8b',
                'verbose_name_plural': '\u670d\u52a1\u8c03\u7528\u793a\u4f8b',
            },
        ),
        migrations.CreateModel(
            name='Service_others',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=100)),
                ('detail', models.TextField(max_length=1000)),
                ('create_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('service', models.ForeignKey(to='service.Service_base')),
            ],
            options={
                'verbose_name': '\u5176\u4ed6\u670d\u52a1\u76f8\u5173',
                'verbose_name_plural': '\u5176\u4ed6\u670d\u52a1\u76f8\u5173',
            },
        ),
        migrations.CreateModel(
            name='Service_price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_free', models.BooleanField(default=True)),
                ('free_times_per', models.IntegerField()),
                ('per_unit', models.IntegerField(choices=[(0, b'\xe6\xaf\x8f\xe5\xa4\xa9'), (1, b'\xe6\xaf\x8f\xe5\x91\xa8'), (3, b'\xe6\xaf\x8f\xe6\x9c\x88'), (4, b'\xe6\xaf\x8f\xe5\xb9\xb4'), (2, b'\xe4\xbb\x8e\xe4\xb8\x8d')])),
                ('cost', models.DecimalField(max_digits=5, decimal_places=0)),
                ('create_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('service', models.OneToOneField(related_name='rel_price', to='service.Service_base')),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u5b9a\u4ef7',
                'verbose_name_plural': '\u670d\u52a1\u5b9a\u4ef7',
            },
        ),
        migrations.CreateModel(
            name='Service_protocol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('protocol_name', models.CharField(max_length=200)),
                ('support_method', models.CharField(max_length=200, blank=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u534f\u8bae',
                'verbose_name_plural': '\u670d\u52a1\u534f\u8bae',
            },
        ),
        migrations.CreateModel(
            name='Service_provider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('provider_name', models.CharField(max_length=200)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
            ],
            options={
                'verbose_name': '\u6570\u636e\u4f9b\u5e94\u5546',
                'verbose_name_plural': '\u6570\u636e\u4f9b\u5e94\u5546',
            },
        ),
        migrations.CreateModel(
            name='Service_reqDemo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('demo_format', models.CharField(max_length=100)),
                ('demo_str', models.TextField(max_length=2000)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('service', models.ForeignKey(related_name='rel_reqdemo', to='service.Service_base')),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u8bf7\u6c42\u793a\u4f8b',
                'verbose_name_plural': '\u670d\u52a1\u8bf7\u6c42\u793a\u4f8b',
            },
        ),
        migrations.CreateModel(
            name='Service_reqField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('field_name', models.CharField(max_length=100)),
                ('required', models.IntegerField(choices=[(0, b'\xe5\x90\xa6'), (1, b'\xe6\x98\xaf')])),
                ('description', models.CharField(max_length=1000)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('field_type', models.ForeignKey(to='service.Service_fieldType')),
                ('service', models.ForeignKey(related_name='rel_reqfield', to='service.Service_base')),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u4f20\u53c2\u8bbe\u7f6e',
                'verbose_name_plural': '\u670d\u52a1\u4f20\u53c2\u8bbe\u7f6e',
            },
        ),
        migrations.CreateModel(
            name='Service_respDemo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('demo_format', models.CharField(max_length=100)),
                ('demo_str', models.TextField(max_length=2000)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('service', models.ForeignKey(related_name='rel_respdemo', to='service.Service_base')),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u8fd4\u56de\u793a\u4f8b',
                'verbose_name_plural': '\u670d\u52a1\u8fd4\u56de\u793a\u4f8b',
            },
        ),
        migrations.CreateModel(
            name='Service_respField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('field_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('field_type', models.ForeignKey(to='service.Service_fieldType')),
                ('service', models.ForeignKey(related_name='rel_respfield', to='service.Service_base')),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u8fd4\u56de\u503c\u8bbe\u7f6e',
                'verbose_name_plural': '\u670d\u52a1\u8fd4\u56de\u503c\u8bbe\u7f6e',
            },
        ),
        migrations.CreateModel(
            name='Service_sdkPack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pack_name', models.CharField(max_length=100)),
                ('pack_desc', models.CharField(max_length=500)),
                ('free_times_per', models.IntegerField()),
                ('per_unit', models.IntegerField(choices=[(0, b'\xe6\xaf\x8f\xe5\xa4\xa9'), (1, b'\xe6\xaf\x8f\xe5\x91\xa8'), (3, b'\xe6\xaf\x8f\xe6\x9c\x88'), (4, b'\xe6\xaf\x8f\xe5\xb9\xb4'), (2, b'\xe4\xbb\x8e\xe4\xb8\x8d')])),
                ('single_client_free_times_per', models.IntegerField()),
                ('single_client_per_unit', models.IntegerField(choices=[(0, b'\xe6\xaf\x8f\xe5\xa4\xa9'), (1, b'\xe6\xaf\x8f\xe5\x91\xa8'), (3, b'\xe6\xaf\x8f\xe6\x9c\x88'), (4, b'\xe6\xaf\x8f\xe5\xb9\xb4'), (2, b'\xe4\xbb\x8e\xe4\xb8\x8d')])),
                ('create_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('service', models.OneToOneField(related_name='rel_sdkpack', to='service.Service_base')),
            ],
            options={
                'verbose_name': 'SDK\u4f7f\u7528\u4f18\u60e0',
                'verbose_name_plural': 'SDK\u4f7f\u7528\u4f18\u60e0',
            },
        ),
        migrations.CreateModel(
            name='Service_statistics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scores', models.DecimalField(max_digits=2, decimal_places=1)),
                ('app_counts', models.IntegerField()),
                ('invoke_counts', models.IntegerField()),
                ('scan_counts', models.IntegerField()),
                ('create_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('service', models.OneToOneField(related_name='rel_statistics', to='service.Service_base')),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u79ef\u5206\u548c\u7edf\u8ba1',
                'verbose_name_plural': '\u670d\u52a1\u79ef\u5206\u548c\u7edf\u8ba1',
            },
        ),
        migrations.CreateModel(
            name='Service_status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status_name', models.CharField(max_length=200)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u72b6\u6001',
                'verbose_name_plural': '\u670d\u52a1\u72b6\u6001',
            },
        ),
        migrations.CreateModel(
            name='Service_tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_name', models.CharField(max_length=b'100')),
                ('tag_color', models.IntegerField()),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u6807\u7b7e',
                'verbose_name_plural': '\u670d\u52a1\u6807\u7b7e',
            },
        ),
        migrations.CreateModel(
            name='Service_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_name', models.CharField(max_length=100)),
                ('parent_type_id', models.IntegerField(default=0, blank=True)),
                ('serve_type_logo', models.ImageField(upload_to=b'images/ico/', blank=True)),
                ('create_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('order_num', models.IntegerField()),
                ('category', models.ForeignKey(to='service.Service_category')),
            ],
            options={
                'ordering': ['order_num'],
                'verbose_name': '\u670d\u52a1\u7c7b\u578b',
                'verbose_name_plural': '\u670d\u52a1\u7c7b\u578b',
            },
        ),
        migrations.CreateModel(
            name='Service_upgrade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('upgrade_title', models.CharField(max_length=100)),
                ('upgrade_contents', models.CharField(max_length=1000)),
                ('upgrade_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('create_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('modify_time', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('service', models.ForeignKey(related_name='rel_upgrade', to='service.Service_base')),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u66f4\u65b0\u8bb0\u5f55',
                'verbose_name_plural': '\u670d\u52a1\u66f4\u65b0\u8bb0\u5f55',
            },
        ),
        migrations.AddField(
            model_name='service_errorcode',
            name='error_type',
            field=models.ForeignKey(to='service.Service_errorType'),
        ),
        migrations.AddField(
            model_name='service_errorcode',
            name='service',
            field=models.ForeignKey(to='service.Service_base'),
        ),
        migrations.AddField(
            model_name='service_base',
            name='protocol',
            field=models.ForeignKey(to='service.Service_protocol'),
        ),
        migrations.AddField(
            model_name='service_base',
            name='provider',
            field=models.ForeignKey(to='service.Service_provider'),
        ),
        migrations.AddField(
            model_name='service_base',
            name='serve_tags',
            field=models.ManyToManyField(to='service.Service_tag', blank=True),
        ),
        migrations.AddField(
            model_name='service_base',
            name='serve_type',
            field=models.ForeignKey(to='service.Service_type'),
        ),
        migrations.AddField(
            model_name='service_base',
            name='status',
            field=models.ForeignKey(to='service.Service_status'),
        ),
        migrations.AddField(
            model_name='service_api',
            name='service',
            field=models.OneToOneField(related_name='rel_api', to='service.Service_base'),
        ),
        migrations.AddField(
            model_name='service_activepack',
            name='service',
            field=models.ForeignKey(related_name='rel_activepack', to='service.Service_base'),
        ),
    ]
