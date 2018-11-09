from django.contrib import admin
from django.urls import path
from rest_framework import routers

from .views import OrderViewSet


router = routers.SimpleRouter()
router.register(r'orders', OrderViewSet)

urlpatterns = router.urls
