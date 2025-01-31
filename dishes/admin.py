from django.contrib import admin
from .models import Dish

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')  # Колонки для отображения в списке
    search_fields = ('name',)  # Поля для поиска
    list_filter = ('price',)  # Фильтрация по цене
