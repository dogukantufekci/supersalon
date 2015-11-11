# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='discounted_price',
            field=models.DecimalField(null=True, verbose_name='Discounted Price', blank=True, decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='service',
            name='remind_day_count_after_due_date',
            field=models.PositiveSmallIntegerField(default=12, verbose_name='Reminder Day Count Before After Date'),
        ),
    ]
