from django.db import models
from products.models import Product
from django.contrib.auth.models import User
from datetime import datetime

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    ordered_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='%(class)s_buyer')
    owned_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='%(class)s_owner')
    price = models.IntegerField()
    is_confirmed = models.BooleanField(default=False, blank=True)
    time = models.DateTimeField(blank=True, default=datetime.now)
    def __str__(self):
        return f"{self.product.title}_{self.product.id}"