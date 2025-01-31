from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import OrderForm
from .models import Order
from dishes.models import Dish

class CreateOrder(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('orders:order_list')
    template_name = 'create_order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dishes'] = Dish.objects.all()
        return context

class UpdateOrder(LoginRequiredMixin, UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'update_order.html'
    success_url = reverse_lazy('orders:order_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dishes'] = Dish.objects.all()
        return context

@login_required
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

@login_required
def delete_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return redirect(reverse('orders:order_list'))