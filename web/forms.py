from django import forms
from .models import Product, Userr


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'photo']

        
class UserForm(forms.ModelForm):
    class Meta:
        model = Userr
        fields = ['user_name','password']
