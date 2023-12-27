from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from SP.models import SP
from SP.paginators import SPPaginator
from SP.serializers import SPSerializer


# Create your views here.
class SPListApiView(generics.ListAPIView):
    queryset = SP.objects.all()
    serializer_class = SPSerializer
    pagination_class = SPPaginator
    permission_classes = [IsAdminUser]


class SPDetailApiView(generics.RetrieveAPIView):
    queryset = SP.objects.all()
    serializer_class = SPSerializer
    permission_classes = [IsAdminUser]

