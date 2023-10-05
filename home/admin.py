from django.contrib import admin

from home.models import Artist, Song, Album

admin.site.register([Artist, Song, Album])
