from django.db import models
from django.contrib.auth.models import User
import datetime

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(unique=True)
    address  = models.CharField(max_length=255)
    profile_img = models.ImageField(upload_to='profile_images/%Y/%m/%d', blank=True)
    def __str__(self):
        return self.user.email