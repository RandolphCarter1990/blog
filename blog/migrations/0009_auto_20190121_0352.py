# Generated by Django 2.1.5 on 2019-01-21 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190121_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(verbose_name='Дата публикации'),
        ),
    ]