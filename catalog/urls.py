from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactsView, ProductDeleteView, ProductCreateView, \
    ProductUpdateView, ProductsByCategoryView
from django.views.decorators.cache import cache_page

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='products_detail'),
    path('product_delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('product_form/', ProductCreateView.as_view(), name='product_form'),
    path('product_update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('category/<int:pk>/', ProductsByCategoryView.as_view(), name='products_by_category')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
