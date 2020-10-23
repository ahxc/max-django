from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


from .models import Game
from scripts.utils import TimestampField


class GameSerializer(ModelSerializer):
    start_time_timestamp = TimestampField(source='start_time')
    end_time_timestamp = TimestampField(source='end_time')
    team_name = serializers.CharField(source='team.name')
    team_logo = serializers.CharField(source='team.logo')
    contests_name = serializers.CharField(source='contests.contests_name')
    class Meta:
        model = Game
        fields = [
            'end_time_timestamp',
            'start_time_timestamp',
            'code',
            'team_name',
            'team_logo',
            'contests_name',
            'game_status'
        ]