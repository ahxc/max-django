from django.contrib import admin


from .models import *


l = [User]
for i in l:
    admin.site.register(i)