from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Transaction

@receiver(post_save, sender=Transaction)
def update_item_quantity_on_save(sender, instance, created, **kwargs):
    """
    Updates the quantity of the Item when a Transaction is created or updated.
    """
    if created:  # Only handle newly created transactions
        if instance.transaction_type == 'IN':
            instance.item.quantity += instance.quantity
        elif instance.transaction_type == 'OUT':
            if instance.quantity > instance.item.quantity:
                raise ValueError("Insufficient quantity available for this transaction.")
            instance.item.quantity -= instance.quantity
        instance.item.save()

@receiver(post_delete, sender=Transaction)
def update_item_quantity_on_delete(sender, instance, **kwargs):
    """
    if transaction is deleted then the quantity is returned to what it was before the transaction
    """
    if instance.transaction_type == 'IN':
        instance.item.quantity -= instance.quantity
    elif instance.transaction_type == 'OUT':
        instance.item.quantity += instance.quantity
    instance.item.save()
