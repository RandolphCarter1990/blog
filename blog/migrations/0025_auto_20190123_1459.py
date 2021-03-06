# Generated by Django 2.1.5 on 2019-01-23 11:59

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20190123_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='preview_image_2_cropping',
            field=image_cropping.fields.ImageRatioField('preview_image_2', '150x150', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='preview image 2 cropping'),
        ),
        migrations.AddField(
            model_name='article',
            name='preview_image_3_cropping',
            field=image_cropping.fields.ImageRatioField('preview_image_3', '150x150', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='preview image 3 cropping'),
        ),
        migrations.AddField(
            model_name='article',
            name='preview_image_4_cropping',
            field=image_cropping.fields.ImageRatioField('preview_image_1', '150x150', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='preview image 4 cropping'),
        ),
    ]
