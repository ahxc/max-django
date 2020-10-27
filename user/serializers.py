from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


from .models import User
from scripts.utils import TimestampField


class UserSerializer(ModelSerializer):
    c_timestamp = TimestampField(source='c_time')
    class Meta:
        model = User
        fields = [
            'id',
            'gender',
            'name',
            'nickname',
            'email',
            'sex',
            'c_timestamp',
            'is_activated',
            'portrait',
            'team'
        ]