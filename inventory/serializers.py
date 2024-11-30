from rest_framework import serializers
from django.contrib.auth.hashers import make_password
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
    """
    Serializer for the Supplier model.
    Handles serialization and validation for supplier data.
    """
    password = serializers.CharField(write_only=True, required=True, min_length=8)

    class Meta:
        model = Supplier
        fields = ['id', 'company_name', 'email', 'password', 'contact_info', 'address', 'total_sale', 'last_login']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        # Hash the password
        validated_data['password'] = make_password(validated_data['password'])
        # Create and return the Customer instance
        return Supplier.objects.create(**validated_data)

    def validate_email(self, value):
        """
        Custom validation to ensure the email is unique.
        """
        if Supplier.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already registered.")
        return value

# Customer Serializer
class CustomerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8)
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'password', 'contact_info', 'address', 'total_sale']
        extra_kwargs = {
            'password': {'write_only': True},  # Prevent password from being returned in API responses
        }

    def create(self, validated_data):
        # Hash the password
        validated_data['password'] = make_password(validated_data['password'])
        # Create and return the Customer instance
        return Customer.objects.create(**validated_data)
    
    def validate_email(self, value):
        """
        Custom validation to ensure the email is unique.
        """
        if Customer.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already registered.")
        return value
    

# Login Serializer
class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login (applies to both customers and suppliers).
    """
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True, min_length=8)

    def validate(self, data):
        """
        Validate login credentials.
        """
        email = data.get('email')
        password = data.get('password')

        # Check for either customer or supplier
        customer = Customer.objects.filter(email=email).first()
        supplier = Supplier.objects.filter(email=email).first()

        user = customer or supplier
        if not user:
            raise serializers.ValidationError("No user with this email exists.")
        
        # Check password validity
        if not user.check_password(password):
            raise serializers.ValidationError("Invalid credentials. Please try again.")

        # Return user type and instance
        return {
            "user": user,
            "type": "customer" if customer else "supplier",
        }

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

