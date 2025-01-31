from rest_framework import serializers
from orders.models import Order, Dish

class OrderSerializer(serializers.ModelSerializer):
    items = serializers.SlugRelatedField(
        queryset=Dish.objects.all(), slug_field='name', many=True
    )

    class Meta:
        model = Order
        fields = '__all__'
