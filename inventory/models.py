from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.utils.timezone import now

class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=50)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def formatted_created_at(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M:%S')  # Format as YYYY-MM-DD HH:MM:SS

    def formatted_updated_at(self):
        return self.updated_at.strftime('%Y-%m-%d %H:%M:%S')  # Format as YYYY-MM-DD HH:MM:SS

    def __str__(self):
        return self.name
class Transaction(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)  # if the item is deleted then the transaction log is also deleted
    transaction_type = models.CharField(
        max_length=10, 
        choices=[('IN', 'Inbound'), ('OUT', 'Outbound')]
    )
    quantity = models.PositiveIntegerField()
    transdate = models.DateTimeField(auto_now_add=True)
    
    def clean(self):
        if self.transaction_type == 'OUT' and self.item.quantity < self.quantity:
            raise ValidationError(f"Not enough stock for {self.item.name}. Current quantity: {self.item.quantity}")
        super().clean()


    def formatted_transdate(self):
        return self.transdatestrftime('%Y-%m-%d %H:%M:%S') # Format as YYYY-MM-DD HH:MM:SS

    def __str__(self):
        return f"{self.transaction_type} - {self.item.name}"
