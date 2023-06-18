from django.contrib import admin
from .models import CustomUser
# Register your models here.


class CustomUserModel(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    search_fields = ['email', 'first_name', 'last_name']


admin.site.register(CustomUser, CustomUserModel)
