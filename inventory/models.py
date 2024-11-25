from django.db import models
from django.core.validators import MinValueValidator
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
