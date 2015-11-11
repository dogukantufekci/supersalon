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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('photo', models.ImageField(default='customers/placeholder.jpg', upload_to='customers', max_length=255, verbose_name='Photo')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('birth_date', models.DateField(null=True, verbose_name='Birth Date', blank=True)),
                ('gender', models.CharField(default='u', choices=[('u', 'Unknown'), ('f', 'Female'), ('m', 'Male')], max_length=1, verbose_name='Gender')),
                ('mobile_phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, verbose_name='Mobile Phone Number', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail', blank=True)),
                ('last_visit', models.DateField(null=True, verbose_name='Last Visit', blank=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customer',
            },
        ),
    ]
