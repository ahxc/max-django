# from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins, viewsets

from .models import News
from .serializers import NewsSerializer, DetailSerializer
# from .filters import IdSearchFilter

# 分页定制类
class FindNewsPagination(PageNumberPagination):
	# 表示每页的默认显示数量
  page_size = 10
  # 表示url中每页请求数量，可以不加到url中
  page_size_query_param = 'page_size'
  # 表示url中的页码参数
  page_query_param = 'page'
  # 表示每页最大显示数量，做限制使用，避免突然大量的查询数据，数据库崩溃
  max_page_size = 100

class FindNews(mixins.ListModelMixin, viewsets.GenericViewSet):
	# 序列化类
  serializer_class = NewsSerializer
  # 数据库查询结果集
  queryset = News.objects.all()
  pagenation_class = FindNewsPagination
news_view = FindNews.as_view({'get': 'list'})

class NewsDetail(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = DetailSerializer
    queryset = News.objects.all()
item_view = NewsDetail.as_view({'get': 'retrieve'})