from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

class findPagination(PageNumberPagination):
  page_size = None
  page_size_query_param = 'page_size'
  max_page_size = None

  def get_paginated_response(self, data):
    """Devuelve la respuesta paginada con enlaces de primera, última, siguiente y anterior página"""
    return Response({
      'count': self.page.paginator.count,
      'next': self.page.next_page_number() if self.page.has_next() else None,
      'previous': self.page.previous_page_number() if self.page.has_previous() else None,
      'first': 1,
      'last': self.page.paginator.num_pages,
      'results': data
    })