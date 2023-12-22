from django.urls import path

from SP.apps import SPConfig
from SP.views import SPListApiView

app_name = SPConfig.name

urlpatterns = [
    path('sp_list/', SPListApiView.as_view(), name='sp_list')
]
