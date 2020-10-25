from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from rest_framework import serializers


from .models import News
from scripts.utils import TimestampField


class NewsSerializer(HyperlinkedModelSerializer):
    released_timestamp = TimestampField(source='released_time')
    class Meta:
        model = News
        fields = [
            "id",
            "title",
            "released_timestamp",
            "views",
            "cover_url"
        ]


class DetailSerializer(ModelSerializer):
    released_timestamp = TimestampField(source='released_time')
    author_nickname = serializers.CharField(source='author.nickname')
    author_portrait = serializers.URLField(source='author.portrait')
    class Meta:
        model = News
        fields = [
            "id",
            "title",
            "text",
            "released_timestamp",
            "cover_url",
            "author_nickname",
            "author_portrait"
        ]