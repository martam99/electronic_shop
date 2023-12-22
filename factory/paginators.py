from rest_framework.pagination import PageNumberPagination


class FactoryPaginator(PageNumberPagination):
    page_size = 10
