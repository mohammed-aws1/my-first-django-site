# Generated by Django 3.0.4 on 2020-04-12 11:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0009_auto_20200412_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 12, 11, 49, 35, 179593, tzinfo=utc)),
        ),
    ]