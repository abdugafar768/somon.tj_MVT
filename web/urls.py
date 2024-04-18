from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-product/', ProductCreateView.as_view(), name='add_product'),
    path('list/',ProductListView.as_view(),name='prodectlist'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('basket/create/', BasketCreateView.as_view(), name='basket_create'),
    path('basket/list/', BasketListView.as_view(), name='basket_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
