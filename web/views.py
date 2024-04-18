from django.shortcuts import render, redirect
from .models import Product, Userr , Basket
from django.views import generic
from django.urls import reverse_lazy


class ProductListView(generic.ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'

class ProductCreateView(generic.CreateView):
    model = Product
    template_name = 'prodect.html'
    fields = '__all__'
    success_url = reverse_lazy('product_list')
    
class ProductDeleteView(generic.DeleteView):
    model = Product
    template_name = 'delete_product.html'
    success_url = reverse_lazy('product_list')

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'product_detail.html'


class BasketCreateView(generic.CreateView):
    model = Basket
    fields = '__all__'
    template_name = 'basket_create.html'
    success_url = reverse_lazy('basket_list')

class BasketListView(generic.ListView):
    model = Basket
    template_name = 'basket_list.html'
    context_object_name = 'basket_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_price = 0
        basket_items = context['basket_list']
        for basket in basket_items:
            product = basket.product
            total_price += product.price
        context['total_price'] = total_price
        return context

    
