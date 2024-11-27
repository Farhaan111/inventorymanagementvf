from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item, Transaction, Customer,Category,Location,Supplier
from .serializers import *


def home(request):
    return render(request, 'home.html')

@api_view(['GET'])
def get_items(request):
    items = Item.objects.all()  # Get all items from the database
    serializer = ItemSerializer(items, many=True)  # Serialize the data
    return Response(serializer.data)  # Return as JSON

@api_view(['GET'])
def get_transaction(request):
    transaction = Transaction.objects.all()  # Get all items from the database
    serializer = TransactionSerializer(transaction, many=True)  # Serialize the data
    return Response(serializer.data)  # Return as JSON

@api_view(['GET'])
def get_Category(request):
    category= Category.objects.all()  # Get all items from the database
    serializer = CategorySerializer(category, many=True)  # Serialize the data
    return Response(serializer.data)  # Return as JSON

@api_view(['GET'])
def get_Customer(request):
    customer = Customer.objects.all()  # Get all items from the database
    serializer = CustomerSerializer(customer, many=True)  # Serialize the data
    return Response(serializer.data)  # Return as JSON

@api_view(['GET'])
def get_Supplier(request):
    supplier = Supplier.objects.all()  # Get all items from the database
    serializer = SupplierSerializer(supplier, many=True)  # Serialize the data
    return Response(serializer.data)  # Return as JSON

@api_view(['GET'])
def get_Location(request):
    location = Location.objects.all()  # Get all items from the database
    serializer = LocationSerializer(location, many=True)  # Serialize the data
    return Response(serializer.data)  # Return as JSON