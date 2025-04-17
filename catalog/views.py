from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, DeleteView, CreateView, UpdateView

from catalog.forms import ProductForm, ContactForm, ProductModeratorForm
from catalog.models import Product, Contact
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied


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


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    success_url = reverse_lazy('catalog:products_list')


    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner or self.request.user.has_perm(
            "catalog.remove_any_product"
        )

    def handle_no_permission(self):
        raise PermissionDenied


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('catalog:products_list')


    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('catalog:products_list')

    def get_form_class(self):
        if self.request.user.is_superuser:
            return ProductForm
        if self.request.user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied