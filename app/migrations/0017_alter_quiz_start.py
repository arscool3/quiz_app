# Generated by Django 3.2.8 on 2021-10-22 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_quiz_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='start',
            field=models.DateTimeField(default='1024-10-10'),
        ),
    ]