# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-01 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0007_auto_20161012_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveSmallIntegerField(choices=[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')], default=1),
        ),
        migrations.AlterField(
            model_name='stripecustomer',
            name='customer_id',
            field=models.CharField(default='', max_length=18),
            preserve_default=False,
        ),
    ]