from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from user import views

router = routers.DefaultRouter()

urlpatterns = [
	path('admin/', admin.site.urls),
	path('api/', include(router.urls)),
	path('', include('news.urls')),
	path('', include('contests.urls')),

	path('index/', views.index),
	path('login/', views.login),
	path('logout/', views.logout),
	path('register/', views.register),
	path('confirm/', views.user_confirm),
	path('captcha/', include('captcha.urls')),

	path("api/auth/", include("rest_framework.urls", namespace="rest_framework")),
]