# Generated by Django 2.2.1 on 2020-03-31 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_myblog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myblog',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
