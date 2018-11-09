from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

from .models import Customer, Order, Pizza
from .serializers import OrderSerializer


class OrderViewSet(ModelViewSet):

    queryset = Order.objects.all()
    renderer_classes = [JSONRenderer,]
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        data = serializer.data

        customer_name, customer_address = (
            data.pop('customer_name'), data.pop('customer_address'))
        customer, _ = Customer.objects.get_or_create(
            name=customer_name, defaults={'address': customer_address})

        pizza_id, pizza_size = (
            data.pop('pizza_id'), data.pop('pizza_size'))
        pizza = Pizza.objects.get(id=pizza_id)

        Order.objects.create(
            pizza=pizza, customer=customer
        )
