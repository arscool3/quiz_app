# Generated by Django 3.2.8 on 2021-10-22 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20211022_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='end',
            field=models.DateTimeField(default='2040-10-11'),
        ),
    ]