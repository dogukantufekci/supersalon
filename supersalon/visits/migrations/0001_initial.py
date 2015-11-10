# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('visit_date', models.DateField(verbose_name='Visit Date', default=datetime.date(2015, 11, 10))),
                ('visit_time', models.TimeField(blank=True, null=True, verbose_name='Visit Time')),
                ('female_guest_count', models.PositiveSmallIntegerField(verbose_name='Female Guest Count', default=0)),
                ('male_guest_count', models.PositiveSmallIntegerField(verbose_name='Male Guest Count', default=0)),
                ('child_guest_count', models.PositiveSmallIntegerField(verbose_name='Child Guest Count', default=0)),
                ('notes', models.TextField(blank=True, verbose_name='Notes')),
                ('customer', models.ForeignKey(to='customers.Customer', verbose_name='Customer')),
            ],
        ),
    ]
