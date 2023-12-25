from rest_framework import generics

from SP.models import SP
from SP.paginators import SPPaginator
from SP.serializers import SPSerializer


# Create your views here.
class SPListApiView(generics.ListAPIView):
    queryset = SP.objects.all()
    serializer_class = SPSerializer
    pagination_class = SPPaginator


class SPDetailApiView(generics.RetrieveAPIView):
    queryset = SP.objects.all()
    serializer_class = SPSerializer
