from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins, viewsets


from .models import News
from .serializers import NewsSerializer, DetailSerializer
from scripts.utils import ListPagination


class FindNews(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = NewsSerializer# 序列化类
    queryset = News.objects.all()# 数据库查询结果集
    pagenation_class = ListPagination
news_view = FindNews.as_view({'get': 'list'})


class NewsDetail(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = DetailSerializer
    queryset = News.objects.all()
item_view = NewsDetail.as_view({'get': 'retrieve'})