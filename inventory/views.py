from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item, Transaction
from .serializers import ItemSerializer, TransactionSerializer

def home(request):
    return render(request, 'home.html')

@api_view(['GET'])
def get_items(request):
    items = Item.objects.all()  # Get all items from the database
    serializer = ItemSerializer(items, many=True)  # Serialize the data
    return Response(serializer.data)  # Return as JSON
def get_transaction(request):
    transaction = Transaction.objects.all()  # Get all items from the database
    serializer = TransactionSerializer(transaction, many=True)  # Serialize the data
    return Response(serializer.data)  # Return as JSON