# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0004_auto_20151111_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productpurchase',
            name='free_amount',
        ),
        migrations.RemoveField(
            model_name='productpurchase',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='servicepurchase',
            name='is_free',
        ),
        migrations.RemoveField(
            model_name='servicepurchase',
            name='notes',
        ),
        migrations.AddField(
            model_name='productpurchase',
            name='discount_notes',
            field=models.TextField(verbose_name='Discount Notes', blank=True),
        ),
        migrations.AddField(
            model_name='productpurchase',
            name='discounted_unit_price',
            field=models.DecimalField(max_digits=8, decimal_places=2, null=True, verbose_name='Discounted Unit Price', blank=True),
        ),
        migrations.AddField(
            model_name='servicepurchase',
            name='discount_notes',
            field=models.TextField(verbose_name='Discount Notes', blank=True),
        ),
        migrations.AddField(
            model_name='servicepurchase',
            name='discounted_unit_price',
            field=models.DecimalField(max_digits=8, decimal_places=2, null=True, verbose_name='Discounted Unit Price', blank=True),
        ),
    ]
