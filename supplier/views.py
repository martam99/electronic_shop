from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from supplier.models import Supplier
from supplier.paginators import SupplierPaginator
from supplier.serializers import SupplierSerializer


# Create your views here.
class SupplierListAPIView(generics.ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    pagination_class = SupplierPaginator
    permission_classes = [IsAdminUser]


class SupplierDetailAPIView(generics.RetrieveAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    pagination_class = SupplierPaginator
    permission_classes = [IsAdminUser]

