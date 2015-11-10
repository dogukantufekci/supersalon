# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0002_auto_20151110_1539'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='visit',
            options={'verbose_name_plural': 'Visits', 'verbose_name': 'Visit', 'ordering': ('-visit_date',)},
        ),
        migrations.AddField(
            model_name='visit',
            name='payment_method',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Payment Method', choices=[(1, 'Cash'), (2, 'Credit Card'), (3, 'Cash and Credit Card')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visit',
            name='total_payment_amount',
            field=models.DecimalField(default=0, decimal_places=2, verbose_name='Total Payment Amount', max_digits=8),
            preserve_default=False,
        ),
    ]
