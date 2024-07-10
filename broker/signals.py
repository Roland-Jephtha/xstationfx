from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=Profile)
def update_balance(sender, instance, created, **kwargs):
    if not created and 'profit' in kwargs.get('update_fields', []):
        instance.balance += instance.profit
        instance.save(update_fields=['balance'])
