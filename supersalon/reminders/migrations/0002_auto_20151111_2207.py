# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professionals', '0001_initial'),
        ('services', '0001_initial'),
        ('reminders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerservicereminderrel',
            name='last_professional',
            field=models.ForeignKey(to='professionals.Professional', verbose_name='Last Professional'),
        ),
        migrations.AddField(
            model_name='customerservicereminderrel',
            name='service',
            field=models.ForeignKey(to='services.Service', verbose_name='Service'),
        ),
        migrations.AlterUniqueTogether(
            name='customerservicereminderrel',
            unique_together=set([('customer', 'service')]),
        ),
    ]
