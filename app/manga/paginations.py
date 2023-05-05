from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class GenrePagination(PageNumberPagination):
    page_size = 5
    max_page_size = 30
    page_query_param = "page"


class MangaLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 12
    max_limit = 12
