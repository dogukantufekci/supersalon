# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name of Service')),
                ('price', models.DecimalField(decimal_places=2, verbose_name='Price', max_digits=8)),
                ('due_period', models.PositiveSmallIntegerField(null=True, verbose_name='Due Period (in days)', blank=True)),
                ('reminder_day_count_before_due_date', models.PositiveSmallIntegerField(default=2, verbose_name='Reminder Day Count Before Due Date')),
                ('remind_day_count_after_due_date', models.PositiveSmallIntegerField(default=10, verbose_name='Reminder Day Count Before After Date')),
            ],
            options={
                'ordering': ('category', 'name'),
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Name of Service Category')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Service Category',
                'verbose_name_plural': 'Service Categories',
            },
        ),
        migrations.AddField(
            model_name='service',
            name='category',
            field=models.ForeignKey(to='services.ServiceCategory', verbose_name='Service Category', related_query_name='service', related_name='services'),
        ),
        migrations.AlterUniqueTogether(
            name='service',
            unique_together=set([('category', 'name')]),
        ),
    ]
