from rest_framework.pagination import PageNumberPagination


class SPPaginator(PageNumberPagination):
    page_size = 10
