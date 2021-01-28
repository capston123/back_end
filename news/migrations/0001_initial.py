# Generated by Django 3.1.5 on 2021-01-24 10:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.TextField()),
                ('image', models.TextField()),
                ('category', models.TextField()),
                ('date', models.TextField(default=datetime.date(2021, 1, 24))),
            ],
        ),
    ]
