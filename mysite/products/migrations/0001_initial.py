# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuditData',
            fields=[
                ('host_id', models.AutoField(serialize=False, primary_key=True)),
                ('not_started_field', models.IntegerField(null=True, db_column='Not_Started_', blank=True)),
                ('in_progress', models.IntegerField(null=True, db_column='In_Progress', blank=True)),
                ('complete', models.IntegerField(null=True, db_column='Complete', blank=True)),
                ('process_not_started', models.IntegerField(null=True, db_column='Process_Not_Started', blank=True)),
                ('process_in_progress', models.IntegerField(null=True, db_column='Process_In_Progress', blank=True)),
                ('process_complete', models.IntegerField(null=True, db_column='Process_Complete', blank=True)),
                ('not_started', models.IntegerField(null=True, db_column='Not_Started', blank=True)),
                ('in_progress_nav', models.IntegerField(null=True, db_column='In_Progress_NAV', blank=True)),
                ('in_progress_malt', models.IntegerField(null=True, db_column='In_Progress_MALT', blank=True)),
                ('completed', models.IntegerField(null=True, db_column='Completed', blank=True)),
            ],
            options={
                'db_table': 'audit_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuditStatus',
            fields=[
                ('status_id', models.IntegerField(serialize=False, primary_key=True)),
                ('status_name', models.CharField(unique=True, max_length=50)),
                ('deleted', models.IntegerField()),
                ('date_created', models.DateTimeField()),
                ('date_updated', models.DateTimeField()),
            ],
            options={
                'db_table': 'audit_status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('device_type_id', models.AutoField(serialize=False, primary_key=True)),
                ('device_type_name', models.CharField(unique=True, max_length=20)),
                ('deleted', models.IntegerField()),
                ('date_created', models.DateTimeField()),
                ('date_updated', models.DateTimeField()),
            ],
            options={
                'db_table': 'device_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hosts',
            fields=[
                ('host_id', models.AutoField(serialize=False, primary_key=True)),
                ('host_name', models.CharField(unique=True, max_length=45)),
                ('ip_address', models.CharField(max_length=15, null=True, blank=True)),
                ('deleted', models.IntegerField()),
                ('date_created', models.DateTimeField()),
                ('date_updated', models.DateTimeField()),
            ],
            options={
                'db_table': 'hosts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('model_id', models.AutoField(serialize=False, primary_key=True)),
                ('model_name', models.CharField(unique=True, max_length=72)),
                ('deleted', models.IntegerField(null=True, blank=True)),
                ('date_created', models.DateTimeField()),
            ],
            options={
                'db_table': 'model',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(serialize=False, primary_key=True)),
                ('product_name', models.CharField(unique=True, max_length=10)),
                ('deleted', models.IntegerField(null=True, blank=True)),
                ('date_created', models.DateTimeField()),
            ],
            options={
                'db_table': 'products',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('site_id', models.AutoField(serialize=False, primary_key=True)),
                ('site_name', models.CharField(unique=True, max_length=72)),
                ('site_type', models.IntegerField()),
                ('deleted', models.IntegerField(null=True, blank=True)),
                ('date_created', models.DateTimeField()),
                ('date_updated', models.DateTimeField()),
            ],
            options={
                'db_table': 'site',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('vendor_id', models.AutoField(serialize=False, primary_key=True)),
                ('vendor_name', models.CharField(unique=True, max_length=72)),
                ('deleted', models.IntegerField(null=True, blank=True)),
                ('date_created', models.DateTimeField()),
            ],
            options={
                'db_table': 'vendor',
                'managed': False,
            },
        ),
    ]
