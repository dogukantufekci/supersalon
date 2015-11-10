# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(default='customers/placeholder.jpg', max_length=255, upload_to='customers', verbose_name='Photo')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('birth_date', models.DateField(blank=True, verbose_name='Birth Date')),
                ('gender', models.CharField(choices=[('f', 'Female'), ('m', 'Male')], max_length=1, blank=True, verbose_name='Gender')),
                ('mobile_phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, blank=True, verbose_name='Mobile Phone Number')),
                ('email', models.EmailField(max_length=254, blank=True, verbose_name='Email')),
                ('last_visit', models.DateField(blank=True, null=True, verbose_name='Last Visit')),
            ],
        ),
    ]
