from django.contrib import admin


from .models import *


l = [News]
for i in l:
    admin.site.register(i)