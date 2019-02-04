# Generated by Django 2.1.5 on 2019-01-23 12:29

import blog.models
from django.db import migrations
import optimized_image.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20190123_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='cover_image',
            field=optimized_image.fields.OptimizedImageField(blank='True', upload_to=blog.models.Article.get_upload_path, verbose_name='Заглавная картинка'),
        ),
        migrations.AlterField(
            model_name='article',
            name='preview_image_1',
            field=optimized_image.fields.OptimizedImageField(blank='True', upload_to=blog.models.Article.get_upload_path, verbose_name='Предпросмотр 1'),
        ),
        migrations.AlterField(
            model_name='article',
            name='preview_image_2',
            field=optimized_image.fields.OptimizedImageField(blank='True', upload_to=blog.models.Article.get_upload_path, verbose_name='Предпросмотр 2'),
        ),
        migrations.AlterField(
            model_name='article',
            name='preview_image_3',
            field=optimized_image.fields.OptimizedImageField(blank='True', upload_to=blog.models.Article.get_upload_path, verbose_name='Предпросмотр 3'),
        ),
        migrations.AlterField(
            model_name='article',
            name='preview_image_4',
            field=optimized_image.fields.OptimizedImageField(blank='True', upload_to=blog.models.Article.get_upload_path, verbose_name='Предпросмотр 4'),
        ),
    ]