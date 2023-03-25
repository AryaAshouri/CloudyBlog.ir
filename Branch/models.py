from django.db import models
from django.db import models
from django.utils import timezone

class Article(models.Model):
	status =  (
		("d", "Draft"),
		("p", "Publish")
	)

	title = models.CharField(max_length = 20)
	sitle = models.CharField(max_length = 20, unique = True, null = True)
	slug = models.SlugField(max_length = 20, unique = True)
	author = models.CharField(max_length = 20, null = True)
	preamble = models.CharField(max_length = 90, null = True)
	description = models.TextField(null = True, blank=True)
	Date = models.CharField(max_length = 20, null = True)
	update = models.CharField(max_length = 5, null = True)
	time = models.CharField(max_length = 20, null = True)
	thumbnail = models.ImageField(null=True, upload_to = "Images")
	publish = models.DateTimeField(default = timezone.now)
	created = models.DateTimeField(auto_now_add = True)
	created = models.DateTimeField(auto_now = True)
	status = models.CharField(max_length = 1, choices = status)
	def __str__(self):
		return self.title

class Course(models.Model):
	status =  (
		("d", "Draft"),
		("p", "Publish")
	)

	title = models.CharField(max_length = 20)
	sitle = models.CharField(max_length = 20, unique = True, null = True)
	slug = models.SlugField(max_length = 20, unique = True, null = True)
	teacher = models.CharField(max_length = 30, null = True)
	price = models.CharField(max_length = 20, null = True)
	preamble = models.CharField(max_length = 90, null = True)
	Date = models.CharField(max_length = 20, null = True)
	Topic = models.CharField(max_length = 20, null = True)
	thumbnail = models.ImageField(null=True, upload_to = "Images")
	Video = models.CharField(max_length = 100, null = True)
	publish = models.DateTimeField(default = timezone.now)
	created = models.DateTimeField(auto_now_add = True)
	created = models.DateTimeField(auto_now = True)
	status = models.CharField(max_length = 1, choices = status)
	def __str__(self):
		return self.title

class Notification(models.Model):
	status =  (
		("d", "Draft"),
		("p", "Publish")
	)

	title = models.CharField(max_length = 40)
	preamble = models.CharField(max_length = 120, null = True)
	Date = models.CharField(max_length = 20, null = True)
	publish = models.DateTimeField(default = timezone.now)
	created = models.DateTimeField(auto_now_add = True)
	created = models.DateTimeField(auto_now = True)
	status = models.CharField(max_length = 1, choices = status)
	def __str__(self):
		return self.title