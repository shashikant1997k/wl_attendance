# Generated by Django 3.2.3 on 2021-05-21 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0005_auto_20210521_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='timing_in',
            field=models.TimeField(default=''),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='timing_out',
            field=models.TimeField(default=''),
        ),
    ]