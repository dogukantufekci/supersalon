# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0002_auto_20151111_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='productpurchase',
            name='free_amount',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Free Amount'),
        ),
        migrations.AddField(
            model_name='servicepurchase',
            name='is_free',
            field=models.BooleanField(default=False, verbose_name='Is Free'),
        ),
    ]
