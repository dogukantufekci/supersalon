# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerServiceReminderRel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('upcoming_reminder_date', models.DateField(verbose_name='Upcoming Service Due Reminder Date')),
                ('past_reminder_date', models.DateField(verbose_name='Past Service Due Reminder Date')),
                ('customer', models.ForeignKey(to='customers.Customer', verbose_name='Customer')),
            ],
            options={
                'ordering': ('upcoming_reminder_date',),
                'verbose_name': 'CustomerServiceReminderRel',
                'verbose_name_plural': 'CustomerServiceReminderRel',
            },
        ),
    ]
