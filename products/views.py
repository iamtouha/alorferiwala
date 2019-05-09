from django.shortcuts import get_object_or_404, render, redirect
from .models import Product
from django.contrib import messages
from .forms import ProductInputForm
from .categories import categories

def index(request):
    return render(request, 'products/products.html')

def product(request, product_id):
    product = get_object_or_404(Product, pk = product_id)
    for category in categories:
        if category[0] == product.category:
            product.category = category[1]
            break
        
    context = {
        'product': product,
    }
    return render(request, 'products/product.html', context)

def search(request):
    return render(request, 'products/search.html')

def add_product(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = ProductInputForm(request.POST, request.FILES)
            if form.is_valid():
                title = form.cleaned_data['title']
                author = form.cleaned_data['author']
                publisher = form.cleaned_data['publisher']
                category = form.cleaned_data['category']
                price = form.cleaned_data['price']
                photo = request.FILES['photo']
                units = form.cleaned_data['units']
                pages = form.cleaned_data['pages']
                publish_year = form.cleaned_data['publish_year']
                details = form.cleaned_data['details']
                tags = form.cleaned_data['tags']
                is_bestseller = form.cleaned_data['is_bestseller']
                is_award_winner = form.cleaned_data['is_award_winner']

                for x in range(units):
                    product = Product(
                        title=title,
                        author=author,
                        publisher=publisher,
                        category=category,
                        init_price=price,
                        photo = photo,
                        pages=pages,
                        publish_year = publish_year,
                        details = details,
                        tags = tags,
                        batch_unit = units,
                        is_bestseller = is_bestseller,
                        is_award_winner = is_award_winner,
                    )
                    product.save()
                messages.success(request, 'product added successfully!')
                return redirect('add_product') 
            else:
                messages.error(request, 'Something went wrong!')
                return redirect('add_product')
        else:
            context = {
                'form': ProductInputForm,
            }
            return render(request, 'products/add.html', context)
    else:
        return redirect('index')