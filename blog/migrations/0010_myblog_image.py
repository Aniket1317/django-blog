# Generated by Django 2.2.1 on 2020-04-28 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200428_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='myblog',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='image/'),
        ),
    ]
