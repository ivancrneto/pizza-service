from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView


class OrderViewSet(APIView):

    renderer_classes = [JSONRenderer,]

    def get(self, request, *args, **kwargs):
        return Response(data={}, content_type='text/json')
