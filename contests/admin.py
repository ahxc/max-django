from django.contrib import admin

from . import models

admin.site.register(models.Team)
admin.site.register(models.Contests)
admin.site.register(models.Game)