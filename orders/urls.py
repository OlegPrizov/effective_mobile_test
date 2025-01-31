from django.urls import path
from .views import CreateOrder, UpdateOrder, orders_list, delete_order

app_name = 'orders'

urlpatterns = [
    path('list/', orders_list, name='order_list'),
    path('create/', CreateOrder.as_view(), name='create_order'),
    path('<int:pk>/edit/', UpdateOrder.as_view(), name='edit_order'),
    path('<int:pk>/delete/', delete_order, name='delete'),
]