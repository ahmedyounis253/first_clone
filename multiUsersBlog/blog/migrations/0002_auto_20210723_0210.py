# Generated by Django 3.2.5 on 2021-07-23 00:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 23, 0, 10, 21, 703049, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 23, 0, 10, 21, 660827, tzinfo=utc)),
        ),
    ]