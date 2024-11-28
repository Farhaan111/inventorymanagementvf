from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('api/items/', views.get_items, name='get_items'),
      # API to fetch items,transactions should come up too along with items.
    path('api/transaction/', views.get_transaction, name='get_transaction'),
    path('api/Customer/', views.get_Customer, name='get_Customer'),
    path('api/Supplier/', views.get_Supplier, name='get_Supplier'),
    path('api/Location/', views.get_Location, name='get_Location'),
    path('api/Category/', views.get_Category, name='get_Category'),
    path('api/register_customer/', views.register_customer, name='register_customer'),

]
"""
      The /api/ in the path is simply a convention 
      to distinguish between regular Django views (like rendering HTML pages) 
      and API endpoints that return data, usually in JSON format.
"""