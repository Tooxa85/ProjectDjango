from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product, Contact


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'


class ContactsView(TemplateView):
    model = Contact
    fields = ['name', 'phone', 'message']
    template_name = 'products/contacts.html'
