from django.contrib import admin


from .models import *


l = [Post, Category]
for i in l:
    admin.site.register(i)