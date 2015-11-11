# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0003_auto_20151111_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='productpurchase',
            name='notes',
            field=models.TextField(blank=True, verbose_name='Notes'),
        ),
        migrations.AddField(
            model_name='servicepurchase',
            name='notes',
            field=models.TextField(blank=True, verbose_name='Notes'),
        ),
    ]
