from django.contrib import admin
from .models import UserProfile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_full_name', '__str__', 'phone', 'address',)
    list_display_links = ('user_full_name',)
    search_fields = ('name','__str__','phone',)

    def user_full_name(self, obj):
        return obj.user.first_name + ' ' + obj.user.last_name

admin.site.register(UserProfile, ProfileAdmin)