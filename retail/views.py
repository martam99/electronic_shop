from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from employee.permissions import IsSuperUser, UserPermissionsAll
from retail.models import Retail, Store
from retail.paginators import RetailPaginator, StorePaginator
from retail.serializers import RetailSerializer, StoreSerializer


class RetailCreateApiView(generics.CreateAPIView):
    serializer_class = RetailSerializer
    permission_classes = [IsSuperUser]


class RetailUpdateApiView(generics.UpdateAPIView):
    queryset = Retail.objects.all()
    serializer_class = RetailSerializer
    permission_classes = [UserPermissionsAll]


class RetailListApiView(generics.ListAPIView):
    queryset = Retail.objects.all()
    serializer_class = RetailSerializer
    pagination_class = RetailPaginator
    permission_classes = [UserPermissionsAll]


class RetailDetailApiView(generics.RetrieveAPIView):
    queryset = Retail.objects.all()
    serializer_class = RetailSerializer
    permission_classes = [UserPermissionsAll]


class RetailDeleteApiView(generics.DestroyAPIView):
    serializer_class = RetailSerializer
    permission_classes = [IsSuperUser]


class StoreCreateApiView(generics.CreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsSuperUser]


class StoreUpdateApiView(generics.UpdateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [UserPermissionsAll]


class StoreDetailApiView(generics.RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [UserPermissionsAll]


class StoreListApiView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    pagination_class = StorePaginator
    permission_classes = [UserPermissionsAll]
    filter = ['contacts__country']



class StoreDestroyApiView(generics.DestroyAPIView):
    queryset = Store.objects.all()
    permission_classes = [IsSuperUser]


