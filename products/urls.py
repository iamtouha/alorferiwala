from django.urls import path
from . import views

urlpatterns = [
    path('<int:product_id>/', views.product, name= 'product'),
    path('add/', views.add_product, name = 'add_product'),
]