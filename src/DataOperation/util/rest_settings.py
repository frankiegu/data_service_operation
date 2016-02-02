from rest_framework import pagination #@UnresolvedImport

class RestPagination(pagination.PageNumberPagination):
    page_query_param = 'page_no'
    page_size_query_param = 'page_size'
    max_page_size = 10000
