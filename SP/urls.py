from django.urls import path

from SP.apps import SPConfig
from SP.views import SPListApiView, SPDetailApiView, SPCreateApiView, SPUpdateApiView, SPDeleteApiView

app_name = SPConfig.name

urlpatterns = [
    path('sp_list/', SPListApiView.as_view(), name='sp_list'),
    path('sp_detail/<int:pk>/', SPDetailApiView.as_view(), name='sp_detail'),
    path('sp_create/', SPCreateApiView.as_view(), name='sp_create'),
    path('sp_update/<int:pk>/', SPUpdateApiView.as_view(), name='sp_update'),
    path('sp_delete/<int:pk>/', SPDeleteApiView.as_view(), name='sp_delete'),
]
