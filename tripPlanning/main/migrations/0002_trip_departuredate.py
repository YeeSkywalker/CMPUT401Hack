# Generated by Django 4.1.5 on 2023-01-15 09:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='departureDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 15, 9, 29, 29, 64354)),
        ),
    ]
