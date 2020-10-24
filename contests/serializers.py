from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


from .models import Game
from scripts.utils import TimestampField


class GameSerializer(ModelSerializer):
    start_time_timestamp = TimestampField(source='start_time')
    end_time_timestamp = TimestampField(source='end_time')
    r_team_name = serializers.CharField(source='r_team.name')
    b_team_name = serializers.CharField(source='b_team.name')
    contests_name = serializers.CharField(source='contests.contests_name')
    class Meta:
        model = Game
        fields = [
            'id'
            'end_time_timestamp',
            'start_time_timestamp',
            'r_team_name',
            'b_team_name',
            'contests_name',
            'game_status',
            'is_end'
        ]