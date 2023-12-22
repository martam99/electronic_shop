from rest_framework import generics

from supplier.paginators import SupplierPaginator
from supplier.serializers import SupplierSerializer


# Create your views here.
class SupplierListAPIView(generics.ListAPIView):
    serializer_class = SupplierSerializer
    pagination_class = SupplierPaginator
