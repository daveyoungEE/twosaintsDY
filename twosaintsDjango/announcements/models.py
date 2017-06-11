# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

class Entry(models.Model):
	date = models.DateTimeField(default=datetime.now())
	title = models.CharField(max_length=256)
	body = models.TextField()
	upload = models.FileField(null=True)
	
