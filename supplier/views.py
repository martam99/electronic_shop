from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from employee.permissions import IsSuperUser, UserPermissionsAll
from supplier.models import Supplier
from supplier.paginators import SupplierPaginator
from supplier.serializers import SupplierSerializer


class SupplierCreateAPIView(generics.CreateAPIView):
    serializer_class = SupplierSerializer
    permission_classes = [IsSuperUser]


class SupplierUpdateAPIView(generics.UpdateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [UserPermissionsAll]


# Create your views here.
class SupplierListAPIView(generics.ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    pagination_class = SupplierPaginator
    permission_classes = [UserPermissionsAll]


class SupplierDetailAPIView(generics.RetrieveAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    pagination_class = SupplierPaginator
    permission_classes = [UserPermissionsAll]


class SupplierDeleteAPIView(generics.DestroyAPIView):
    queryset = Supplier.objects.all()
    permission_classes = [IsSuperUser]

