# Generated by Django 3.2.8 on 2021-10-21 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20211021_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='end',
            field=models.DateField(default='2021-10-11'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='start',
            field=models.DateField(default='2021-10=10'),
        ),
    ]