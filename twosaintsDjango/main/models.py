# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.utils import timezone

class Announcement(models.Model):
	date = models.DateTimeField(default=timezone.now)
	title = models.CharField(max_length=256)
	body = models.TextField()
	upload = models.FileField(upload_to='uploads/Announcement/%Y/%m/%d/', blank=True, null=True)
	
class Event(models.Model):
	date = models.DateField()
	time = models.TimeField()
	title = models.TextField(max_length=64)
	description = models.TextField()
	
