from django.shortcuts import render
from rest_framework import mixins, viewsets
from scripts.utils import ListPagination
from django_filters.rest_framework import DjangoFilterBackend


from .serializers import GameSerializer, CommentarySerializer
from .models import Game, Commentary
from .filters import CommentaryFilter
from scripts.utils import ListPagination


class GameList(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    pagenation_class = ListPagination
gamelist_view = GameList.as_view({'get': 'list'})


class CommentaryList(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = CommentarySerializer
    queryset = Commentary.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = CommentaryFilter
Commentary_view = CommentaryList.as_view({'get': 'list'})