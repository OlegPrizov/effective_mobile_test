from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import OrderForm
from .models import Order
from dishes.models import Dish
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

class CreateOrder(CreateView):
    model = Order  # Указываем модель для представления
    form_class = OrderForm  # Используем форму для создания заказа
    success_url = reverse_lazy('orders:order_list')  # Страница, куда перейдём после успешного создания
    template_name = 'create_order.html'  # Шаблон для отображения формы

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем все блюда в контекст
        context['dishes'] = Dish.objects.all()  # Все доступные блюда
        return context

class UpdateOrder(UpdateView):
    model = Order  # Модель для редактирования
    form_class = OrderForm  # Форма для редактирования
    template_name = 'update_order.html'  # Шаблон для редактирования
    success_url = reverse_lazy('orders:order_list')  # Куда перенаправлять после сохранения

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем доступные блюда в контекст (если нужно)
        context['dishes'] = Dish.objects.all()
        return context

def orders_list(request):
    table_number = request.GET.get('table_number')
    status = request.GET.get('status')

    orders = Order.objects.all()

    if table_number:
        orders = orders.filter(table_number=table_number)
    if status:
        orders = orders.filter(status=status)

    return render(request, 'orders_list.html', {
        'orders': orders,
        'table_number': table_number,
        'status': status,
    })


def delete_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return redirect(reverse('orders:order_list'))