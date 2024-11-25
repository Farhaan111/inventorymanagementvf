from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    formatted_created_at = serializers.SerializerMethodField()
    formatted_updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = [
            'id', 'name', 'category', 'quantity', 'price', 
            'description', 'formatted_created_at', 'formatted_updated_at'
        ]
        '''
        add 'created_at', 'updated_at' to fields if raw form of the dates is needed by frontend people
        '''

    def get_formatted_created_at(self, obj):
        return obj.formatted_created_at()

    def get_formatted_updated_at(self, obj):
        return obj.formatted_updated_at()