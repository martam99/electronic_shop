from django.urls import path

from employee.apps import EmployeeConfig
from employee.views import UserCreateAPIView

app_name = EmployeeConfig.name

urlpatterns = [
    path('create_user/', UserCreateAPIView.as_view(), name='create_user')
]
