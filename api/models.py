from django.db import models
from model_utils import Choices, TimeStampedModel


class Pizza(TimeStampedModel):
    SIZES = Choices(
        (S30_CM, '30 cm'),
        (S50_CM, '50 cm'),
    )
    size = models.CharField(
        choices=SIZES, default=SIZES.S30_CM, max_length=20)


class Customer(TimeStampedModel):
    name = models.CharField(max_lenght=40)
    address = models.CharField(max_lenght=100)


class Order(TimeStampedModel):
    pizza = models.ForeignKey('api.Pizza')
    customer = models.ForeignKey('api.Customer')
