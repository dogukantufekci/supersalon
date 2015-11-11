# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('visit_date', models.DateField(default=django.utils.timezone.now, verbose_name='Visit Date')),
                ('arrival_time', models.TimeField(null=True, verbose_name='Arrival Time', blank=True)),
                ('departure_time', models.TimeField(null=True, verbose_name='Departure Time', blank=True)),
                ('female_guest_count', models.PositiveSmallIntegerField(default=0, verbose_name='Female Guest Count')),
                ('male_guest_count', models.PositiveSmallIntegerField(default=0, verbose_name='Male Guest Count')),
                ('child_guest_count', models.PositiveSmallIntegerField(default=0, verbose_name='Child Guest Count')),
                ('payment_method', models.PositiveSmallIntegerField(choices=[(1, 'Cash'), (2, 'Credit Card'), (3, 'Cash and Credit Card')], verbose_name='Payment Method')),
                ('total_payment_amount', models.DecimalField(decimal_places=2, verbose_name='Total Payment Amount', max_digits=8)),
                ('notes', models.TextField(verbose_name='Notes', blank=True)),
                ('customer', models.ForeignKey(to='customers.Customer', verbose_name='Customer')),
            ],
            options={
                'ordering': ('-visit_date',),
                'verbose_name': 'Visit',
                'verbose_name_plural': 'Visits',
            },
        ),
    ]
