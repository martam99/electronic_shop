from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from retail.models import Retail, Store
from retail.paginators import RetailPaginator, StorePaginator
from retail.serializers import RetailSerializer, StoreSerializer


# Create your views here.
class RetailListApiView(generics.ListAPIView):
    queryset = Retail.objects.all()
    serializer_class = RetailSerializer
    pagination_class = RetailPaginator
    permission_classes = [IsAdminUser]


class StoreListApiView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    pagination_class = StorePaginator
    permission_classes = [IsAdminUser]


class RetailDetailApiView(generics.RetrieveAPIView):
    queryset = Retail.objects.all()
    serializer_class = RetailSerializer
    permission_classes = [IsAdminUser]


class StoreDetailApiView(generics.RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAdminUser]

