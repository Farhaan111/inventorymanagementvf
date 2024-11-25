from django.contrib import admin
from .models import Item

# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity', 'price')  # Fields to show in the admin list view
    search_fields = ('name', 'category')  # Enable search by name and category
