from django.urls import path

from supplier.apps import SupplierConfig
from supplier.views import SupplierListAPIView, SupplierDetailAPIView, SupplierCreateAPIView, SupplierUpdateAPIView, \
    SupplierDeleteAPIView

app_name = SupplierConfig.name

urlpatterns = [
    path('supplier_list/', SupplierListAPIView.as_view(), name='supplier_list'),
    path('supplier_detail/<int:pk>/', SupplierDetailAPIView.as_view(), name='supplier_detail'),
    path('supplier_create', SupplierCreateAPIView.as_view(), name='supplier_create'),
    path('supplier_update/<int:pk>/', SupplierUpdateAPIView.as_view(), name='supplier_update'),
    path('supplier_delete/<int:pk>/', SupplierDeleteAPIView.as_view(), name='supplier_delete'),
]
