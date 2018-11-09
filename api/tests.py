import json
from django.test import Client, TestCase
from model_mommy import mommy

from .views import OrderViewSet



class OrderViewSetTest(TestCase):

    def setUp(self):
        self.viewset = OrderViewSet()

    def test_get(self):
        orderdb = mommy.make(
            'api.Order', pizza__size='50', customer__name='Ivan',
            customer__address='1750 Commerce Dr Nw, NY, NY, US')

        client = Client()
        response = client.get('/api/orders/')
        response_data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_data), 1)

        order = response_data[0]
        self.assertEqual(order['pizza_id'], orderdb.pizza.id)
        self.assertEqual(order['pizza_size'], '50')
        self.assertEqual(order['customer_name'], 'Ivan')
        self.assertEqual(
            order['customer_address'], '1750 Commerce Dr Nw, NY, NY, US')
