from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    """ Контроль количества результатов на странице """
    page_size = 5
    max_page_size = 100
    page_size_query_param = 'page_size'


class IsOwner(permissions.BasePermission):
    """ Проверяем права на просмотр и редактирование. """
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
