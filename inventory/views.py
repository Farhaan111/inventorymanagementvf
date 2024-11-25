from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer

def home(request):
    return render(request, 'home.html')

@api_view(['GET'])
def get_items(request):
    items = Item.objects.all()  # Get all items from the database
    serializer = ItemSerializer(items, many=True)  # Serialize the data
    return Response(serializer.data)  # Return as JSON
