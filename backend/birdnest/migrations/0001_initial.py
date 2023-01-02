# Generated by Django 4.1.5 on 2023-01-02 17:23

from django.db import migrations, models
import django.utils.timezone


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
                ('createdDt', models.DateTimeField(default=django.utils.timezone.now)),
                ('email', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'pilots',
            },
        ),
    ]
