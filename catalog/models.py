from django.conf import settings
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


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
        upload_to="product/image",
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
    is_available = models.BooleanField(
        default=False,
        verbose_name="доступность в каталоге",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Владелец",
        related_name="products",
        null=True,
    )

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
            ("remove_any_product", "Remove any product"),
        ]

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


class Contact(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Имя и Фамилия",
        help_text="Введите ваше имя и фамилию",
    )
    phone = PhoneNumberField(
        verbose_name="Номер телефона",
        help_text="Введите описание категории",
        unique=True,
    )
    message = models.TextField(
        verbose_name="Сообщение",
        help_text="Введите ваше сообщение",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ["phone", "name", "message"]

    def __str__(self):
        return self.phone