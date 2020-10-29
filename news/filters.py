from django_filters import rest_framework as drf_filters


from .models import News


class NewsFilter(drf_filters.FilterSet):
    class Meta:
        model = News
        fields = ["id"]