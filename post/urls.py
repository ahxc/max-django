from django.urls import path


from . import views


app_name = 'news'


urlpatterns = [
    path('api/community/post', views.post_view),
]