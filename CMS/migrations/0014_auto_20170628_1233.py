# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 12:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('wagtailcore', '0033_remove_golive_expiry_help_text'),
        ('CMS', '0013_data_visuals'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='visuals',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='Data',
        ),
        migrations.DeleteModel(
            name='Visuals',
        ),
    ]
