# Generated by Django 5.1.3 on 2024-11-19 10:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0002_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Хозяин привычки",
            ),
        ),
        migrations.AlterField(
            model_name="habit",
            name="periodicity",
            field=models.CharField(
                choices=[("DAY", "Day"), ("WEEK", "Week")],
                default="Day",
                max_length=10,
                verbose_name="Периодичность привычки",
            ),
        ),
    ]
