from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from rest_framework import serializers


from .models import News
from user.models import User
from scripts.utils import TimestampField


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'nickname',
            'portrait',
        ]


class NewsSerializer(ModelSerializer):
    released_timestamp = TimestampField(source='released_time')
    author = AuthorSerializer()
    class Meta:
        model = News
        fields = [
            'id',
            'title',
            'text',
            'views',
            'released_timestamp',
            'cover_url',

            'author'
        ]