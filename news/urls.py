from django.urls import path


from . import views


app_name = 'news'


urlpatterns = [
    path('api/find/news', views.news_view),
]