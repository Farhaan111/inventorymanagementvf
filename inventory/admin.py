from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Item)
admin.site.register(Transaction)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Location)
admin.site.register(Supplier)
