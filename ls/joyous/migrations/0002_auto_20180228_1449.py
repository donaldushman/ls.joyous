# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-28 01:49
from __future__ import unicode_literals

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('joyous', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='simpleeventpage',
            options={'verbose_name': 'Event Page'},
        ),
        migrations.AlterField(
            model_name='grouppage',
            name='content',
            field=wagtail.fields.RichTextField(blank=True, default='', help_text='An area of text for whatever you like'),
        ),
    ]
