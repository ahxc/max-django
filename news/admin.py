from django.contrib import admin

from .models import News

class NewsAdmin(admin.ModelAdmin):
  list_display = ['id', 'title', 'text', 'views', 'released_time', 'link', 'cover_url']

admin.site.register(News, NewsAdmin)