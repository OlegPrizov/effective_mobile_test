from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['table_number', 'items', 'status']  # Указываем поля, которые будут доступны в форме

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Можно добавить дополнительные настройки формы, например, для поля 'items':
        self.fields['items'].widget = forms.CheckboxSelectMultiple()  # Виджет для ManyToMany, можно использовать чекбоксы