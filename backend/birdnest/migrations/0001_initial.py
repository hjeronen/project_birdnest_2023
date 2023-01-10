# Generated by Django 4.1.5 on 2023-01-10 09:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pilot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pilotId', models.CharField(max_length=100)),
                ('firstName', models.TextField()),
                ('lastName', models.TextField()),
                ('phoneNumber', models.CharField(max_length=100)),
                ('createdDt', models.DateTimeField(default=datetime.datetime.now)),
                ('email', models.CharField(max_length=100)),
                ('closest_distance', models.FloatField(default=100000)),
                ('last_seen', models.DateTimeField(default=datetime.datetime.now)),
                ('drone_serial_number', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'db_table': 'pilots',
                'ordering': ['last_seen'],
            },
        ),
    ]
