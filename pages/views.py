from django.shortcuts import get_object_or_404, render
from products.models import Product
from products.categories import categories

def index(request):
    products = []
    for category in categories:
        items = Product.objects.order_by('-updated_at').filter(status = 'OS', category=category[0]).all().exclude(current_owner = request.user)[:6]
        i = 0
        members = []
        for item in items:
            if i==0:
                members.append(item)
            elif (item.title != items[i-1].title) or (item.sold_count != items[i-1].sold_count):
                    members.append(item)
            i += 1
        if members:
            subproducts={
                'title': category[1],
                'items' : members,
            }
            products.append(subproducts)
    context = {
        'products' : products,
    }
        
    return render(request, 'pages/index.html', context)