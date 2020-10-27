from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from rest_framework import serializers


from .models import News
from user.models import User
from scripts.utils import TimestampField


class NewsSerializer(HyperlinkedModelSerializer):
    released_timestamp = TimestampField(source='released_time')
    class Meta:
        model = News
        fields = [
            'id',
            'title',
            'released_timestamp',
            'views',
            'cover_url'
        ]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'nickname',
            'portrait',
        ]


class DetailSerializer(ModelSerializer):
    released_timestamp = TimestampField(source='released_time')
    author = AuthorSerializer()
    class Meta:
        model = News
        fields = [
            'id',
            'title',
            'text',
            'released_timestamp',
            'cover_url',
            'author'
        ]