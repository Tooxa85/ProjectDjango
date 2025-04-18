# Generated by Django 5.1.6 on 2025-02-25 20:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, verbose_name="наименование")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="описание"),
                ),
            ],
            options={
                "verbose_name": "категория",
                "verbose_name_plural": "категории",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, verbose_name="наименование")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="описание"),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="catalog/image",
                        verbose_name="изображение",
                    ),
                ),
                (
                    "price",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="цена за покупку"
                    ),
                ),
                (
                    "created_at",
                    models.DateField(
                        blank=True, null=True, verbose_name="дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateField(
                        blank=True, null=True, verbose_name="дата последнего изменения"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="products",
                        to="catalog.category",
                        verbose_name="категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "продукт",
                "verbose_name_plural": "продукты",
            },
        ),
    ]