from rest_framework import serializers
from .models import Category, Location, Supplier, Customer, Item, Transaction


# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'cname']


# Location Serializer
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'loc', 'area_code']


# Supplier Serializer
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'contact_info', 'address']

# Customer Serializer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'contact_info', 'address', 'email']

# Item Serializer
class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # Nested Category
    loc = LocationSerializer(read_only=True)  # Nested Location
    transactions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    formatted_created_at = serializers.SerializerMethodField()
    formatted_updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = [
            'id', 'name', 'category', 'loc', 'quantity', 'price', 
            'description', 'formatted_created_at', 'formatted_updated_at', 'transactions'
        ]

    def get_formatted_created_at(self, obj):
        return obj.formatted_created_at()

    def get_formatted_updated_at(self, obj):
        return obj.formatted_updated_at()


# Transaction Serializer
class TransactionSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)
    supplier_id = SupplierSerializer(read_only=True)
    customer_id = CustomerSerializer(read_only=True)

    transdate = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = [
            'id', 'item', 'transaction_type', 'transaction_category', 
            'supplier_id', 'customer_id', 'quantity', 'transdate'
        ]
    

    def get_transdate(self, obj):
        return obj.transdate.strftime('%Y-%m-%d %H:%M:%S')

