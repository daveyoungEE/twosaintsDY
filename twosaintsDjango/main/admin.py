# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Event
from .models import Announcement
from .models import Blog

class AnnouncementAdmin(admin.ModelAdmin):
	list_display = ['date', 'title', 'body', 'upload']
class EventAdmin(admin.ModelAdmin):
	list_display = ['date', 'time', 'title', 'description']
class BlogAdmin(admin.ModelAdmin):
	list_display = ['date', 'title', 'body', 'upload']

admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Blog, BlogAdmin)
