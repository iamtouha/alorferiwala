from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display  = ('__str__', 'ordered_by', 'owned_by', 'price', 'time', 'is_confirmed_by_owner','is_confirmed_by_customer',)
    list_search  = ('product', 'ordered_by', 'owned_by',)
    list_editable  = ('is_confirmed_by_owner',)
    list_display_links  = ('__str__',)
    list_filter = ('is_confirmed_by_owner','is_confirmed_by_customer',)
    list_per_page  = 25

admin.site.register(Order, OrderAdmin)

