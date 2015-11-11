# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPurchase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('amount', models.PositiveSmallIntegerField(default=1, verbose_name='Amount')),
            ],
            options={
                'ordering': ('-visit', 'product'),
                'verbose_name': 'Product Purchase',
                'verbose_name_plural': 'Product Purchases',
            },
        ),
        migrations.CreateModel(
            name='ServicePurchase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
            ],
            options={
                'ordering': ('-visit', 'service'),
                'verbose_name': 'Service Purchase',
                'verbose_name_plural': 'Service Purchases',
            },
        ),
    ]
