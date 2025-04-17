from django.core.cache import cache

from catalog.models import Product, Category
from config.settings import CACHE_ENABLED

def get_products_from_cache():
    """Получает данные из кэша, если кэш пуст, получает данные из бд"""
    if not CACHE_ENABLED:
        return Product.objects.all()

    key = 'products_list'
    products = cache.get(key)

    if products is not None:
        return products

    products = Product.objects.all()
    cache.set(key, products)
    return products


def get_products_by_category(category_id):

    if not CACHE_ENABLED:
        return Product.objects.filter(category_id=category_id)
    key = f'products_by_category_{category_id}'
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.filter(category=Category.objects.get(pk=category_id))
    cache.set(key, products, 60)
    return products