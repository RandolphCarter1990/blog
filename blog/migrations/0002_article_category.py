# Generated by Django 2.1.5 on 2019-01-18 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(max_length=16, null='true'),
            preserve_default='true',
        ),
    ]
