from django.shortcuts import render
from rest_framework import generics

from retail.models import Retail, Store
from retail.paginators import RetailPaginator, StorePaginator
from retail.serializers import RetailSerializer, StoreSerializer


# Create your views here.
class RetailListApiView(generics.ListAPIView):
    queryset = Retail.objects.all()
    serializer_class = RetailSerializer
    pagination_class = RetailPaginator


class StoreListApiView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    pagination_class = StorePaginator
