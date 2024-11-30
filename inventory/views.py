from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

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


@api_view(['POST'])
def customer_login(request):
    """
    Authenticate customer and return JWT tokens.
    """
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({"detail": "Email and password are required."}, status=HTTP_401_UNAUTHORIZED)

    # Authenticate the user
    customer = authenticate(username=email, password=password)

    if customer is not None and hasattr(customer, 'customer'):
        # Generate tokens
        refresh = RefreshToken.for_user(customer)

        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'message': 'Login Successful'
        }, status=HTTP_200_OK)
    return Response({'detail': 'Invalid credentials or not a customer'}, status=status.HTTP_401_UNAUTHORIZED)


#Supplier Authentication
@api_view(['POST'])
def register_supplier(request):
    """
    Handles supplier registration.
    """
    serializer = SupplierSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Supplier registered successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def supplier_login(request):
    """
    Handles supplier login using JWT.
    """
    email = request.data.get('email')
    password = request.data.get('password')

    supplier = authenticate(request, username=email, password=password)
    if supplier is not None and hasattr(supplier, 'supplier'):
        refresh = RefreshToken.for_user(supplier)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'message': 'Login successful'
        })
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)