# Generated by Django 2.2.1 on 2020-04-29 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200428_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myblog',
            name='image',
        ),
    ]
