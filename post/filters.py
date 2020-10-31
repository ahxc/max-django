from django_filters import rest_framework as drf_filters


from .models import Post


class PostFilter(drf_filters.FilterSet):
    class Meta:
        model = Post
        fields = ["id"]