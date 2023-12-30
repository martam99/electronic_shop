from django.urls import path

from factory.apps import FactoryConfig
from factory.views import FactoryListApiView
from retail.views import RetailListApiView, StoreListApiView, RetailDetailApiView, StoreDetailApiView, \
    StoreCreateApiView, StoreUpdateApiView, StoreDestroyApiView, RetailCreateApiView, RetailUpdateApiView, \
    RetailDeleteApiView

app_name = FactoryConfig.name

urlpatterns = [
    path('retail_list/', RetailListApiView.as_view(), name='retail_list'),
    path('retail_detail/<int:pk>/', RetailDetailApiView.as_view(), name='retail_detail'),
    path('store_detail/<int:pk>/', StoreDetailApiView.as_view(), name='store_detail'),
    path('store_list/', StoreListApiView.as_view(), name='store_list'),
    path('store_create/', StoreCreateApiView.as_view(), name='store_create'),
    path('store_update/<int:pk>/', StoreUpdateApiView.as_view(), name='store_update'),
    path('store_delete/<int:pk>/', StoreDestroyApiView.as_view(), name='store_delete'),
    path('retail_create/', RetailCreateApiView.as_view(), name='retail_create'),
    path('retail_update/<int:pk>/', RetailUpdateApiView.as_view(), name='retail_update'),
    path('retail_delete/<int:pk>/', RetailDeleteApiView.as_view(), name='retail_destroy'),
]
