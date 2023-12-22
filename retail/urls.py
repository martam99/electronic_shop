from django.urls import path

from factory.apps import FactoryConfig
from factory.views import FactoryListApiView
from retail.views import RetailListApiView, StoreListApiView

app_name = FactoryConfig.name

urlpatterns = [
    path('retail_list/', RetailListApiView.as_view(), name='retail_list'),
    path('store_list/', StoreListApiView.as_view(), name='store_list'),

]
