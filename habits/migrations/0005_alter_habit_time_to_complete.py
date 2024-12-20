# Generated by Django 5.1.3 on 2024-11-19 11:59

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0004_alter_habit_time_to_complete"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="time_to_complete",
            field=models.DurationField(
                default=datetime.timedelta(seconds=120),
                verbose_name="Длительность выполнения привычки",
            ),
        ),
    ]
