from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins, viewsets


from .models import News
from .serializers import NewsSerializer, DetailSerializer
from scripts.utils import ListPagination


# 列表、单例和基础视图集，动态化序列化器
class FindNews(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = News.objects.all()
    pagenation_class = ListPagination
    serializer_class_table = {
        'list': NewsSerializer,
        'retrieve': DetailSerializer
    }
    def get_serializer_class(self):
        return self.serializer_class_table.get(self.action, NewsSerializer)
item_view = FindNews.as_view({'get': 'retrieve'})
news_view = FindNews.as_view({'get': 'list'})