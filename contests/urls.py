from django.urls import path

from . import views


app_name = 'contests'


urlpatterns = [
    path('api/contests/game', views.gamelist_view),
]