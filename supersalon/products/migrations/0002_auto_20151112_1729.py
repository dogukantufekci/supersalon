# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='due_period',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Due Period (in days)', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='reminder_day_count_after_due_date',
            field=models.PositiveSmallIntegerField(verbose_name='Reminder Day Count Before After Date', default=12),
        ),
        migrations.AddField(
            model_name='product',
            name='reminder_day_count_before_due_date',
            field=models.PositiveSmallIntegerField(verbose_name='Reminder Day Count Before Due Date', default=2),
        ),
    ]
