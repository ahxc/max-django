from django_filters import rest_framework as drf_filters


from .models import Commentary


class CommentaryFilter(drf_filters.FilterSet):
    class Meta:
        model = Commentary
        fields = ["game"]