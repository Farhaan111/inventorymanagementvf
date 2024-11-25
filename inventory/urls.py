from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('api/items/', views.get_items, name='get_items'),  # API to fetch items
]
"""
      The /api/ in the path is simply a convention 
      to distinguish between regular Django views (like rendering HTML pages) 
      and API endpoints that return data, usually in JSON format.
"""