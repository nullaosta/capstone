# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 22:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EconomicSnapshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptor', models.CharField(blank=True, editable=False, max_length=50)),
                ('year', models.PositiveSmallIntegerField()),
                ('country', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('IP', 'Intellectual Property Sales'), ('PAT', 'Patent Applications'), ('GNI', 'Gross National Income'), ('GDP', 'Gross Domestic Product'), ('FDI', 'Foreign Direct Investment')], max_length=100)),
                ('value', models.FloatField(blank=True)),
                ('description', models.CharField(max_length=500)),
                ('source_url', models.URLField(blank=True, null=True)),
                ('country_code', models.CharField(blank=True, max_length=3, null=True)),
            ],
        ),
    ]
