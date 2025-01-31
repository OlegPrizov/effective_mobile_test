from django.db import models

class Dish(models.Model):
    name = models.CharField(max_length=100)  # Название блюда
    description = models.TextField(blank=True, null=True)  # Описание блюда
    price = models.DecimalField(max_digits=8, decimal_places=2)  # Цена блюда

    def __str__(self):
        return self.name