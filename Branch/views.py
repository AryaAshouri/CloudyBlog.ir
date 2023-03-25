from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import CreateUserForm
from .models import *
app_name = "Branch"

def home(request):
	context = {"Articles" : Article.objects.filter(status = "p").order_by("-publish")[:3],
	"Courses" : Course.objects.filter(status = "p").order_by("-publish")[:3],
	"Notifs" : Notification.objects.filter(status = "p").order_by("-publish")[:2],}
	return render(request, "home.html", context)

def signup(request):
	form = CreateUserForm()
	if (request.method == "POST"):
		form = CreateUserForm(request.POST)
		if (form.is_valid()):
			form.save()
			return HttpResponseRedirect("/")
	context = {"form" : form}
	return render(request, "signup.html", context)

def signin(request):

	if (request.method == "POST"):
		username = request.POST.get("username")
		password = request.POST.get("password")

		user = authenticate(request, username=username, password=password)
		if (user is not None):
			login(request, user)
			return HttpResponseRedirect("/")
		else:
			return HttpResponseRedirect("/signin")
	return render(request, "signin.html")

def about(request):
	return render(request, "about.html")

def blogs(request):
	context = {"Articles" : Article.objects.filter(status = "p").order_by("-publish")}
	return render(request, "articles.html", context)

def courses(request):
	context = {"Courses" : Course.objects.filter(status = "p").order_by("-publish")}
	return render(request, "courses.html", context)

def course(request, slug):
	context = {"Course_Info" : Course.objects.get(slug=slug)}
	return render(request, "course.html", context)

def blog(request, slug):
	context = {"Article_Info" : Article.objects.get(slug=slug)}
	return render(request, "article.html", context)

def guide(request):
	return render(request, "guide.html")