# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professionals', '0001_initial'),
        ('services', '0001_initial'),
        ('purchases', '0001_initial'),
        ('products', '0001_initial'),
        ('visits', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicepurchase',
            name='professional',
            field=models.ForeignKey(to='professionals.Professional', verbose_name='Professional', related_query_name='service_purchase', related_name='service_purchases'),
        ),
        migrations.AddField(
            model_name='servicepurchase',
            name='service',
            field=models.ForeignKey(to='services.Service', verbose_name='Service', related_query_name='product_purchase', related_name='product_purchases'),
        ),
        migrations.AddField(
            model_name='servicepurchase',
            name='visit',
            field=models.ForeignKey(to='visits.Visit', verbose_name='Visit', related_query_name='service_purchase', related_name='service_purchases'),
        ),
        migrations.AddField(
            model_name='productpurchase',
            name='product',
            field=models.ForeignKey(to='products.Product', verbose_name='Product', related_query_name='product_purchase', related_name='product_purchases'),
        ),
        migrations.AddField(
            model_name='productpurchase',
            name='visit',
            field=models.ForeignKey(to='visits.Visit', verbose_name='Visit', related_query_name='product_purchase', related_name='product_purchases'),
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
