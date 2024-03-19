from django import forms
from .models import Prodect, User

class ProdectForm(forms.ModelForm):
    class Meta:
        model = Prodect
        fields = ['name', 'description', 'price', 'category', 'photo']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_name','password']
