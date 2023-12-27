from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from employee.permissions import UserPermissionsAll
from factory.models import Factory
from factory.paginators import FactoryPaginator
from factory.serializers import FactorySerializer


# Create your views here.
class FactoryListApiView(generics.ListAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    pagination_class = FactoryPaginator
    permission_classes = [UserPermissionsAll]


class FactoryDetailApiView(generics.RetrieveAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    permission_classes = [UserPermissionsAll]

