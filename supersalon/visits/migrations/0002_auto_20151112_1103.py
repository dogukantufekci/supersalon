# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visit',
            name='payment_method',
        ),
        migrations.AddField(
            model_name='visit',
            name='card_payment_amount',
            field=models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='Card Payment Amount'),
        ),
        migrations.AddField(
            model_name='visit',
            name='cash_payment_amount',
            field=models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='Cash Payment Amount'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='total_payment_amount',
            field=models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='Total Payment Amount'),
        ),
    ]
