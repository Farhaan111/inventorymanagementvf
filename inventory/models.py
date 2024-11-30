
from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Category Model
class Category(models.Model):
    cname = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.cname


# Location Model
class Location(models.Model):
    loc = models.CharField(max_length=35, unique=True)
    area_code = models.IntegerField()

    def __str__(self):
        return f"{self.loc} ({self.area_code})"


# Supplier Model
class SupplierManager(BaseUserManager):
    """
    Custom manager for creating suppliers.
    """
    def create_supplier(self, email, password=None, **extra_fields):
        """
        Create and return a supplier with an email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        supplier = self.model(email=email, **extra_fields)
        supplier.set_password(password)  # Hash the password before saving
        supplier.save(using=self._db)
        return supplier

class SupplierManager(BaseUserManager):
    """
    Custom manager for Supplier model.
    """
    def create_supplier(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        supplier = self.model(email=email, **extra_fields)
        supplier.set_password(password)
        supplier.save(using=self._db)
        return supplier

class Supplier(AbstractBaseUser):
    company_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, blank=False)
    contact_info = models.CharField(max_length=255)
    address = models.TextField()
    total_sale = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    last_login = models.DateTimeField(auto_now_add=True)

    objects = SupplierManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['company_name','email', 'contact_info', 'address']

    def __str__(self):
        return self.company_name


# Customer Model
class CustomerManager(BaseUserManager):
    def create_customer(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(("The Email field must be set"))
        email = self.normalize_email(email)
        customer = self.model(email=email, **extra_fields)
        customer.set_password(password)  # Hash the password
        customer.save(using=self._db)
        return customer
    
class Customer(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    address = models.CharField(max_length=500)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, blank=False)
    total_sale=models.IntegerField(default=0,validators=[MinValueValidator(0)])

    USERNAME_FIELD = 'email'  # This will be used to log in (instead of username)
    REQUIRED_FIELDS = ['name', 'email']  # Fields required to create the customer object
    
    objects = CustomerManager()

    def save(self, *args, **kwargs): #oh these parameters are used to store extra parameters if we pass em while calling the function
        # Ensures that password is hashed before saving
        if not self.password.startswith('pbkdf2_'): # Check if already hashed since If the password is already hashed (it starts with pbkdf2_), it will not hash it again.
            self.password = make_password(self.password) #inbuilt hashing method
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# Item Model
class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True, blank=True,)
    loc = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def formatted_created_at(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M:%S')

    def formatted_updated_at(self):
        return self.updated_at.strftime('%Y-%m-%d %H:%M:%S')

    def __str__(self):
        return self.name


# Transaction Model
class Transaction(models.Model):
    ITEM_CHOICES = [
        ('IN', 'Inbound'),
        ('OUT', 'Outbound')
    ]

    TRANSACTION_CATEGORY_IN = [
        ('PS', 'Purchased from Supplier'),
        ('PI', 'Produced In-house')
    ]

    TRANSACTION_CATEGORY_OUT = [
        ('SC', 'Sold to Customer'),
        ('GD', 'Goods Damaged')
    ]
    TRANSACTION_CATEGORY_General = [
        ('G', 'General'),('SC', 'Sold to Customer'),
        ('GD', 'Goods Damaged'), ('PS', 'Purchased from Supplier'),
        ('PI', 'Produced In-house')
      
    ]
    

    item = models.ForeignKey(Item, on_delete=models.CASCADE)  # Relates to the Item model
    transaction_type = models.CharField(
        max_length=10,
        choices=ITEM_CHOICES,
    )
    transaction_category = models.CharField(
        max_length=10,choices=TRANSACTION_CATEGORY_General
    )
    supplier_id = models.ForeignKey(Supplier, null=True, blank=True, on_delete=models.SET_NULL)
    customer_id = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField()
    transdate = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Validate transaction category
        if self.transaction_type == 'IN' and self.transaction_category not in dict(self.TRANSACTION_CATEGORY_IN):
            raise ValidationError("Invalid category for 'IN' transactions.")
        if self.transaction_type == 'OUT' and self.transaction_category not in dict(self.TRANSACTION_CATEGORY_OUT):
            raise ValidationError("Invalid category for 'OUT' transactions.")

        # Validate supplier_id or customer_id based on category
        if self.transaction_category == 'PS' and not self.supplier_id:
            raise ValidationError("Supplier ID must be provided for 'Purchased from Supplier'.")
        if self.transaction_category == 'SC' and not self.customer_id:
            raise ValidationError("Customer ID must be provided for 'Sold to Customer'.")

        # Ensure enough stock for 'OUT' transactions
        if self.transaction_type == 'OUT' and self.item.quantity < self.quantity:
            raise ValidationError(f"Not enough stock for {self.item.name}. Current quantity: {self.item.quantity}")

        super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()  # Run validation before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.transaction_type} - {self.item.name} - {self.transaction_category}"
