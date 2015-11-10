# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0002_auto_20151110_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productpurchase',
            name='professional',
        ),
        migrations.RemoveField(
            model_name='servicepurchase',
            name='count',
        ),
    ]
