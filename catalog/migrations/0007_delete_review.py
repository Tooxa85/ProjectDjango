# Generated by Django 4.2.2 on 2025-04-17 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0006_review"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Review",
        ),
    ]
