from django.shortcuts import render
from rest_framework import mixins, viewsets
from scripts.utils import ListPagination


from .serializers import GameSerializer
from .models import Game
from scripts.utils import ListPagination


class GameList(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    pagenation_class = ListPagination
gamelist_view = GameList.as_view({'get': 'list'})