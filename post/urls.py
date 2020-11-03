from django.urls import path


from .views import *


app_name = 'post'


urlpatterns = [
    path('api/community/post', post_view),
    path('api/community/category', category_view)
]