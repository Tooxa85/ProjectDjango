from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactsView, ProductDeleteView, ProductCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='products_detail'),
    path('product_delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('product_form/', ProductCreateView.as_view(), name='product_form')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
