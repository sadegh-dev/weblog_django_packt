# Generated by Django 3.1.2 on 2020-10-18 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fblog', '0005_auto_20201018_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='count_viewer',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
