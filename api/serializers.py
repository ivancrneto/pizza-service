from rest_framework import serializers

from .models import Order, Pizza


class OrderSerializer(serializers.ModelSerializer):

    pizza_id = serializers.IntegerField()
    pizza_size = serializers.ChoiceField(choices=Pizza.SIZES)
    customer_name = serializers.CharField(source='customer.name')
    customer_address = serializers.CharField(source='customer.address')

    class Meta:
        model = Order
        fields = ('pizza_id', 'pizza_size', 'customer_name',
                  'customer_address')

