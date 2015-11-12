# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20151112_1729'),
        ('customers', '0002_auto_20151112_1103'),
        ('reminders', '0002_auto_20151111_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProductReminderRel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('upcoming_reminder_date', models.DateField(verbose_name='Upcoming Product Due Reminder Date')),
                ('past_reminder_date', models.DateField(verbose_name='Past Product Due Reminder Date')),
                ('customer', models.ForeignKey(verbose_name='Customer', to='customers.Customer')),
                ('service', models.ForeignKey(verbose_name='Product', to='products.Product')),
            ],
            options={
                'verbose_name': 'Customer Product Reminder Rel',
                'verbose_name_plural': 'Customer Product Reminder Rels',
                'ordering': ('upcoming_reminder_date',),
            },
        ),
        migrations.AlterModelOptions(
            name='customerservicereminderrel',
            options={'verbose_name': 'Customer Service Reminder Rel', 'verbose_name_plural': 'Customer Service Reminder Rels', 'ordering': ('upcoming_reminder_date',)},
        ),
        migrations.RemoveField(
            model_name='customerservicereminderrel',
            name='last_professional',
        ),
        migrations.AlterUniqueTogether(
            name='customerproductreminderrel',
            unique_together=set([('customer', 'service')]),
        ),
    ]
