from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from django.contrib.auth.models import User
from .models import Order
from datetime import datetime
from django.contrib import messages
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
                current_price=price,
                status = 'OD',
                ordered_by = request.user,
                updated_at = datetime.now()
            )
            order.save()
            return redirect('profile')
        else:
            return redirect('index')
    else:
        messages.error(request, 'Please Login first!')
        return redirect('login')

def sell(request, product_id):
    if request.user.is_authenticated:
        place_order = Product.objects.filter(pk = product_id, current_owner = request.user)
        place_order.update(
            status = 'OS',
            updated_at = datetime.now()
        )
        messages.success(request, 'product added on sale')
        return redirect('profile')
    else:
        messages.success(request, 'please login first')
        return redirect('login')


def confirm(request, product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=product_id)
        if product.current_owner == request.user and product.status=='OD':
            Product.objects.filter(pk = product_id).update(
                current_owner = product.ordered_by,
                ordered_by = None,
                current_price = product.init_price * fraction ** (product.sold_count + 1),
                sold_count = product.sold_count + 1,
                status = 'SD',
                updated_at = datetime.now()
            )
            Order.objects.filter(product=product, is_confirmed=False).update(
                is_confirmed=True
            )
            messages.success(request, 'product sold successfully')
            return redirect('profile')
        else:
            messages.error(request, 'Something went wrong, Please try again')
            return redirect('profile')