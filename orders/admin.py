from django.contrib import admin
from .models import Order
from products.models import Product
from django.db.models import F
from .views import fraction
from datetime import datetime

class OrderAdmin(admin.ModelAdmin):
    list_display  = ('__str__', 'ordered_by', 'owned_by', 'price', 'time', 'is_confirmed',)
    list_search  = ('product', 'ordered_by', 'owned_by',)
    list_editable  = ('is_confirmed',)
    list_display_links  = ('__str__',)
    list_filter = ('is_confirmed',)
    list_per_page  = 25
    def save_model(self, request, obj, form, change):
        if 'is_confirmed' in form.changed_data:
            if obj.is_confirmed:
                Product.objects.filter(id = obj.product.id).update(
                    sold_count = F('sold_count') + 1,
                    current_price = F('current_price') * fraction ** F('sold_count'),
                    current_owner = obj.ordered_by,
                    status = 'SD',
                    updated_at = datetime.now()
                    )
        super().save_model(request, obj, form, change)

admin.site.register(Order, OrderAdmin)

