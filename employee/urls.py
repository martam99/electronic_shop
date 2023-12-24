from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from employee.apps import EmployeeConfig
from employee.views import UserCreateAPIView

app_name = EmployeeConfig.name

urlpatterns = [
    path('create_user/', UserCreateAPIView.as_view(), name='create_user'),
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
