# Generated by Django 3.1.1 on 2021-03-03 14:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtoons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daum',
            name='date',
            field=models.TextField(default=datetime.date(2021, 3, 3)),
        ),
        migrations.AlterField(
            model_name='naver',
            name='date',
            field=models.TextField(default=datetime.date(2021, 3, 3)),
        ),
    ]