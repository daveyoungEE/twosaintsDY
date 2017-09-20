# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from main.models import Announcement

def index(request):
	announcements = Announcement.objects.all().order_by('-date')
	return render(request, 'main/index.html',{
		'announcements': announcements,
		})
def announcement_detail(request, id):
	try:
		announcement = Announcement.objects.get(id=id).order_by('-date')
	except: Announcement.DoesNotExist
	raise Http(404) ('this announcement does not exist')
	return render(request, 'main/announcement_detail.html', {
			'announcement': announcement,
		})
