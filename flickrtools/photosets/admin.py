from flickrtools.photosets.models import *
from django.contrib import admin

class PhotoSetAdmin(admin.ModelAdmin):
    list_display=('uid','title')

admin.site.register(Photoset,PhotoSetAdmin)
