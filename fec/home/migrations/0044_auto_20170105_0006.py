# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 00:06
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0043_merge_20161230_0122'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcepage',
            name='breadcrumb_style',
            field=models.CharField(choices=[('primary', 'Blue'), ('secondary', 'Red')], default='primary', max_length=255),
        ),
        migrations.AlterField(
            model_name='resourcepage',
            name='citations',
            field=wagtail.core.fields.StreamField((('citations', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('label', wagtail.core.blocks.CharBlock()), ('content', wagtail.core.blocks.RichTextBlock(help_text='Use Shift + Enter to add line breaks between citation and description')))))),), null=True),
        ),
        migrations.AlterField(
            model_name='resourcepage',
            name='sections',
            field=wagtail.core.fields.StreamField((('sections', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=True)), ('hide_title', wagtail.core.blocks.BooleanBlock(help_text='Should the section title be displayed?', required=False)), ('content', wagtail.core.blocks.StreamBlock((('text', wagtail.core.blocks.RichTextBlock(blank=False, icon='pilcrow', null=False, required=False)), ('documents', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('url', wagtail.core.blocks.URLBlock()), ('text', wagtail.core.blocks.CharBlock()))), icon='doc-empty', template='blocks/section-documents.html')), ('contact_info', wagtail.core.blocks.StructBlock((('label', wagtail.core.blocks.CharBlock(icon='title', required=False)), ('contact_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('item_label', wagtail.core.blocks.CharBlock(required=True)), ('item_icon', wagtail.core.blocks.ChoiceBlock(choices=[('email', 'Email'), ('fax', 'Fax'), ('hand', 'Hand delivery'), ('phone', 'Phone'), ('mail', 'Mail')])), ('item_info', wagtail.core.blocks.RichTextBlock(required=True))))))))), ('internal_button', wagtail.core.blocks.StructBlock((('internal_page', wagtail.core.blocks.PageChooserBlock()), ('text', wagtail.core.blocks.CharBlock())))), ('external_button', wagtail.core.blocks.StructBlock((('url', wagtail.core.blocks.URLBlock()), ('text', wagtail.core.blocks.CharBlock()))))))), ('aside', wagtail.core.blocks.StreamBlock((('title', wagtail.core.blocks.CharBlock(icon='title', required=False)), ('document', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('url', wagtail.core.blocks.URLBlock()), ('text', wagtail.core.blocks.CharBlock())))), ('link', wagtail.core.blocks.StructBlock((('link_type', wagtail.core.blocks.ChoiceBlock(choices=[('search', 'Search'), ('calendar', 'Calendar')], help_text='Set an icon', icon='link', required=False)), ('url', wagtail.core.blocks.URLBlock()), ('text', wagtail.core.blocks.CharBlock(required=True)), ('coming_soon', wagtail.core.blocks.BooleanBlock(required=False)))))), icon='placeholder', template='blocks/section-aside.html'))))),), null=True),
        ),
    ]
