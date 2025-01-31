from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'table_number', 'status', 'total_price')  # Поля, которые будут отображаться в списке
    list_filter = ('status',)  # Фильтры для быстрого поиска
    search_fields = ('id', 'table_number')  # Поиск по этим полям
    ordering = ('-id',)  # Сортировка по убыванию ID (по умолчанию)
    readonly_fields = ('total_price',)  # Сделать поле total_price доступным только для чтения
    filter_horizontal = ('items',)

admin.site.register(Order, OrderAdmin)

