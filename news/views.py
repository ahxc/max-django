from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins, viewsets
from django_filters.rest_framework import DjangoFilterBackend


from .models import News
from .serializers import NewsSerializer
from .filters import NewsFilter
from scripts.utils import ListPagination


# 列表、单例和基础视图集，动态化序列化器
class FindNews(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    pagenation_class = ListPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilter
# item_view = FindNews.as_view({'get': 'retrieve'})
news_view = FindNews.as_view({'get': 'list'})

"""
serializer_class_table = {
        'list': NewsSerializer,
        'retrieve': DetailSerializer
    }
    def get_serializer_class(self):
        return self.serializer_class_table.get(self.action, NewsSerializer)
"""