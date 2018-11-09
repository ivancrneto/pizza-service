from django.db import models
from model_utils import Choices
from model_utils.models import TimeStampedModel


class Pizza(TimeStampedModel):
    SIZES = Choices(
        ('30', 'S30_CM', '30 cm'),
        ('50', 'S50_CM', '50 cm'),
    )
    size = models.CharField(
        choices=SIZES, default=SIZES.S30_CM, max_length=20)


class Customer(TimeStampedModel):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=100)


class Order(TimeStampedModel):
    pizza = models.ForeignKey(
        'api.Pizza', null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(
        'api.Customer', null=True, on_delete=models.SET_NULL)
