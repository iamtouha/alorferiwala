from django.urls import path
from . import views

urlpatterns = [
    path('<int:product_id>/', views.index, name='order'),
    path('confirm/<int:product_id>', views.confirm, name='confirm'),
    path('sell/<int:product_id>', views.sell, name='sell'),
]