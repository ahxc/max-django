# -*- coding: utf-8 -*-


from rest_framework import serializers


from .models import Game, Commentary, Team
from scripts.utils import TimestampField


class CommentarySerializer(serializers.ModelSerializer):
    timestamp = TimestampField(source='time')
    class Meta:
        model = Commentary
        fields = [
            "id",
            'timestamp',
            'story'
        ]


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = [
            'id',
            'logo',
            'name',
        ]


class GameSerializer(serializers.ModelSerializer):
    start_time_timestamp = TimestampField(source='start_time')
    end_time_timestamp = TimestampField(source='end_time')
    r_team = TeamSerializer()
    b_team = TeamSerializer()
    contests_name = serializers.CharField(source='contests.contests_name')
    class Meta:
        model = Game
        fields = [
            'id',
            'is_end',
            'game_status',
            'end_time_timestamp',
            'start_time_timestamp',

            'contests_name',
            'r_team',
            'b_team'
        ]