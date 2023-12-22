from rest_framework import generics
from SP.paginators import SPPaginator
from SP.serializers import SPSerializer


# Create your views here.
class SPListApiView(generics.CreateAPIView):
    serializer_class = SPSerializer
    pagination_class = SPPaginator
