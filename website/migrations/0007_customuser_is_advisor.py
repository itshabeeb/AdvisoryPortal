# Generated by Django 5.0.1 on 2024-04-06 14:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0006_workshops"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="is_advisor",
            field=models.BooleanField(default=False),
        ),
    ]
