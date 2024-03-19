from django.shortcuts import render, redirect
from .models import Prodect, User
from django.views import generic
from django.urls import reverse_lazy

class UserLoginView(generic.CreateView):
    model = User
    template_name = 'login.html'
    fields = '__all__'
    success_url = reverse_lazy('prodect.html')


class ProdectListView(generic.ListView):
    model = Prodect
    template_name = 'index.html'
    context_object_name = 'products'

class ProdectCreateView(generic.CreateView):
    model = Prodect
    template_name = 'prodect.html'
    fields = '__all__'
    success_url = reverse_lazy('index.html')
    
class ProdectDeleteView(generic.DeleteView):
    model = Prodect
    template_name = 'delete_product.html'
    success_url = reverse_lazy('product_list')
