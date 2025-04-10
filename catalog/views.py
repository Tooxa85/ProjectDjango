from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, DeleteView, CreateView

from catalog.forms import ProductForm, ContactForm
from catalog.models import Product, Contact
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductListView(ListView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_list.html'


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_detail.html'


class ContactsView(TemplateView):
    model = Contact
    form_class = ContactForm
    template_name = 'products/contacts.html'


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    success_url = reverse_lazy('catalog:products_list')


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('catalog:products_list')


