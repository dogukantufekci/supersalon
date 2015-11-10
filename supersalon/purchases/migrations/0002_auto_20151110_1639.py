# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professionals', '0001_initial'),
        ('visits', '0003_auto_20151110_1558'),
        ('purchases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPurchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('product', models.PositiveSmallIntegerField(verbose_name='Service', choices=[(0, 'Other'), ('Nashi Argan', ((1001, 'Color #2543 (Nashi Argan)'), (1002, 'Color #1231 (Nashi Argan)'))), ('Schwarzkopf', ((2001, 'Color #2543 (Schwarzkopf)'), (2002, 'Color #1231 (Schwarzkopf)')))])),
                ('count', models.PositiveSmallIntegerField(default=1, verbose_name='Count')),
                ('professional', models.ForeignKey(verbose_name='Professional', to='professionals.Professional')),
                ('visit', models.ForeignKey(verbose_name='Visit', to='visits.Visit')),
            ],
            options={
                'ordering': ('-visit', 'product'),
                'verbose_name': 'Product Purchase',
                'verbose_name_plural': 'Product Purchases',
            },
        ),
        migrations.AddField(
            model_name='servicepurchase',
            name='count',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Count'),
        ),
        migrations.AlterUniqueTogether(
            name='servicepurchase',
            unique_together=set([('visit', 'service')]),
        ),
        migrations.AlterUniqueTogether(
            name='productpurchase',
            unique_together=set([('visit', 'product')]),
        ),
    ]
