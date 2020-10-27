from django.contrib import admin


from .models import *


l = [Team, Contests, Game, Commentary]
for i in l:
    admin.site.register(i)