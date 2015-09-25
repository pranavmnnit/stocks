# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stock_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('cur_price', models.FloatField(default=0)),
                ('predict_price', models.FloatField(default=0)),
                ('Rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
            ],
        ),
        migrations.CreateModel(
            name='Trader',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('org_name', models.CharField(max_length=100)),
                ('mobile', models.IntegerField(default=0)),
                ('e_mail', models.CharField(max_length=100)),
                ('points', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Viewer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('mobile', models.IntegerField(default=0)),
                ('e_mail', models.CharField(max_length=100)),
                ('credits', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='stock',
            name='trader',
            field=models.ForeignKey(to='trading.Trader'),
        ),
    ]
