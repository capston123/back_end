# Generated by Django 3.1.1 on 2021-03-23 15:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtoons', '0002_auto_20210303_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daum',
            name='date',
            field=models.TextField(default=datetime.date(2021, 3, 24)),
        ),
        migrations.AlterField(
            model_name='naver',
            name='date',
            field=models.TextField(default=datetime.date(2021, 3, 24)),
        ),
    ]
