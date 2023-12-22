from django.shortcuts import render
from rest_framework import generics

from retail.paginators import RetailPaginator, StorePaginator
from retail.serializers import RetailSerializer, StoreSerializer


# Create your views here.
class RetailListApiView(generics.ListAPIView):
    serializer_class = RetailSerializer
    pagination_class = RetailPaginator


class StoreListApiView(generics.ListAPIView):
    serializer_class = StoreSerializer
    pagination_class = StorePaginator
