from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    """ Контроль количества результатов на странице """
    page_size = 5
    max_page_size = 100
    page_size_query_param = 'page_size'

