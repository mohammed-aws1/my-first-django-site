# Generated by Django 3.0.4 on 2020-04-21 09:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0025_auto_20200419_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 21, 12, 16, 33, 654336)),
        ),
    ]
