from rest_framework.pagination import PageNumberPagination


class RetailPaginator(PageNumberPagination):
    page_size = 10


class StorePaginator(PageNumberPagination):
    page_size = 10
