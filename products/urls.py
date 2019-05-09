from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'products'),
    path('<int:product_id>/', views.product, name= 'product'),
    path('search/', views.search, name = 'search'),
    path('add/', views.add_product, name = 'add_product'),
]