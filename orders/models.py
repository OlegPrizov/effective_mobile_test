from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from dishes.models import Dish

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('paid', 'Paid'),
    ]

    table_number = models.PositiveIntegerField()
    items = models.ManyToManyField(Dish)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Order #{self.id} - Table {self.table_number}"

@receiver(m2m_changed, sender=Order.items.through)
def update_total_price(sender, instance, action, **kwargs):
    if action in ['post_add', 'post_remove']:
        total = sum(dish.price for dish in instance.items.all())
        instance.total_price = total
        instance.save()