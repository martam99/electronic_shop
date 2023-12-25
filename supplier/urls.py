from django.urls import path

from supplier.apps import SupplierConfig
from supplier.views import SupplierListAPIView, SupplierDetailAPIView

app_name = SupplierConfig.name

urlpatterns = [
    path('supplier_list/', SupplierListAPIView.as_view(), name='supplier_list'),
    path('supplier_detail/<int:pk>/', SupplierDetailAPIView.as_view(), name='supplier_detail'),
]
