from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from .categories import categories

class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=32, choices=categories)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    init_price = models.IntegerField(default=0)
    current_price = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', max_length=255)
    batch_unit = models.IntegerField(default=0)
    pages = models.IntegerField()
    publish_year = models.CharField(max_length=8)
    details = models.TextField(max_length=1024)
    tags = models.CharField(max_length=255)
    is_bestseller = models.BooleanField(default=False)
    is_award_winner = models.BooleanField(default=False)
    sold_count = models.IntegerField(blank=True, default=0)

    on_sale = 'OS'
    ordered = 'OD'
    sold = 'SD'
    status_choice = (
        (on_sale, 'On Sale'),
        (ordered, 'Ordered'),
        (sold, 'Sold'),
    )
    status = models.CharField(max_length=2, choices = status_choice, default=on_sale)

    uploaded_at = models.DateTimeField(default = datetime.now, blank = True)
    updated_at = models.DateTimeField(default = datetime.now, blank = True)
    current_owner = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank=True, related_name='%(class)s_seller')
    ordered_by = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank=True, related_name='%(class)s_buyer')
    def __str__(self):
        return self.title
