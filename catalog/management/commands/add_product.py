from django.core.management.base import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):
    help = 'Add test books to the database'

    def handle(self, *args, **kwargs):
        category, _ = Category.objects.get_or_create(name='Смартфон', description='портативное компьютерное устройство,которое сочетает в себе функции мобильного телефона и функции портативного компьютера.',)

        products = [
            {'name': 'Samsung', 'description': 'S24 Ulta', 'price': '18000', 'category': category},
            {'name': 'Iphone', 'description': '15 PRO MAX', 'price': '200000', 'category': category},
        ]

        for book_data in products:
            product, created = Product.objects.get_or_create(**book_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Smartphone successfully added: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'The smartphone already exists: {product.name}'))