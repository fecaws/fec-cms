# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 21:12
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0072_auto_20170324_0544'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcepage',
            name='related_pages',
            field=wagtail.core.fields.StreamField((('related_pages', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock())),), blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resourcepage',
            name='sidebar_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
