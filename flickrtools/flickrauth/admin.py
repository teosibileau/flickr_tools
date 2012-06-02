from flickrtools.flickrauth.models import *
from django.contrib import admin

class AccessAdmin(admin.ModelAdmin):
    list_display=('user','key','secret')

admin.site.register(Access,AccessAdmin)
