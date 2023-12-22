from django.urls import path

from factory.apps import FactoryConfig
from factory.views import FactoryListApiView

app_name = FactoryConfig.name

urlpatterns = [
    path('factory_list/', FactoryListApiView.as_view(), name='factory_list')
]
