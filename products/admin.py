from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display=('title','author', 'category', 'init_price','sold_count','current_price', 'current_owner', 'status',)
    list_display_links=('title',)
    list_search=('title', 'author', 'publisher',)
    list_per_page=25
    list_filter=('status', 'publisher', 'category',)

admin.site.register(Product, ProductAdmin)