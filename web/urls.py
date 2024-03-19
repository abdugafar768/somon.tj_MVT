from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-product/', ProdectCreateView.as_view(), name='add_product'),
    path('list/',ProdectListView.as_view(),name='prodectlist'),
    path('', UserLoginView.as_view(), name='register_user'),
    path('delete/<int:pk>/', ProdectDeleteView.as_view(), name='delete_product'),
    path('products/', ProdectListView.as_view(), name='product_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
