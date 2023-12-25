from django.urls import path

from SP.apps import SPConfig
from SP.views import SPListApiView, SPDetailApiView

app_name = SPConfig.name

urlpatterns = [
    path('sp_list/', SPListApiView.as_view(), name='sp_list'),
    path('sp_detail/<int:pk>/', SPDetailApiView.as_view(), name='sp_detail'),
]
