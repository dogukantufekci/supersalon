# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='drink',
            field=models.CharField(blank=True, max_length=128, verbose_name='Drink'),
        ),
        migrations.AddField(
            model_name='customer',
            name='engagement_date',
            field=models.DateField(blank=True, null=True, verbose_name='Engagement Date'),
        ),
        migrations.AddField(
            model_name='customer',
            name='magazine',
            field=models.CharField(blank=True, max_length=128, verbose_name='Magazine'),
        ),
        migrations.AddField(
            model_name='customer',
            name='newspaper',
            field=models.CharField(blank=True, max_length=128, verbose_name='Newspaper'),
        ),
        migrations.AddField(
            model_name='customer',
            name='notes',
            field=models.TextField(blank=True, verbose_name='Notes'),
        ),
        migrations.AddField(
            model_name='customer',
            name='relationship_status',
            field=models.CharField(max_length=1, default='u', choices=[('u', 'Unknown'), ('s', 'Single'), ('e', 'Engaged'), ('m', 'Married')], verbose_name='Relationship Status'),
        ),
        migrations.AddField(
            model_name='customer',
            name='wedding_date',
            field=models.DateField(blank=True, null=True, verbose_name='Wedding Date'),
        ),
    ]
