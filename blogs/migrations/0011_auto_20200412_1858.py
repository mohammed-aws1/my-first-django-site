# Generated by Django 3.0.4 on 2020-04-12 15:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0010_auto_20200412_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 12, 18, 58, 47, 924800)),
        ),
    ]
