from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="наименование",
    )
    description = models.TextField(
        verbose_name="описание",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="catalog/image",
        blank=True,
        null=True,
        verbose_name="изображение",
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="категория",
        related_name="products",
    )
    price = models.IntegerField(
        verbose_name="цена за покупку",
        blank=True,
        null=True,
    )
    created_at = models.DateField(
        verbose_name="дата создания",
        blank=True,
        null=True,
    )
    updated_at = models.DateField(
        verbose_name="дата последнего изменения",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="наименование",
    )
    description = models.TextField(
        verbose_name="описание",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.name
