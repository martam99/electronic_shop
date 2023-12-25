from django.urls import path

from factory.apps import FactoryConfig
from factory.views import FactoryListApiView
from retail.views import RetailListApiView, StoreListApiView, RetailDetailApiView, StoreDetailApiView

app_name = FactoryConfig.name

urlpatterns = [
    path('retail_list/', RetailListApiView.as_view(), name='retail_list'),
    path('retail_detail/<int:pk>/', RetailDetailApiView.as_view(), name='retail_detail'),
    path('store_detail/<int:pk>/', StoreDetailApiView.as_view(), name='store_detail'),
    path('store_list/', StoreListApiView.as_view(), name='store_list'),
]
