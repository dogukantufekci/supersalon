# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name of Product')),
                ('price', models.DecimalField(decimal_places=2, verbose_name='Price', max_digits=8)),
            ],
            options={
                'ordering': ('category', 'name'),
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Name of Product Category')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Product Category',
                'verbose_name_plural': 'Product Categories',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(to='products.ProductCategory', verbose_name='Product Category', related_query_name='product', related_name='products'),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set([('category', 'name')]),
        ),
    ]
