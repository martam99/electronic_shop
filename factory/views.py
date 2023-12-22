from django.shortcuts import render
from rest_framework import generics

from factory.paginators import FactoryPaginator
from factory.serializers import FactorySerializer


# Create your views here.
class FactoryListApiView(generics.ListAPIView):
    serializer_class = FactorySerializer
    pagination_class = FactoryPaginator
