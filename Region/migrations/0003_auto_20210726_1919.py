# Generated by Django 3.1.5 on 2021-07-26 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Region', '0002_auto_20210724_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='display',
            field=models.BooleanField(default=False),
        ),
    ]