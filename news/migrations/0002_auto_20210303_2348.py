# Generated by Django 3.1.1 on 2021-03-03 14:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='title',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.TextField(default=datetime.date(2021, 3, 3)),
        ),
    ]
