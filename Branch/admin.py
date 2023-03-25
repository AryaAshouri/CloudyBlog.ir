from django.contrib import admin
from .models import *

class ArticleAdmin(admin.ModelAdmin):
	list_display = ("title", "slug", "publish", "status")
	list_filter = ("publish", "status")
	search_fields = ("title", "preamble")
	prepopulated_fields = {"slug" : ("title",)}
	ordering = ("publish", "status")
admin.site.register(Article, ArticleAdmin)

class CourseAdmin(admin.ModelAdmin):
	list_display = ("title", "publish", "status")
	list_filter = ("publish", "status")
	search_fields = ("title", "preamble")
	ordering = ("publish", "status")
admin.site.register(Course, CourseAdmin)

class NotificationAdmin(admin.ModelAdmin):
	list_display = ("title", "publish", "status")
	list_filter = ("publish", "status")
	search_fields = ("title", "preamble")
	ordering = ("publish", "status")
admin.site.register(Notification, NotificationAdmin)