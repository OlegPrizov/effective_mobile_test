from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'table_number', 'status', 'total_price')
    list_filter = ('status',)
    search_fields = ('id', 'table_number')
    ordering = ('-id',)
    readonly_fields = ('total_price',)
    filter_horizontal = ('items',)

admin.site.register(Order, OrderAdmin)

