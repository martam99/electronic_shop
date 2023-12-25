from django.shortcuts import render
from rest_framework import generics

from factory.models import Factory
from factory.paginators import FactoryPaginator
from factory.serializers import FactorySerializer


# Create your views here.
class FactoryListApiView(generics.ListAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    pagination_class = FactoryPaginator


class FactoryDetailApiView(generics.RetrieveAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
