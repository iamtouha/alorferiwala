from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from django.contrib.auth.models import User
from .models import Order
from datetime import datetime
fraction = 0.8

def index(request, product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=product_id)
        if product.status == 'OS':
            price = product.init_price * fraction ** product.sold_count
            owner = product.current_owner
            order = Order(
                product = product,
                price = price,
                owned_by = owner,
                ordered_by = request.user,
            ) 
            Product.objects.filter(pk=product_id).update(
                status = 'OD',
                updated_at = datetime.now()
            )
            order.save()
            return redirect('profile')
        else:
            return redirect('index')
    else:
        messages.error(request, 'Please Login first!')
        return redirect('login')
