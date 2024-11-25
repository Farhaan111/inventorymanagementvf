from django.db import models
from django.core.validators import MinValueValidator
from django.utils.timezone import now

class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=50)
    quantity = models.IntegerField(validators=[MinValueValidator(0)]) # No negative quantities
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=now, editable=False)  # Automatically set at creation
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updated on save

    def __str__(self):
        return self.name
