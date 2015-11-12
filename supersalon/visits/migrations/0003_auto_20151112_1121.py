# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0002_auto_20151112_1103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visit',
            name='card_payment_amount',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='cash_payment_amount',
        ),
        migrations.AlterField(
            model_name='visit',
            name='total_payment_amount',
            field=models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Total Payment Amount'),
        ),
    ]
