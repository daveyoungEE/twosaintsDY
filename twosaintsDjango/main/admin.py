# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Announcement

class AnnouncementAdmin(admin.ModelAdmin):
	list_display = ['date', 'title', 'body', 'upload']

admin.site.register(Announcement, AnnouncementAdmin)
