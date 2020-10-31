from rest_framework import mixins, viewsets
from django_filters.rest_framework import DjangoFilterBackend


from .models import Post
from .serializers import PostSerializer
from .filters import PostFilter
from scripts.utils import ListPagination


# 列表、单例和基础视图集，动态化序列化器
class PostView(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    pagenation_class = ListPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter
post_view = PostView.as_view({'get': 'list'})


"""
# 不使用筛选器，使用list和retrieve区分单个实例和多个实例的方法
serializer_class_table = {
        'list': NewsSerializer,
        'retrieve': DetailSerializer
    }
    def get_serializer_class(self):
        return self.serializer_class_table.get(self.action, NewsSerializer)
"""