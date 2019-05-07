from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display  = ('product', 'ordered_by', 'owned_by', 'price', 'time', 'is_confirmed',)
    list_search  = ('product', 'ordered_by', 'owned_by',)
    list_editable  = ('is_confirmed',)
    list_display_links  = ('product',)
    list_filter = ('product','is_confirmed',)
    list_per_page  = 25

admin.site.register(Order, OrderAdmin)

