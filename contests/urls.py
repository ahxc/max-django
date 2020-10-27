from django.urls import path

from . import views


app_name = 'contests'


urlpatterns = [
    path('api/contests/game', views.gamelist_view),
    path('api/contests/game/commentary', views.Commentary_view)
]