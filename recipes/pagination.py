from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size_query_param = 'limit'

    def get_paginated_response(self, data):
        return Response({
            'page': self.page.number,
            'limit': self.page.paginator.per_page,
            'total': self.page.paginator.count,
            'data': data
        })
