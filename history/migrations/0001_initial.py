# Generated by Django 3.1.3 on 2021-04-08 16:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.TextField()),
                ('category', models.TextField()),
                ('content_number', models.TextField()),
                ('content_class', models.TextField()),
                ('date_time', models.TextField(default=datetime.datetime(2021, 4, 8, 16, 23, 42, 39393))),
            ],
        ),
    ]
