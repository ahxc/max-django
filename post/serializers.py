from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


from .models import Post, Category
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


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'category_icon',
            'is_parents',
            'parents_category',
            'describe',
        ]


class PostSerializer(ModelSerializer):
    modified_time_timestamp = TimestampField(source='modified_time')
    category = CategorySerializer()
    author = AuthorSerializer()
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'text',
            'views',
            'likes',
            'modified_time_timestamp',

            'category',
            'author'
        ]