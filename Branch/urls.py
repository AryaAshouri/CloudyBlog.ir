from django.views.generic import TemplateView
from django.urls import path
from .views import *
app_name = "Branch"

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('guide/', guide, name="guide"),
    path('signin', signin, name="signin"),
    path('signup', signup, name="signup"),
    path('blogs/', blogs, name="blogs"),
    path('courses/', courses, name="courses"),
    path('blog/<slug:slug>', blog, name="blog"),
    path('course/<slug:slug>', course, name="course"),
]