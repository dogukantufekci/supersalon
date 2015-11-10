# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0003_auto_20151110_1558'),
        ('professionals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicePurchase',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('service', models.PositiveSmallIntegerField(choices=[(0, 'Other'), ('Hair (Woman)', ((101, 'Hair Cut'), (102, 'Hair Coloring'))), ('Nail (Woman)', ((201, 'Manicure'), (202, 'Pedicure')))], verbose_name='Service')),
                ('professional', models.ForeignKey(to='professionals.Professional', verbose_name='Professional')),
                ('visit', models.ForeignKey(to='visits.Visit', verbose_name='Visit')),
            ],
            options={
                'ordering': ('-visit', 'service'),
                'verbose_name': 'Service Purchase',
                'verbose_name_plural': 'Service Purchases',
            },
        ),
    ]
