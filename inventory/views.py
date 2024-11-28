from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
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
    transaction = Transaction.objects.all()
    serializer = TransactionSerializer(transaction, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_Category(request):
    category= Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_Customer(request): #To be removed later or made admin-only
    customer = Customer.objects.all()
    serializer = CustomerSerializer(customer, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_Supplier(request):
    supplier = Supplier.objects.all()
    serializer = SupplierSerializer(supplier, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_Location(request):
    location = Location.objects.all()
    serializer = LocationSerializer(location, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def register_customer(request):
    """
    Handle customer registration. Validate input and create a new customer.
    """
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # Calls the `create` method in the serializer
        return Response({"message": "Customer registered successfully!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)