from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from SP.models import SP
from SP.paginators import SPPaginator
from SP.serializers import SPSerializer
from employee.permissions import UserPermissionsAll, IsSuperUser


class SPCreateApiView(generics.CreateAPIView):
    serializer_class = SPSerializer
    permission_classes = [IsSuperUser]


class SPUpdateApiView(generics.UpdateAPIView):
    queryset = SP.objects.all()
    serializer_class = SPSerializer
    permission_classes = [UserPermissionsAll]


class SPListApiView(generics.ListAPIView):
    queryset = SP.objects.all()
    serializer_class = SPSerializer
    pagination_class = SPPaginator
    permission_classes = [UserPermissionsAll]


class SPDetailApiView(generics.RetrieveAPIView):
    queryset = SP.objects.all()
    serializer_class = SPSerializer
    permission_classes = [UserPermissionsAll]


class SPDeleteApiView(generics.DestroyAPIView):
    queryset = SP.objects.all()
    permission_classes = [IsSuperUser]
