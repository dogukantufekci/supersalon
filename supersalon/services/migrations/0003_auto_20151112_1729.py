# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20151111_2313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='remind_day_count_after_due_date',
            new_name='reminder_day_count_after_due_date',
        ),
        migrations.RemoveField(
            model_name='service',
            name='discounted_price',
        ),
    ]
